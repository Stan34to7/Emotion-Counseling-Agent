"""Offline Windows speech adapter for the local deployment."""
from pathlib import Path
import uuid

import pythoncom
import win32com.client

from utils import util


class Speech:
    def connect(self):
        util.log(1, 'Windows 本地中文语音已就绪')

    def close(self):
        pass

    def to_sample(self, text, style):
        if not str(text).strip():
            return None
        pythoncom.CoInitialize()
        stream = None
        try:
            voice = win32com.client.Dispatch('SAPI.SpVoice')
            tokens = list(voice.GetVoices())
            chinese = next((token for token in tokens
                            if 'chinese' in token.GetDescription().lower()), None)
            if chinese is not None:
                voice.Voice = chinese
            output = Path('samples') / f'sample-{uuid.uuid4().hex}.wav'
            output.parent.mkdir(exist_ok=True)
            stream = win32com.client.Dispatch('SAPI.SpFileStream')
            stream.Format.Type = 22  # 22.05 kHz, 16-bit, mono PCM
            stream.Open(str(output.resolve()), 3)
            voice.AudioOutputStream = stream
            voice.Speak(str(text), 0)
            stream.Close()
            stream = None
            return str(output)
        except Exception as error:
            util.log(1, f'Windows 本地语音生成失败: {error}')
            return None
        finally:
            if stream is not None:
                stream.Close()
            pythoncom.CoUninitialize()
