@echo off
setlocal

set /p PID=<process_id.txt

if "%PID%"=="" (
    echo No se pudo leer el ID del proceso. Asegúrate de que el archivo process_id.txt existe.
    endlocal
    exit /b 1
)

taskkill /PID %PID% /F

echo Listener detenido. Proceso con ID %PID% terminado.
endlocal
pause
