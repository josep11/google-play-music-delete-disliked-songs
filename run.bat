@echo off
echo Google Play Music Delete Disliked Songs
set iniDir=%~dp0
python %iniDir%main.py >> info.log 2>> error.log
