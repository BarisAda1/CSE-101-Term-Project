@echo off
if exist __pycache__ rmdir /s /q __pycache__
python -B main.py
pause