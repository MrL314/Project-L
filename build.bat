��
@echo off
cls
title ROM Builder 1.1

REM Check setup has been run

IF EXIST ".\setup\setup" (echo Found Setup!) ELSE (echo Setup not detected, run \Setup\setup.bat first. See the readme and try again.)
IF EXIST ".\setup\setup" (cls) ELSE (pause)
IF EXIST ".\setup\setup" (cls) ELSE (EXIT)


REM
REM Edit the below to the name of the tools you want to use to compress, decompress and build DAT files.
REM
SET comppath=".\Compress\"
SET DATpath=".\DATBuilder\"
SET compress=EpicCompress.exe
SET decomp=EpicCompress.exe
SET ToolsPath=".\tools\"
SET game=".\OUTPUT\Super Mario Kart (U).sfc"


SET buildDAT=DATBuilder.exe

SET CompilerPath=".\tools\as65c\"
SET Compiler=.\createROM.bat

REM
REM Setting the region to build - Default US
REM
SET REGION= NTSC-US
REM
REM Edit the name of ROM files to build to DAT - Default US
REM
SET ROM1=ROM1-E.txt
SET ROM2=ROM2-E.txt
SET ROM3=ROM3-E.txt
SET ROM4=ROM4-E.txt
REM
REM Edit the name of DAT files to output - Default US
REM
SET DAT1=".\..\..\DAT\ROM1-E.DAT"
SET DAT2=".\..\..\DAT\ROM2-E.DAT"
SET DAT3=".\..\..\DAT\ROM3-E.DAT"
SET DAT4=".\..\..\DAT\ROM4-E.DAT"

SET track=

SET DEBUG_TOGGLE=DEBUG_OFF
SET WAIT=

:MENU
@echo off
cd %~dp0
title ROM Builder 1.1
IF "%DEBUG_TOGGLE%"=="DEBUG_OFF" (
	SET Build_Mode=Retail
) ELSE (
	SET Build_Mode= Debug
)
IF "%WAIT%"=="-wait" (
	SET Wait_Mode=On 
) ELSE (
	SET Wait_Mode=Off
)

SET M=nul
cls
color 0

ECHO						The SMK Workshop ROM Builder (ver. 1.1)                            
ECHO                                                                                           [ROM Target: %REGION% %Build_Mode%]
ECHO  0) Build all
ECHO  1) Build DAT files
ECHO  2) Compress all files
ECHO	   View values to build individual assets:
ECHO		B) Track Backgrounds
ECHO		G) Graphics
ECHO		M) Music
ECHO		P) Pallets
ECHO		T) Tracks
ECHO		O) Other
ECHO.
ECHO  3) Build all data packs
ECHO       Build individual data packs:
ECHO		31) Lakitu, Shadow and Coins
ECHO		32) Title + Results (Eng)
REM ECHO		33) Title + Results (Jap)
ECHO		34) Podium (Eng)
REM ECHO		35) Podium (Jap)
ECHO		36) Player Select (Eng)
REM ECHO		37) Player Select (Jap)
ECHO.
ECHO  4) Compile ROM (The output ROM will be in .\OUTPUT\)
ECHO		41) Only add assets to existing code file
ECHO		42) Toggle retail or debug version build (Currently: %Build_Mode%)
ECHO.
ECHO  5) Load ROM
ECHO  6) Exit											           	?) Help
ECHO.
SET /P M=Type your option then press ENTER: 

