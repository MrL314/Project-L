
@echo  OFF



rem Do not change these unless you know what you are doing.

set FUNC=%~1
set DEBUG_ENABLE=%~2

set source_dir="../../Source"
set hex-output=out
set code-output="../../Output/CODE_ONLY.rom"
set ROM-OUTPUT="../../Output/Super Mario Kart (U).sfc"

rem set exe_dir="single_exe/"
set exe_dir="dist/"

set asm=%exe_dir%as65c
set lnk=%exe_dir%link
set h2b=%exe_dir%hex2bin
set addromdata=%exe_dir%addROMdata


set kimura=%source_dir%"/kimura"
set kart=%kimura%"/kart"
set mak=%kart%"/mak"
set join=%kart%"/join"
set sfxdos=%kart%"/sfxdos"




rem SET YOUR ASM FILES TO ASSEMBLE HERE:

set ASM_FILES=^
 %mak%/kart-main.asm^
 %mak%/kart-init-e.asm^
 %mak%/kart-bg.asm^
 %mak%/kart-ppu.asm^
 %mak%/kart-apu.asm^
 %mak%/kart-calc.asm^
 %mak%/kart-data.asm^
 %mak%/kart-drive.asm^
 %mak%/kart-pers.asm^
 %mak%/kart-enemy.asm^
 %mak%/kart-effect.asm^
 %join%/kart-obj.asm^
 %join%/Object.asm^
 %join%/System.asm^
 %join%/Screen.asm^
 %join%/Scene.asm^
 %join%/Car.asm^
 %join%/Pole.asm^
 %join%/Missile.asm^
 %join%/Sub_sound.asm^
 %join%/Effect.asm^
 %join%/Debug.asm^
 %join%/Shadow.asm^
 %join%/Hit.asm^
 %join%/Item.asm^
 %join%/BGmove.asm^
 %join%/Pause.asm^
 %join%/Over.asm^
 %join%/Net.asm^
 %join%/ISPK-7E.asm^
 %join%/ISPK-7F.asm^
 %join%/Compress.asm^
 %join%/BGcheck.asm^
 %join%/Jugem.asm^
 %join%/Poo.asm^
 %join%/Doppler.asm^
 %join%/Meter.asm^
 %join%/Round.asm^
 %join%/Record.asm^
 %join%/Move.asm^
 %join%/Battle.asm^
 %join%/Window.asm^
 %join%/BGunit_set.asm^
 %join%/Coin.asm^
 %join%/title-e.asm^
 %join%/c-select-e.asm^
 %join%/k-select.asm^
 %join%/w-select-e.asm^
 %join%/demo.asm^
 %join%/Result.asm^
 %join%/Final-e.asm^
 %join%/Driver-point-e.asm^
 %join%/record-e.asm^
 %join%/edit_1.asm^
 %join%/edit_2.asm^
 %join%/edit_3.asm^
 %join%/ed_dos1.asm^
 %join%/ed_dos2.asm^
 %join%/edit_data.asm^
 %join%/mapedit.asm^
 %join%/runed.asm^
 %join%/runed1.asm^
 %join%/runed2.asm^
 %join%/maped3.asm^
 %join%/maped4.asm^
 %join%/edmap2.asm^
 %join%/Ending1-e.asm^
 %join%/Ending2-e.asm^
 %join%/rundat.asm^
 %join%/Camera.asm^
 %sfxdos%/fdcdrv.asm^
 %sfxdos%/fileio.asm^
 %sfxdos%/ppidrv.asm^
 %sfxdos%/sccdrv.asm^
 %sfxdos%/condrv.asm^
 %sfxdos%/ascii.asm^
 %sfxdos%/sfxdos.asm^


rem   when adding new asm files, make sure to put them directly below the current list, start the line with a space, and end the line with ^
rem   otherwise the batch file will not properly understand the format



rem Change the values here to set section offsets for debug build code
set SFXDOS_OFFSET=09c000
set editer_OFFSET=088000





