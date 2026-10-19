$ErrorActionPreference = 'Stop'
& "$PSScriptRoot\.venv\Scripts\python.exe" "$PSScriptRoot\deployment\manage.py" start
if ($LASTEXITCODE -ne 0) { throw 'SoulLink startup failed. Check deployment logs.' }