IF /I %M%==? cls
IF /I %M%==? more ".\readme.txt"
IF /I %M%==? pause
IF /I %M%==p GOTO :PalletMenu
IF /I %M%==g GOTO :GraphicsMenu
IF /I %M%==m GOTO :MusicMenu
IF /I %M%==t GOTO :TrackMenu
IF /I %M%==o GOTO :OtherMenu
IF /I %M%==b GOTO :BackgroundsMenu
IF /I %M%==5 GOTO :Load
IF /I %M%==0 call :BuildAll
IF /I %M%==1 GOTO BuildAllDAT
IF /I %M%==2 GOTO CompressAll
IF /I %M%==t1 call :TrackCompress sand01 ".\source\assets\mode7\scr\sand\" scr
IF /I %M%==t2 call :TrackCompress star01 ".\source\assets\mode7\scr\star\" scr
IF /I %M%==t3 call :TrackCompress circuit01 ".\source\assets\mode7\scr\circuit\" scr
IF /I %M%==t4 call :TrackCompress circuit02 ".\source\assets\mode7\scr\circuit\" scr
IF /I %M%==t5 call :TrackCompress circuit03 ".\source\assets\mode7\scr\circuit\" scr
IF /I %M%==t6 call :TrackCompress obake02 ".\source\assets\mode7\scr\obake\" scr
IF /I %M%==t7 call :TrackCompress grass01 ".\source\assets\mode7\scr\grass\" scr
IF /I %M%==t8 call :TrackCompress ice01 ".\source\assets\mode7\scr\ice\" scr
IF /I %M%==t9 call :TrackCompress dart02 ".\source\assets\mode7\scr\dart\" scr
IF /I %M%==t10 call :TrackCompress sand02 ".\source\assets\mode7\scr\sand\" scr
IF /I %M%==t11 call :TrackCompress battle06 ".\source\assets\mode7\scr\battle\" scr
IF /I %M%==t12 call :TrackCompress obake03 ".\source\assets\mode7\scr\obake\" scr
IF /I %M%==t13 call :TrackCompress grass02 ".\source\assets\mode7\scr\grass\" scr
IF /I %M%==t14 call :TrackCompress grass03 ".\source\assets\mode7\scr\grass\" scr
IF /I %M%==t15 call :TrackCompress castle03 ".\source\assets\mode7\scr\castle\" scr
IF /I %M%==t16 call :TrackCompress castle01 ".\source\assets\mode7\scr\castle\" scr
IF /I %M%==t17 call :TrackCompress castle02 ".\source\assets\mode7\scr\castle\" scr
IF /I %M%==t18 call :TrackCompress obake01 ".\source\assets\mode7\scr\obake\" scr
IF /I %M%==t19 call :TrackCompress battle03 ".\source\assets\mode7\scr\battle\" scr
IF /I %M%==t20 call :TrackCompress battle02 ".\source\assets\mode7\scr\battle\" scr
IF /I %M%==t21 call :TrackCompress battle05 ".\source\assets\mode7\scr\battle\" scr
IF /I %M%==t22 call :TrackCompress ice02 ".\source\assets\mode7\scr\ice\" scr
IF /I %M%==t23 call :TrackCompress circuit04 ".\source\assets\mode7\scr\circuit\" scr
IF /I %M%==t24 call :TrackCompress dart03 ".\source\assets\mode7\scr\dart\" scr
IF /I %M%==314 color 0A 
IF /I %M%==mario color 04
IF /I %M%==dirtbag color 05
IF /I %M%==clean call :clean_up
IF /I %M%==fullclean call :full_clean_up


