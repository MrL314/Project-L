REM Check for source files needed for setup.
@echo off
title Setup Script 1.0
cls

IF EXIST ".\risc\bin\demo_kame.bin" (echo Found \risc files) ELSE (echo \risc files not found. & ECHO.  & ECHO.Copy the contents of archive: & ECHO.    \NEWS_05\NEWS_05\home\kimura\kart\risc.lzh & ECHO to: & ECHO.     %~dp0setup\risc\ & echo. & echo Then re-run setup.bat read the readme for more details.)
IF EXIST ".\risc\bin\demo_kame.bin" (cls) ELSE (pause)
IF EXIST ".\risc\bin\demo_kame.bin" (cls) ELSE (EXIT)

REM Make sure that the correct demo.asm is in use (if extracted with 7zip)


IF EXIST ".\risc\join\demo_1.asm" (ren ".\risc\join\demo.asm" "demo.asm.bak") ELSE (echo.)
IF EXIST ".\risc\join\demo_1.asm" (ren ".\risc\join\demo_1.asm" "demo.asm") ELSE (echo.)

IF EXIST ".\car\TITLE-ENG.CGX" (echo Found \CAR files) ELSE (echo \CAR files not found. & ECHO. & ECHO. & ECHO Copy the the contents of directory: & ECHO.    \NEWS_04\home\sugiyama\CAR & ECHO to: & ECHO.     %~dp0setup\CAR & echo. & echo Then re-run setup.bat read the readme for more details.)
IF EXIST ".\car\TITLE-ENG.CGX" (cls) ELSE (pause)
IF EXIST ".\car\TITLE-ENG.CGX" (cls) ELSE (EXIT)
 

IF EXIST ".\data\rom\rom1-p.DAT" (echo Found \data files) ELSE (echo \data files not found. & ECHO. & ECHO Copy the contents of archive: & ECHO.    \NEWS_05\NEWS_05\home\kimura\kart\data.lzh & ECHO to: & ECHO.     %~dp0setup\data & echo. & echo Then re-run setup.bat read the readme for more details.)
IF EXIST ".\data\rom\rom1-p.DAT" (cls) ELSE (pause)
IF EXIST ".\data\rom\rom1-p.DAT" (cls) ELSE (EXIT)

IF EXIST ".\mak\apu.asm" (echo Found \mak files) ELSE (echo \mak files not found. & ECHO. & ECHO. & ECHO Copy the contents of archive: & ECHO.   \NEWS_05\NEWS_05\home\kimura\kart\mak.lzh & ECHO to: & ECHO.     %~dp0setup\mak & echo. & echo Then re-run setup.bat read the readme for more details.)
IF EXIST ".\mak\apu.asm" (cls) ELSE (pause)
IF EXIST ".\mak\apu.asm" (cls) ELSE (EXIT)

IF EXIST ".\Super Mario Kart (USA).sfc" (echo Found ROM Found) ELSE (ECHO Copy "Super Mario Kart (USA).sfc" to %~dp0\ and re-run setup.bat note this must be a unheadered ROM image and named correctly)
IF EXIST ".\Super Mario Kart (USA).sfc" (cls) ELSE (pause)
IF EXIST ".\Super Mario Kart (USA).sfc" (cls) ELSE (EXIT)

REM Setup DAT folder
MKDIR .\..\Source\DAT\
REM NEWS\テープリストア\NEWS_05\NEWS_05\home\kimura\kart\data
MKDIR .\..\Source\Assets\
xcopy /s /y .\data .\..\Source\Assets

REM NEWS\テープリストア\NEWS_05\NEWS_05\home\kimura\kart\risc
MKDIR .\..\Source\Assets\sound
MKDIR .\..\Source\Assets\bin
xcopy /s /y .\risc\sound\*.sss .\..\Source\Assets\sound
xcopy /s /y .\risc\bin .\..\Source\Assets\bin

REM NEWS\テープリストア\NEWS_04\NEWS_04\home\sugiyama\CAR

xcopy /s /y .\CAR\TITLE-ENG.CGX .\..\Source\Assets\title
xcopy /s /y .\CAR\TITLE.COL .\..\Source\Assets\title
xcopy /s /y .\CAR\REGI.COL .\..\Source\Assets\title
xcopy /s /y .\CAR\TITLE-ENG.SCR .\..\Source\Assets\title
xcopy /s /y .\CAR\TITLE2-ENG.SCR .\..\Source\Assets\title
xcopy /s /y .\CAR\D-POINT-ENG.SCR .\..\Source\Assets\title


xcopy /s /y .\CAR\CAR-SELECT.SCR .\..\Source\Assets\select
xcopy /s /y .\CAR\CAR-SELECT2-ENG.SCR .\..\Source\Assets\select	
xcopy /s /y .\CAR\CAR-SELECT3.SCR .\..\Source\Assets\select
xcopy /s /y .\CAR\CAR-SELECT.COL .\..\Source\Assets\select
xcopy /s /y .\CAR\SELECT-ENG.CGX .\..\Source\Assets\select
xcopy /s /y .\CAR\MAP-SELECT2.SCR .\..\Source\Assets\select
xcopy /s /y .\CAR\MAP-SELECT-ENG.COL .\..\Source\Assets\select
xcopy /s /y .\CAR\DEMO-MOJI.CGX .\..\Source\Assets\select

xcopy /s /y .\Resources\se.ROM .\..\Source\Assets\rom
xcopy /s /y .\Resources\select-e.ROM .\..\Source\Assets\select
xcopy /s /y .\Resources\title-e.ROM .\..\Source\Assets\title 

