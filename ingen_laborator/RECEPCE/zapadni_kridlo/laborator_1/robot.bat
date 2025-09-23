REM Tady je pouze kod.
REM Robota spustis tak, ze napises robot (nebo robot.bat)
REM do prikazoveho radku a zmacknes enter

























@echo off
cls
echo.
echo.
echo Dobry. Den. Co. Pro. Vas. Mohu. Zanalyzovat?
echo.

choice /c:kopln /n Zmacknete prvni pismeno predmetu, ktery chcete analyzovat. Napr. pro lopatu zmacknete L. Pro konec stiknete K.

if errorlevel 5 goto nuz
if errorlevel 4 goto hello
if errorlevel 3 goto there
if errorlevel 2 goto generalkenobi
if errorlevel 1 goto end







:nuz
cls
echo.
echo Analyzuji... Na nozi nejsou zadne prokazatelne otisky
echo.
goto end

:hello
cls
echo.
echo Lopata je pouze priklad. Spuste znovu a zadejte prvni pismenko Vaseho predmetu
echo.
goto end

:there
cls
echo.
echo Analyzuji... Na pacidlu je otisk prstu doktora Fialy
echo.
goto end

:generalkenobi
cls
echo.
echo Analyzuji... Toto je otisk prstu doktora Fialy
echo.
goto end

:end
