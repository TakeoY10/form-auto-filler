@echo off
title Automação - Inicializador

:: Solicita elevação de privilégios para Administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissoes de Administrador...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Define o diretório atual onde o arquivo .bat está localizado (ex: Área de Trabalho)
cd /d "%~dp0"

echo ======================================================
echo  Diretorio atual: %cd%
echo ======================================================

:: Verifica se o arquivo Python existe no mesmo diretório
if not exist "Automacao.py" (
    echo [ERRO] O arquivo 'Automacao.py' nao foi encontrado nesta pasta!
    echo Certifique-se de que o arquivo 'Automacao.py' esta na mesma pasta/local do .bat.
    pause
    exit /b
)

echo A iniciar o script Python...
python Automacao.py

echo.
echo Script finalizado ou interrompido.
pause