IF /I %M%==G1 call :compress lost ".\source\assets\obj\others\" cgx
IF /I %M%==G2 call :compress circuit ".\source\assets\mode7\chr\" cm7
IF /I %M%==G3 call :compress castle ".\source\assets\mode7\chr\" cm7
IF /I %M%==G4 call :compress sand  ".\source\assets\obj\others\" cgx
IF /I %M%==G5 call :compress dart ".\source\assets\mode7\chr\" cm7
IF /I %M%==G6 call :compress pole ".\source\assets\obj\others\" cgx
IF /I %M%==G7 call :compress mogura ".\source\assets\obj\others\" cgx
IF /I %M%==G8 call :compress water ".\source\assets\obj\others\" cgx
IF /I %M%==G9 call :compress checker ".\source\assets\obj\others\" cgx
IF /I %M%==G10 call :compress ball ".\source\assets\obj\others\" cgx
IF /I %M%==G11 call :compress dossun ".\source\assets\obj\others\" cgx
IF /I %M%==G12 call :compress ice ".\source\assets\mode7\chr\" cm7
IF /I %M%==G13 call :compress pakkun ".\source\assets\obj\others\" cgx
IF /I %M%==G14 call :compress dokan ".\source\assets\obj\others\" cgx
IF /I %M%==G15 call :compress abc ".\source\assets\back\chr\" cgx
IF /I %M%==G16 call :compress pukupuku ".\source\assets\obj\others\" cgx
IF /I %M%==G17 call :compress perapera ".\source\assets\obj\others\" cgx
IF /I %M%==G18 call :compress mark ".\source\assets\obj\others\" cgx
IF /I %M%==G19 call :compress moji-e ".\source\assets\back\chr\" cgx
IF /I %M%==G20 call :compress item ".\source\assets\mode7\chr\" cm7
IF /I %M%==G21 call :compress item ".\source\assets\obj\others\" cgx
IF /I %M%==G22 call :compress star ".\source\assets\mode7\chr\" cm7
IF /I %M%==G23 call :compress grass ".\source\assets\mode7\chr\" cm7
IF /I %M%==G24 call :compress sand ".\source\assets\mode7\chr\" cm7
IF /I %M%==G25 call :compress killer ".\source\assets\obj\others\" cgx
IF /I %M%==G26 call :compress obake ".\source\assets\mode7\chr\" cm7



IF /I %M%==M1 call :compress sand ".\source\assets\sound\" music
IF /I %M%==M2 call :compress castle ".\source\assets\sound\" music
IF /I %M%==M3 call :compress dart ".\source\assets\sound\" music
IF /I %M%==M4 call :compress title ".\source\assets\sound\" music
IF /I %M%==M5 call :compress star ".\source\assets\sound\" music
IF /I %M%==M6 call :compress ending ".\source\assets\sound\" music
IF /I %M%==M7 call :compress final02 ".\source\assets\sound\" music
IF /I %M%==M8 call :compress obake ".\source\assets\sound\" music
IF /I %M%==M9 call :compress final01 ".\source\assets\sound\" music
IF /I %M%==M10 call :compress grass ".\source\assets\sound\" music
IF /I %M%==M11 call :compress select ".\source\assets\sound\" music
IF /I %M%==M12 call :compress circuit ".\source\assets\sound\" music
IF /I %M%==M13 call :compress battle ".\source\assets\sound\" music
IF /I %M%==M14 call :compress ice ".\source\assets\sound\" music



IF /I %M%==B1 call :compress circuit ".\source\assets\back\chr\" cgx
IF /I %M%==B2 call :compress circuit ".\source\assets\back\scr\" scr
IF /I %M%==B3 call :compress obake ".\source\assets\back\chr\" cgx
IF /I %M%==B4 call :compress obake ".\source\assets\back\scr\" scr
IF /I %M%==B5 call :compress grass ".\source\assets\back\chr\" cgx
IF /I %M%==B6 call :compress grass ".\source\assets\back\scr\" scr
IF /I %M%==B7 call :compress castle ".\source\assets\back\chr\" cgx
IF /I %M%==B8 call :compress castle ".\source\assets\back\scr\" scr
IF /I %M%==B9 call :compress ice ".\source\assets\back\chr\" cgx
IF /I %M%==B10 call :compress ice ".\source\assets\back\scr\" scr
IF /I %M%==B11 call :compress dart ".\source\assets\back\chr\" cgx
IF /I %M%==B12 call :compress dart ".\source\assets\back\scr\" scr
IF /I %M%==B13 call :compress sand ".\source\assets\back\chr\" cgx
IF /I %M%==B14 call :compress sand ".\source\assets\back\scr\" scr
IF /I %M%==B15 call :compress star ".\source\assets\back\chr\" cgx
IF /I %M%==B16 call :compress star ".\source\assets\back\scr\" scr