rem DO NOT CHANGE ANYTHING BETWEEN THESE LINES
rem ====================================================================
if "%DEBUG_ENABLE%"=="" set DEBUG_ENABLE=DEBUG_ON

set debug_mode_build_var=1

if "%DEBUG_ENABLE%"=="DEBUG_OFF" (
	set SFXDOS_OFFSET=0
	set editer_OFFSET=0
	set debug_mode_build_var=0
)
rem ====================================================================





rem Set assembly pre-defined variables (usually for version control)
set asm-vars=-dENG_VER=1 -dJAP_VER=0 -ddebug_mode=%debug_mode_build_var%



rem Set code section starting offsets
set RELINFO=^
prog=0ff70,^
bank80=808000,^
objprog=80b900,^
objdata=818000,^
objinit=85dc00,^
bank81=81e000,^
bank83=83f000,^
bank84=84d500,^
bank85=858000,^
SFXDOS=%SFXDOS_OFFSET%,^
editer=%editer_OFFSET%,^
comn=0,^
,
rem   when adding new sections, make sure to put them ABOVE the comma on the previous line, and end the line with ,^
rem   otherwise the batch file will not properly read the new data




rem Set asset inclusion instructions here!
rem FORMAT is  <file> <source offset> <destination offset> <tranfser size>

rem these are the assets that will always be included
set ASSET_INSTRUCTIONS=^
 %source_dir%/DAT/rom1-e.DAT 0x010000 0x28000 0x8000,^
 %source_dir%/DAT/rom1-e.DAT 0x018000 0x38000 0x7000,^
 %source_dir%/DAT/rom2-e.DAT 0x000000 0x48000 0x5500,^
 %source_dir%/DAT/rom2-e.DAT 0x010000 0x68000 0x8000,^
 %source_dir%/DAT/rom2-e.DAT 0x018000 0x78000 0x8000,^
 %source_dir%/DAT/rom3-e.DAT 0x000000 0x00000 0x8000,^
 %source_dir%/DAT/rom3-e.DAT 0x008000 0x10000 0x8000,^
 %source_dir%/DAT/rom3-e.DAT 0x010000 0x20000 0x8000,^
 %source_dir%/DAT/rom3-e.DAT 0x018000 0x30000 0x8000,^
 %source_dir%/DAT/rom4-e.DAT 0x000000 0x40000 0x8000,^
 %source_dir%/DAT/rom4-e.DAT 0x008000 0x50000 0x8000,^
 %source_dir%/DAT/rom4-e.DAT 0x010000 0x60000 0x8000,^
 %source_dir%/DAT/rom4-e.DAT 0x018000 0x70000 0x8000,^
 %kimura%/bin/OAM_data.bin 0x000000 0x5ee00 0x1200,^
 %kimura%/bin/BG_unit.bin 0x000000 0x5d000 0x0c00,^
 %kimura%/bin/windeco1.bin 0x000000 0x5e770 0x0690,^
 %kimura%/bin/pole_data.bin 0x000000 0x5c800 0x0800,^
 ,
rem   when adding new assets, make sure to put them ABOVE the comma on the previous line, and end the line with ,^
rem   otherwise the batch file will not properly read the new data
rem   also make sure that the end of the line does not have a space, AND that the beginning has exactly one space


rem these are the assets that will only be included if building the debug version
set DEBUG_ASSET_INSTRUCTIONS=^
 %kimura%/bin/editchar.bin 0x000000 0x99000 0x2800,^
 ,
rem   when adding new assets, make sure to put them ABOVE the comma on the previous line, and end the line with ,^
rem   otherwise the batch file will not properly read the new data
rem   also make sure that the end of the line does not have a space, AND that the beginning has exactly one space

















rem   DO NOT MODIFY ANYTHING BELOW THIS LINE
rem ====================================================

rem if "%FUNC%"=="" set FUNC=DO_ALL
if "%FUNC%"=="" set FUNC=ASSETS_ONLY

