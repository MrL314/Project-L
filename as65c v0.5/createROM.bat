
@echo  OFF

set asm-vars=--options ENG_VER 1 JAP_VER 0 debug_mode 1

set linker-input="linked rel files.txt"
set linker-options="rel options.txt"
set linker-output="../LINKED_OUTPUT.rom"
set ROM-SIZE=1024

set asset-instructions="ROM files.txt"
set ROM-OUTPUT="../final output.sfc"


set asm="dist/assembler/assembler.exe"



ECHO Assembling .asm files into .rel files!

break>SYMBOLS.txt



rem Assemble all files



rem PUT FILES TO ASSEMBLE HERE:
rem format as "%asm% <file_directory> %asm-vars%"


%asm% ../kimura/kart/mak/kart-main.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-init-e.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-bg.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-ppu.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-apu.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-calc.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-data.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-drive.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-pers.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-enemy.asm %asm-vars%
%asm% ../kimura/kart/mak/kart-effect.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/kart-obj.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Object.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/System.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Screen.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Scene.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Car.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Pole.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Missile.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Sub_sound.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Effect.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Debug.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Shadow.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Hit.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Item.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/BGmove.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Pause.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Over.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Net.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/ISPK-7E.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/ISPK-7F.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Compress.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/BGcheck.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Jugem.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Poo.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Doppler.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Meter.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Round.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Record.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Move.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Battle.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Window.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/BGunit_set.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Coin.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/title-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/c-select-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/k-select.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/w-select-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/demo.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Result.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Final-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Driver-point-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/record-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/edit_1.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/edit_2.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/edit_3.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/ed_dos1.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/ed_dos2.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/edit_data.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/mapedit.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/runed.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/runed1.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/runed2.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/maped3.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/maped4.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/edmap2.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Ending1-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Ending2-e.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/rundat.asm %asm-vars%
%asm% ../kimura/kart/mak/../join/Camera.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/fdcdrv.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/fileio.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/ppidrv.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/sccdrv.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/condrv.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/ascii.asm %asm-vars%
%asm% ../kimura/kart/mak/../sfxdos/sfxdos.asm %asm-vars%








ECHO Assembled .asm files!

ECHO.

ECHO Linking .rel files into a single ROM





linker.exe %linker-input% %linker-options% %linker-output% --rom_size %ROM-SIZE%

ECHO Linked files into a single ROM!

ECHO.

ECHO Adding asset data

addROMdata.exe %linker-output% %asset-instructions% %ROM-OUTPUT%

ECHO Asset data added

ECHO.

ECHO Created .sfc at %ROM-OUTPUT%!

PAUSE