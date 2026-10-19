"""Start and stop this local SoulLink deployment without visible terminal windows."""
import argparse
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import time
import urllib.request

import psutil

ROOT = Path(__file__).resolve().parent.parent
APP = ROOT / 'soullink13'
DEPLOY = ROOT / 'deployment'
STATE = DEPLOY / 'processes.json'


def read_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def owned_process(record):
    try:
        process = psutil.Process(record['pid'])
        return process if abs(process.create_time() - record['created']) < 1 else None
    except psutil.NoSuchProcess:
        return None


def launch(name, command, cwd, state):
    if name in state and owned_process(state[name]):
        return
    environment = os.environ.copy()
    environment.update(json.loads((DEPLOY / 'runtime.env.json').read_text(encoding='utf-8')))
    environment['PATH'] = str(Path(sys.executable).parent) + os.pathsep + environment['PATH']
    with (DEPLOY / f'{name}.log').open('w', encoding='utf-8') as output:
        process = subprocess.Popen(command, cwd=cwd, env=environment, stdin=subprocess.DEVNULL,
                                   stdout=output, stderr=subprocess.STDOUT,
                                   creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    state[name] = {'pid': process.pid, 'created': psutil.Process(process.pid).create_time()}
    STATE.write_text(json.dumps(state, indent=2))


def wait_port(port, timeout=30):
    until = time.monotonic() + timeout
    while time.monotonic() < until:
        try:
            with socket.create_connection(('127.0.0.1', port), timeout=1):
                return
        except OSError:
            time.sleep(0.5)
    raise RuntimeError(f'Port {port} did not start. See deployment/*.log')


def start():
    state = read_state()
    ssh = shutil.which('ssh')
    node = shutil.which('node')
    if not ssh or not node:
        raise RuntimeError('OpenSSH and Node.js must be installed and available on PATH')
    command = [ssh, '-N', '-T', '-i', str(Path.home() / '.ssh/soullink-deploy-key'),
               '-p', '28890', '-o', 'BatchMode=yes', '-o', 'ExitOnForwardFailure=yes',
               '-o', 'ConnectTimeout=15', '-o', 'ServerAliveInterval=30',
               '-o', 'ServerAliveCountMax=3', '-o', 'StrictHostKeyChecking=yes']
    forwards = {18000: '192.168.11.28:8000', 18081: '172.17.0.4:8081',
                17860: '172.17.0.4:7860', 17861: '172.17.0.4:7861',
                18765: '172.17.0.4:18765', 10197: '172.17.0.4:10197'}
    for local_port, target in forwards.items():
        command.extend(['-L', f'127.0.0.1:{local_port}:{target}'])
    command.append('zhushiyu10+@211.87.224.136')
    launch('tunnel', command, ROOT, state)
    wait_port(18000)
    launch('backend', [sys.executable, '-u', 'main.py', 'start'], APP, state)
    wait_port(5002, timeout=90)
    frontend = APP / 'soullink'
    launch('frontend', [node, str(frontend / 'node_modules/vite/bin/vite.js'),
                        '--host', '127.0.0.1', '--port', '5173', '--strictPort'], frontend, state)
    wait_port(5173)
    print('SoulLink: http://127.0.0.1:5173')
    print('Backend:  http://127.0.0.1:5002')


def stop():
    state = read_state()
    for name in ('frontend', 'backend', 'tunnel'):
        record = state.get(name)
        process = owned_process(record) if record else None
        if process:
            children = process.children(recursive=True)
            for child in reversed(children):
                try:
                    child.terminate()
                except psutil.NoSuchProcess:
                    pass
            process.terminate()
            _, pending = psutil.wait_procs([process, *children], timeout=5)
            for pending_process in pending:
                try:
                    pending_process.kill()
                except psutil.NoSuchProcess:
                    pass
            print(f'Stopped {name}')
    STATE.write_text('{}')


def status():
    for name, record in read_state().items():
        print(f'{name}: {"running" if owned_process(record) else "stopped"} (PID {record["pid"]})')
    for url in ('http://127.0.0.1:5002/health', 'http://127.0.0.1:5173'):
        try:
            with urllib.request.urlopen(url, timeout=5) as response:
                print(f'{url}: HTTP {response.status}')
        except Exception as error:
            print(f'{url}: {error}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'stop', 'status', 'restart'])
    action = parser.parse_args().action
    if action in ('stop', 'restart'):
        stop()
    if action in ('start', 'restart'):
        start()
    if action == 'status':
        status()
