@echo off
setlocal EnableDelayedExpansion

REM If no message provided, use default
if "%~1"=="" (
    set "msg=AI update"
) else (
    set "msg=%~1"
)

git pull origin main --rebase
git add .
git commit -m "%msg%"
git push origin main