IF /I %M%==O1 call :compress bg-data ".\source\assets\bin\" bin
IF /I %M%==O2 call :compress tan-data ".\source\assets\bin\" bin

IF /I %M%==P1 call :compress ending ".\source\assets\color\" col
IF /I %M%==P2 call :compress circuit ".\source\assets\color\" col
IF /I %M%==P3 call :compress obake ".\source\assets\color\" col
IF /I %M%==P4 call :compress grass ".\source\assets\color\" col
IF /I %M%==P5 call :compress castle ".\source\assets\color\" col
IF /I %M%==P6 call :compress ice ".\source\assets\color\" col
IF /I %M%==P7 call :compress dart ".\source\assets\color\" col
IF /I %M%==P8 call :compress sand ".\source\assets\color\" col
IF /I %M%==P9 call :compress star ".\source\assets\color\" col


IF /I %M%==3 GOTO BuildAllDataPacks
IF /I %M%==31 call :J-S-C


IF /I %M%==32 call :title-e ".\..\..\..\..\"
REM IF /I %M%==33 call :title-j
IF /I %M%==34 call :final-e 
REM IF /I %M%==35 call :podium-j
IF /I %M%==36 call :select-e 
REM IF /I %M%==37 call :select-j
IF /I %M%==4 call :compile_all

REM IF /I %M%==40 call :compile_code
IF /I %M%==41 call :compile_assets
IF /I %M%==42 call :toggle_debug
IF /I %M%==wait call :toggle_wait


IF /I %M%==6  GOTO Exit
GOTO MENU

:BuildAll
call :J-S-C
call :select-e
call :final-e
call :title-e
call :CompressAllCommand
call :BuildAllDATfunction
call :compile_all
GOTO MENU

:BuildAllDataPacks
call :J-S-C
call :select-e
call :final-e
call :title-e
GOTO MENU

:J-S-C
@echo off
call :BuildPack j-s-c.ROM ".\source\assets\obj\others" j-s-c.DAT 4992
call :compress j-s-c ".\source\assets\obj\others" DAT
del ".\source\assets\obj\others\j-s-c.bin"
rename ".\source\assets\obj\others\j-s-c.cpr" j-s-c.bin
exit /b

:select-e
@echo off
call :BuildPack select-e.ROM ".\source\assets\select" select-e.DAT 16320
call :compress select-e ".\source\assets\select" DAT
del ".\source\assets\select\select-e.bin"
rename ".\source\assets\select\select-e.cpr" select-e.bin
exit /b

:final-e
@echo off
call :BuildPack final-e.ROM ".\source\assets\final" final-e.DAT 18944
call :TrackCompress final-e ".\source\assets\final" DAT
exit /b

:title-e
@echo off
call :BuildPack title-e.ROM ".\source\assets\title" title-e.DAT 17408
call :compress title-e ".\source\assets\title" DAT

del ".\source\assets\title\title-e.bin"
rename ".\source\assets\title\title-e.cpr" title-e.bin

exit /b


