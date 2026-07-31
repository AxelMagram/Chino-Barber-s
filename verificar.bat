@echo off
REM ============================================================
REM  Chino Barber - Verificacion de cierre de paso
REM  Correr desde C:\Chino Barber con: verificar.bat
REM ============================================================

echo.
echo === 1) Generando migraciones (si hay cambios en modelos) ===
python manage.py makemigrations

echo.
echo === 2) Aplicando migraciones a la base de datos ===
python manage.py migrate

echo.
echo === 3) Chequeo de integridad del proyecto ===
python manage.py check

echo.
echo === 4) Estado de git (archivos pendientes de subir) ===
git status

echo.
echo ============================================================
echo  Si todo salio OK, para subir a git:
echo    git add .
echo    git commit -m "Paso X: descripcion"
echo    git push
echo ============================================================
pause
