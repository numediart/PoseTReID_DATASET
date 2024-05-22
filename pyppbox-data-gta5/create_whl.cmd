::    MIT License
::    Copyright (c) [2023] [Ratha SIV]
::    pyppbox-data-gta5: The restructured GTA_V_DATASET for pyppbox V3+.

@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python -m pip install --upgrade pip
pip install wheel build
python -m build --wheel --skip-dependency-check --no-isolation
pause