:TrackMenu
cls
ECHO.
ECHO Track layouts menu values:
ECHO.
ECHO 	T1) Koopa Beach 2 (sand01)			T13) Donut Plains 3 (grass02)
ECHO		T2) Rainbow Road (star01)			T14) Donut Plains 1 (grass03)
ECHO 	T3) Mario Circuit 3 (circuit01)			T15) Bowser Castle 1 (castle03)
ECHO 	T4) Mario Circuit 1 (circuit02)			T16) Bowser Castle 2 (castle01)
ECHO 	T5) Mario Circuit 4 (circuit03)			T17) Bowser Castle 3 (castle02)
ECHO 	T6) Ghost Valley 3 (obake02)			T18) Ghost Valley 2 (obake01)
ECHO 	T7) Donut Plains 2 (grass01)			T19) Battle Course 4 (battle03)
ECHO 	T8) Vanilla Lake 2 (ice01)			T20) Battle Course 3 (battle02)
ECHO 	T9) Choco Island 2 (dart02)			T21) Battle Course 2 (battle05)
ECHO 	T10) Koopa Beach 1 (sand02)			T22) Vanilla Lake 1 (ice02)
ECHO 	T11) Battle Course 1 (battle06)			T23) Mario Circuit 2 (circuit04)
ECHO 	T12) Ghost Valley 1 (obake03)			T24) Choco Island 1 (dart03)
ECHO.
ECHO 	Enter value at the main menu to compress the track.
ECHO. 
Pause
GOTO MENU

:GraphicsMenu
cls
ECHO.
ECHO Graphics layouts menu values:
ECHO.
ECHO		G1) Loser disappearance cloud sprite (lost)	G14) Pipe sprite (dokan)
ECHO		G2) Mario Circuit road gfx (circuit)		G15) Race time font + Item icon sprites (abc)
ECHO		G3) Bowser Castle road gfx (castle)		G16) Cheep-Cheep sprite (pukupuku)	
ECHO		G4) Dust cloud sprite (dust)			G17) Squashed driver sprites (perapera)
ECHO		G5) Choco Island road gfx (dart)		G18) Driver face and little position number sprites (mark)
ECHO		G6) Ghost Pillar sprite (pole)			G19) Many font and a few icon gfx (moji-e)
ECHO		G7) Monty Mole sprite (mogura)			G20) Common road gfx (item)
ECHO		G8) Water/mud, grass effect etc. (water)	G21) Item sprites (item)
ECHO		G9) Winner Flag sprite(checker)			G22) Rainbow Road road gfx (star)
ECHO		G10) Battle Mode Balloon sprite (ball)		G23) Donut Plains road gfx (grass)	
ECHO		G11) Thwomp sprite (dossun)			G24) Koopa Beach road gfx (sand)
ECHO		G12) Vanilla Lake road gfx (ice)		G25) Chain Chomp sprite (killer)
ECHO		G13) Piranha Plant sprite (pakkun)		G26) Ghost Valley road gfx (obake)
ECHO.
ECHO Enter value at the main menu to compress the graphic.
ECHO.
Pause
GOTO MENU

:PalletMenu
cls
ECHO.
ECHO Pallets menu values:
ECHO.
ECHO	P1) Credits palette (ending)
ECHO	P2) Mario Circuit palette (ending)
ECHO	P3) Ghost Valley palette (ending)
ECHO	P4) Donut Plains palette (ending)
ECHO	P5) Bowser Castle palette (ending)
ECHO	P6) Vanilla Lake palette (ending)
ECHO	P7) Choco Island palette (ending)
ECHO	P8) Koopa Beach palette (ending)
ECHO	P9) Rainbow Road palette (ending)
ECHO.
ECHO Enter value at the main menu to compress the pallet.
ECHO. 
pause
GOTO MENU

:OtherMenu
cls
ECHO.
ECHO Other menu values:
ECHO.
ECHO 	O1) Tile types / behaviors for each theme (bg-data)
ECHO 	O2) Tan values for the AI to workout turning angle (tan-data)
ECHO.
ECHO Enter value at the main menu to compress the data.
ECHO. 
pause
GOTO MENU

