@echo off
cd /d "%~dp0"
REM Start a static file server on port 8000 (serves repo root)
start "Static Server" cmd /k "python -m http.server 8000"
REM Start netlify-cms proxy server for GitHub auth in the current window
npx netlify-cms-proxy-server
pause
