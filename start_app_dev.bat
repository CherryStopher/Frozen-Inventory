@echo off

REM Run front
start cmd /k "cd front && npm run dev"

REM Run back
start cmd /k "cd back && env\Scripts\activate && cd app && uvicorn main:app"

@echo on