:BackgroundsMenu
cls
ECHO.
ECHO Backgrounds menu values:
ECHO.
ECHO 	B1) Mario Circuit background graphics (circuit)
ECHO 	B2) Mario Circuit background layout (circuit)
ECHO 	B3) Ghost Valley background graphics (obake)
ECHO 	B4) Ghost Valley background layout (obake)
ECHO 	B5) Donut Plains background graphics (grass)
ECHO 	B6) Donut Plains  background layout (grass)
ECHO 	B7) Bowser Castle background graphics (castle)
ECHO 	B8) Bowser Castle background layout (castle)
ECHO 	B9) Vanilla Lake background graphics (ice)
ECHO 	B10) Vanilla Lake background layout (ice)
ECHO 	B11) Choco Island background graphics (dart)
ECHO 	B12) Choco Island background layout (dart)
ECHO 	B13) Koopa Beach background graphics (sand)
ECHO 	B14) Koopa Beach background layout (sand)
ECHO 	B15) Rainbow Road background graphics (star)
ECHO 	B16) Rainbow Road background layout (star)
ECHO.
ECHO Enter value at the main menu to compress the data.
ECHO. 
pause
GOTO MENU

:MusicMenu
cls
ECHO.
ECHO Music menu values:
ECHO.
ECHO	M1) Koopa Beach music (sand)
ECHO	M2) Bowser Castle music (castle)
ECHO	M3) Choco Island music (dart)
ECHO	M4) Title music	(title)
ECHO	M5) Rainbow Road music (star)
ECHO	M6) Credits music (ending)
ECHO	M7) Podium no cup music, below 3rd (final02)
ECHO	M8) Ghost Valley music (obake)
ECHO	M9) Podium ceremony music (final01)
ECHO	M10) Donut Plains music (grass)
ECHO	M11) Menu music (select)
ECHO	M12) Mario Circuit music (circuit)
ECHO	M13) Battle Mode music (battle)
ECHO	M14) Vanilla Lake (ice)
ECHO.
ECHO Enter value at the main menu to compress the music.
ECHO.
pause
GOTO MENU

:CompressAll
CALL CompressAllCommand
GOTO MENU

