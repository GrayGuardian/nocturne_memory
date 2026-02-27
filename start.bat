@echo off
chcp 65001 >nul
title Nocturne Memory WebUI

echo ========================================
echo   Nocturne Memory - Starting...
echo ========================================
echo.

REM Start Backend
echo [1/2] Starting Backend (port 8000)...
start "Nocturne-Backend" cmd /k "cd /d %~dp0backend && py -m uvicorn main:app --reload --port 8000"

timeout /t 2 /nobreak >nul

REM Start Frontend
echo [2/2] Starting Frontend...
start "Nocturne-Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo ========================================
echo   Both services started!
echo   Backend:  http://localhost:8000
echo   Frontend: Check the terminal for URL
echo ========================================
echo.
pause >nul