call :%FUNC%
goto :exit


:DO_ALL
	call :ASSEMBLE_MAIN
	call :ADD_ASSETS
exit /b


:ASSEMBLE_ONLY
	call :ASSEMBLE_MAIN
exit /b

:ASSETS_ONLY
	call :ADD_ASSETS
exit /b






:ASSEMBLE_MAIN
	rem Assemble all files

	ECHO Assembling .asm files into .rel files!

	set LINK_FILES=
	set t=%ASM_FILES%
	:asmfileloop
		set curr_f=""
		for /f "tokens=1* delims= " %%a in ("%t%") do set curr_f=%%a&set t=%%b
		set curr_f=%curr_f:"=%
		call :clean_end %curr_f%
		for %%f in (%curr_f%) do (
			call :assemble %cleaned%%%~nf.asm
			set LINK_FILES=%LINK_FILES%%cleaned%%%~nf.rel &rem
		)
		if defined t goto :asmfileloop


	rem wait for multi-core assembly to finish
	call :asm_wait_loop

	ECHO Assembled .asm files!

	ECHO.











	ECHO Linking .rel files into a single ROM


	%lnk% %LINK_FILES% -r %RELINFO% -o %hex-output%.hex -ls %hex-output%.map

	ECHO Linked files into a single ROM!



	ECHO Converting Hex File

	%h2b% -cff -f%hex-output%.hex -o%code-output%


	ECHO.

	ECHO Created %code-output%!

	ECHO.

exit /b



:ADD_ASSETS
	ECHO Adding asset data

	break > "temp.txt"

	call :add_asset_list "%ASSET_INSTRUCTIONS:"=%"
	if "%DEBUG_ENABLE%"=="DEBUG_ON" (
		call :add_asset_list "%DEBUG_ASSET_INSTRUCTIONS:"=%"
	)

	%addromdata% %code-output% "temp.txt" %ROM-OUTPUT%

	del "temp.txt"

	ECHO Asset data added

	ECHO.

	ECHO Created .sfc at %ROM-OUTPUT%!
exit /b


:add_asset_list
	set t=%~1
	:asset_loop
	set curr_asset=
	for /f "tokens=1* delims=," %%a in ("%t%") do set curr_asset=%%a&set t=%%b
	if not defined t goto :asset_break
	if not defined curr_asset goto :asset_loop
	set curr_f=
	set curr_soff=
	set curr_doff=
	set curr_size=
	for /f "tokens=1,2,3,4* delims= " %%a in ("%curr_asset%") do (
		set curr_f=%%a
		set curr_soff=%%b
		set curr_doff=%%c
		set curr_size=%%d
	)

	if defined curr_f if defined curr_soff if defined curr_doff if defined curr_size (
		echo %curr_f%, %curr_soff%, %curr_doff%, %curr_size% >> "temp.txt"
		goto :good_add
	)
	rem bad add:
	echo [ERROR] Error parsing
	echo    %curr_asset%

	:good_add

	if defined t goto :asset_loop
	:asset_break
exit /b



:force_assemble
	%asm% %1 %asm-vars% -f
exit /b

:assemble
	start "asmble" /b %asm% %1 %asm-vars%
exit /b


:clean_end
	set str=%1
	set cleaned=
	:cleanloop
	for /f "tokens=1*delims=/" %%a in ("%str%") do (
		set new=%%a
		set str=%%b
	)
	if defined str (
		set cleaned=%cleaned%%new%/
		goto :cleanloop
	)
exit /b


:checkinstances
	rem check how many instances of as65c.exe are running
	rem this is used to speed up assembly time by a TON!
	for /f "usebackq tokens=1,*" %%t in (`tasklist ^| find /I /C "as65c.exe"`) do set INSTANCES=%%t
exit /b

:asm_wait_loop
	call :checkinstances
	
	if %INSTANCES% EQU 0 goto :exit_asm_wait

	goto :asm_wait_loop
	:exit_asm_wait
exit /b




:exit
pause