:CompressAllCommand
call :TrackCompress sand01 ".\source\assets\mode7\scr\sand\" scr
call :TrackCompress star01 ".\source\assets\mode7\scr\star\" scr
call :TrackCompress circuit01 ".\source\assets\mode7\scr\circuit\" scr
call :TrackCompress circuit02 ".\source\assets\mode7\scr\circuit\" scr
call :TrackCompress circuit03 ".\source\assets\mode7\scr\circuit\" scr
call :TrackCompress obake02 ".\source\assets\mode7\scr\obake\" scr
call :TrackCompress grass01 ".\source\assets\mode7\scr\grass\" scr
call :TrackCompress ice01 ".\source\assets\mode7\scr\ice\" scr
call :TrackCompress dart02 ".\source\assets\mode7\scr\dart\" scr
call :TrackCompress sand02 ".\source\assets\mode7\scr\sand\" scr
call :TrackCompress battle06 ".\source\assets\mode7\scr\battle\" scr
call :TrackCompress obake03 ".\source\assets\mode7\scr\obake\" scr
call :TrackCompress grass02 ".\source\assets\mode7\scr\grass\" scr
call :TrackCompress grass03 ".\source\assets\mode7\scr\grass\" scr
call :TrackCompress castle03 ".\source\assets\mode7\scr\castle\" scr
call :TrackCompress castle01 ".\source\assets\mode7\scr\castle\" scr
call :TrackCompress castle02 ".\source\assets\mode7\scr\castle\" scr
call :TrackCompress obake01 ".\source\assets\mode7\scr\obake\" scr
call :TrackCompress battle03 ".\source\assets\mode7\scr\battle\" scr
call :TrackCompress battle02 ".\source\assets\mode7\scr\battle\" scr
call :TrackCompress battle05 ".\source\assets\mode7\scr\battle\" scr
call :TrackCompress ice02 ".\source\assets\mode7\scr\ice\" scr
call :TrackCompress circuit04 ".\source\assets\mode7\scr\circuit\" scr
call :TrackCompress dart03 ".\source\assets\mode7\scr\dart\" scr
call :compress lost ".\source\assets\obj\others\" cgx
call :compress circuit ".\source\assets\mode7\chr\" cm7
call :compress castle ".\source\assets\mode7\chr\" cm7
call :compress sand  ".\source\assets\obj\others\" cgx
call :compress dart ".\source\assets\mode7\chr\" cm7
call :compress pole ".\source\assets\obj\others\" cgx
call :compress mogura ".\source\assets\obj\others\" cgx
call :compress water ".\source\assets\obj\others\" cgx
call :compress checker ".\source\assets\obj\others\" cgx
call :compress ball ".\source\assets\obj\others\" cgx
call :compress dossun ".\source\assets\obj\others\" cgx
call :compress ice ".\source\assets\mode7\chr\" cm7
call :compress pakkun ".\source\assets\obj\others\" cgx
call :compress dokan ".\source\assets\obj\others\" cgx
call :compress abc ".\source\assets\back\chr\" cgx
call :compress pukupuku ".\source\assets\obj\others\" cgx
call :compress perapera ".\source\assets\obj\others\" cgx
call :compress mark ".\source\assets\obj\others\" cgx
call :compress moji-e ".\source\assets\back\chr\" cgx
call :compress item ".\source\assets\mode7\chr\" cm7
call :compress item ".\source\assets\obj\others\" cgx
call :compress star ".\source\assets\mode7\chr\" cm7
call :compress grass ".\source\assets\mode7\chr\" cm7
call :compress sand ".\source\assets\mode7\chr\" cm7
call :compress killer ".\source\assets\obj\others\" cgx
call :compress obake ".\source\assets\mode7\chr\" cm7
call :compress sand ".\source\assets\sound\" music
call :compress castle ".\source\assets\sound\" music
call :compress dart ".\source\assets\sound\" music
call :compress title ".\source\assets\sound\" music
call :compress star ".\source\assets\sound\" music
call :compress ending ".\source\assets\sound\" music
call :compress final02 ".\source\assets\sound\" music
call :compress obake ".\source\assets\sound\" music
call :compress final01 ".\source\assets\sound\" music
call :compress grass ".\source\assets\sound\" music
call :compress select ".\source\assets\sound\" music
call :compress circuit ".\source\assets\sound\" music
call :compress battle ".\source\assets\sound\" music
call :compress ice ".\source\assets\sound\" music
call :compress circuit ".\source\assets\back\chr\" cgx
call :compress circuit ".\source\assets\back\scr\" scr
call :compress obake ".\source\assets\back\chr\" cgx
call :compress obake ".\source\assets\back\scr\" scr
call :compress grass ".\source\assets\back\chr\" cgx
call :compress grass ".\source\assets\back\scr\" scr
call :compress castle ".\source\assets\back\chr\" cgx
call :compress castle ".\source\assets\back\scr\" scr
call :compress ice ".\source\assets\back\chr\" cgx
call :compress ice ".\source\assets\back\scr\" scr
call :compress dart ".\source\assets\back\chr\" cgx
call :compress dart ".\source\assets\back\scr\" scr
call :compress sand ".\source\assets\back\chr\" cgx
call :compress sand ".\source\assets\back\scr\" scr
call :compress star ".\source\assets\back\chr\" cgx
call :compress star ".\source\assets\back\scr\" scr
call :compress bg-data ".\source\assets\bin\" bin
call :compress tan-data ".\source\assets\bin\" bin
call :compress ending ".\source\assets\color\" col
call :compress circuit ".\source\assets\color\" col
call :compress obake ".\source\assets\color\" col
call :compress grass ".\source\assets\color\" col
call :compress castle ".\source\assets\color\" col
call :compress ice ".\source\assets\color\" col
call :compress dart ".\source\assets\color\" col
call :compress sand ".\source\assets\color\" col
call :compress star ".\source\assets\color\" col
exit /b

:BuildAllDAT
call :BuildAllDATFunction
GOTO MENU