xcopy /s /y .\Resources\ROM1-e.txt .\..\Source\Assets\rom
xcopy /s /y .\Resources\ROM2-e.txt .\..\Source\Assets\rom
xcopy /s /y .\Resources\ROM3-e.txt .\..\Source\Assets\rom
xcopy /s /y .\Resources\ROM4-e.txt .\..\Source\Assets\rom


 
.\..\Tools\DATBuilder\DATBuilder.exe .\..\Source\Assets\rom\se.ROM .\..\Source\Assets\sound\se.bin



title Setup Script 1.0
REM
REM Edit the below to the name of the tools you want to use to compress, decompress and build DAT files.
REM
SET compress=.\recomp.exe
SET LundaCompressPerams=0 4 0
SET LundaDecompressPerams=0 4 0
SET decomp=.\decomp.exe
SET buildDAT=toDat.py
SET DLL="Lunar Compress.dll"
SET ToolsPath=.\..\tools\Compress\
SET ROM=".\Super Mario Kart (USA).sfc"
SET createSourcePath="createSource\"
SET createSource="createSource.exe"
REM
REM Edit the name of ROM files to build to DAT
REM
SET ROM1=rom1-e.txt
SET ROM2=rom2-e.txt
SET ROM3=rom3-e.txt
SET ROM4=rom4-e.txt
cls
ECHO Creating Source Code
cd %ToolsPath%..\%createSourcePath%
%createSource%
cd .\..\..\setup
PAUSE 


GOTO :extractAll
pause
EXIT



:extractAll
call :decompress lost ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 48000
call :decompress circuit ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 481C9
call :decompress castle ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 48F6A
call :decompress sand  ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 49C19
call :decompress dart ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 78000
call :decompress pole ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 0
call :decompress mogura ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 5D6
call :decompress water ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 903
call :decompress checker ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx BB7
call :decompress ball ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx E96
call :decompress dossun ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 1070
call :decompress ice ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 14EE
call :decompress pakkun ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 10AA5 
call :decompress dokan ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 10F9B
call :decompress abc ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 112F8 
call :decompress pukupuku ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 11706
call :decompress perapera ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 11C0E
call :decompress mark ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 30000
call :decompress moji-e ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx  70000
call :decompress item ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 40000
call :decompress item ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 40594
call :decompress star ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 41EBB
call :decompress grass ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 50000
call :decompress sand ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 51636
call :decompress killer ".\..\Source\Assets\obj\others\" ".\..\..\..\..\setup" cgx 60000
call :decompress obake ".\..\Source\Assets\mode7\chr\" ".\..\..\..\..\setup" cm7 60189
call :decompress sand ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 4C800
call :decompress castle ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 4CC3A
call :decompress dart ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 4CFAF
call :decompress title ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 49801
call :decompress star ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 6FA73
call :decompress ending ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 7F18D
call :decompress final02 ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 7FBE1
call :decompress obake ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 334
call :decompress final01 ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 21A83
call :decompress grass ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 30B9D
call :decompress select ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 61E28
call :decompress circuit ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 76301
call :decompress battle ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 76876
call :decompress ice ".\..\Source\Assets\sound\" ".\..\..\..\setup" music 76D16
call :decompress circuit ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 20000
call :decompress circuit ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 20946
call :decompress obake ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 20148
call :decompress obake ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 20B34
call :decompress grass ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 20356
call :decompress grass ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 20CF3
call :decompress castle ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 20523
call :decompress castle ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 20E85
call :decompress ice ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 205EB
call :decompress ice ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 21126
call :decompress dart ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 206B5
call :decompress dart ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 2124C
call :decompress sand ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 208A2
call :decompress sand ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 213A8
call :decompress star ".\..\Source\Assets\back\chr\" ".\..\..\..\..\setup" cgx 1499
call :decompress star ".\..\Source\Assets\back\scr\" ".\..\..\..\..\setup" scr 7718A
call :decompress bg-data ".\..\Source\Assets\bin\" ".\..\..\..\setup" bin 7FDBA
call :decompress tan-data ".\..\Source\Assets\bin\" ".\..\..\..\setup" bin 61F46
call :decompress ending ".\..\Source\Assets\color\" ".\..\..\..\setup" col 31F7F
call :decompress circuit ".\..\Source\Assets\color\" ".\..\..\..\setup" col 4117F
call :decompress obake ".\..\Source\Assets\color\" ".\..\..\..\setup" col 41313
call :decompress grass ".\..\Source\Assets\color\" ".\..\..\..\setup" col 414C4
call :decompress castle ".\..\Source\Assets\color\" ".\..\..\..\setup" col 41675
call :decompress ice ".\..\Source\Assets\color\" ".\..\..\..\setup" col 4182F
call :decompress dart ".\..\Source\Assets\color\" ".\..\..\..\setup" col 419C0
call :decompress sand ".\..\Source\Assets\color\" ".\..\..\..\setup" col 41B5B
call :decompress star ".\..\Source\Assets\color\" ".\..\..\..\setup" col 41D0B
GOTO Exit



:decompress
REM Args 1 filename 2 path 3 return path 4 file extention 5 offset

copy %ToolsPath%%decomp% %2 /y
copy %ToolsPath%%dll% %2 /y
copy %ROM% %2 /y

cd %2
cls
REM prompt Running Command: 

%decomp% %ROM% %1.%4 %5 4 0
del %decomp%
del %dll%
del %ROM%
cd %3
prompt
exit /b
:Exit
echo Setup complete > setup
cls