:BuildAllDATFunction
REM Copying BuildDAT tool to source dir to run for relative file paths
REM copy %ToolsPath%%DATpath%%buildDAT% ".\source\assets\rom\" /y .\..\..\DAT\
cls
cd ".\source\assets\rom\"
prompt Running Command: 
@echo off
.\..\..\..\%ToolsPath%%DATpath%%buildDAT% %ROM1% %DAT1%
.\..\..\..\%ToolsPath%%DATpath%%buildDAT% %ROM2% %DAT2%
.\..\..\..\%ToolsPath%%DATpath%%buildDAT% %ROM3% %DAT3%
.\..\..\..\%ToolsPath%%DATpath%%buildDAT% %ROM4% %DAT4%

cd %~dp0
prompt
exit /b



:BuildAllDataPacks
call :J-S-C
call :select-e
call :final-e
call :title-e
GOTO MENU

:BuildPack
REM %1 rom file %2 dir path  %3 output file %4 buffer size
cls
cd %2
REM prompt Running Command: 
"%~dp0"%ToolsPath%%DATpath%%buildDAT% %1 %3 %4
cd %~dp0
prompt
exit /b


:TrackCompress
cls
copy %ToolsPath%%comppath%%compress% %2 /y

cd %2
cls
prompt Running Command: 
%compress% %1.%3 %1.sss -compress -double -overwrite %WAIT%
@echo Compressed %1
del %compress%
cd %~dp0

exit /b

:Compress
REM Args 1 filename 2 path 3 return path 4 file extention
cls
copy %ToolsPath%%comppath%%compress% %2 /y

cd %2
cls
prompt Running Command: 
%compress% %1.%3 %1.cpr -compress -overwrite %WAIT%
@echo Compressed %1
del %compress%
cd %~dp0
prompt
exit /b

:compile_all
cls
CD %CompilerPath%
call createROM.bat DO_ALL %DEBUG_TOGGLE%
cd %~dp0
exit /b

:compile_code
cls
CD %CompilerPath%
call createROM.bat ASSEMBLE_ONLY %DEBUG_TOGGLE%
cd %~dp0
exit /b

:compile_assets
cls
CD %CompilerPath%
call createROM.bat ASSETS_ONLY %DEBUG_TOGGLE%
cd %~dp0
exit /b

:toggle_debug
cls
IF "%DEBUG_TOGGLE%"=="DEBUG_OFF" (
	SET DEBUG_TOGGLE=DEBUG_ON
) ELSE (
	SET DEBUG_TOGGLE=DEBUG_OFF
)
cd %~dp0
exit /b

:toggle_wait
cls
IF "%WAIT%"=="-wait" (
	SET WAIT=
) ELSE (
	SET WAIT=-wait
)
cd %~dp0
exit /b

:load

IF EXIST %game% (%game%) ELSE (ECHO %game% not found.  Compile first & pause)
GOTO :MENU



:clean_up

call :delete_file %ToolsPath%\as65c\fhist.ahist
call :delete_file %ToolsPath%\as65c\*.map
call :delete_file %ToolsPath%\as65c\*.hex

call :delete_file_recursive .\Source\*.rel
call :delete_file_recursive .\Source\*.lis
call :delete_file .\Output\*.rom
call :delete_file .\Output\*.sfc
	
cd %~dp0

exit /b


:full_clean_up

call :clean_up

call :delete_subdirs .\Source\Assets
call :delete_subdirs .\Source\kimura
call :delete_file .\Source\DAT\*.DAT
call :delete_file .\Setup\setup


cd %~dp0
cls
echo CLEANED SETUP DATA. EXITING.
pause
exit

exit /b


:delete_file
IF EXIST %1 del %1
exit /b

:delete_file_recursive
del /S /Q %1 2>NUL
exit /b

:delete_subdirs
cd %1
for /D %%p in (*) do rmdir /S /Q %%p
cd %~dp0
exit /b

:Exit
cls