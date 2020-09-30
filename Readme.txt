######################################
#  PROJECT L  by MrL314 and Dirtbag  #
######################################
version 0.5: Sep. 29, 2020


QUICK DOWNLOAD: >>> https://github.com/MrL314/Project-L/archive/master.zip


Contact MrL314: 
	email: LFmisterL314@gmail.com
	discord: MrL314#8106
	Patreon: https://www.patreon.com/MrL314 (see "Final notes")

Contact Dirtbag:
	discord: Dirtbag#3153

Special thanks to:
	MrL314
	Dirtbag
	SmorBjorn
	xprism
	Everyone in the SMK Workshop community!!
	and YOU!


For the open-source code, you may find the github here: https://github.com/MrL314/Project-L


Disclaimer
----------
This program set of scripts and programs is provided free of charge and without warranty.
It is not to be distributed with any additional files, these must be provided by the user at their own risk.


Intro to Project L: By MrL314
-----------------------------
So you're looking to assemble an SNES game? Well you've come to the right place.
PROJECT L is a general purpose assembler and linker for SNES games. The main 
project in mind was to be able to assemble Super Mario Kart directly from the
source files, however we have plans to make this project more general purpose in
the future!

This project is in no way affiliated with Nintendo. We have no connections to Nintendo,
so this entire project is a third party SDK for the SNES. As such, we expect most of you
to be coming here for assembling Super Mario Kart. Instructions to build SMK are given 
below. However, because this is completely third party, extra efforts have been taken
in order to ensure none of Nintendo's IP are used directly in the project. Since
a few files were indeed missing regarding SMK's source code, one of the files had to be
built from scratch, meaning we had to find another way around to both create that file
and keep Nintendo's data out of the program. You will see this later. For now, let's build
a Super Mario Kart English ROM!

  Happy karting, 
      -MrL314 


----------------------
How to use: By Dirtbag
----------------------

Pre-requisite: .NET frame work

Setup
-----

Before you can run this toolset you need to run the setup script. The setup process is automated, 
but some files are required that you will need to supply yourself before you run setup.bat.

1) .NET framework. The DATBuilder tool writen for this is in .NET, and to run requres the .NET 
   framework to be installed on your PC

2) The following folders under \setup\ need to be populated

	\setup\risc\ with the contents of \NEWS_05\NEWS_05\home\kimura\kart\risc.lzh
	\setup\CAR\ with the contents of \NEWS_04\home\sugiyama\CAR
	\setup\data\ with the contents of \NEWS_05\NEWS_05\home\kimura\kart\data.lzh
	\setup\mak\ with the contents of \NEWS_05\NEWS_05\home\kimura\kart\mak.lzh

3) You will also need to place a copy of the release ROM in the root of \setup\
The ROM must be named: Super Mario Kart (USA).sfc
and it must be an unheadered ROM (512KB not 513KB)

Once you have done this run the SETUP.BAT file in the SETUP directory.  
During the running of SETUP.BAT, you will encounter a prompt to enter a key. This is to ensure
that no real code from Nintendo is directly included in our project. We unfortunately cannot provide
the key for you flat-out, but the key is simple:

	It is the name of this project, with the space in between, in all caps.

If run successfully you will be able to run the build.bat file.



-----------------------------------
| Why do I need to provide a ROM? |
-----------------------------------

Some of the source files are larger than what is taken and placed into the build ROM image.  The original 
compression tool used would have taken a start and end offset parameter.  The compression tool we are using 
compresses the whole file.  Therefore, it was easier to extract some of the assets from the Release ROM at 
the correct size.  It also means that when you edit those files, you are staying withing the size limit of 
what is used.





Quick Guide
-----------

Edit the code and/or assets that you want to change.  A full list of files is listed below. (See: File List)
	
Assets (Compress files) -> Packs (Build Packs) -> DAT (Build DATs) -> ROM (Compile ROM) -> Play ROM!

The output ROM will be in the folder \Output\

----------
## Tip ##:
----------
When compressing all, double tap Enter when it says "press any key to continue".  This will auto press any key 
for the rest of the prompts.  At some point, we plan to swap out the compression tool to the one in EE, and 
make it stand-alone tool.





Compressed Assets
-----------------

Some assets are compressed within the ROM file to save space, and are decompressed in real time when playing the game.
Not all items are compressed, such as the drivers sprites, but other items -- such as the music -- are. Track layouts are
double compressed.

If you have only edited one asset, then you will only need to compress that one item. Via the menu system, you can find the
option to compress just the one item.  If an item needs to be double compressed, the menu system will deal with that.

For example, if you are editing the tiles and layout for Rainbow Road, from the main menu you can enter B to see the
background menu options.  The graphics for rainbow road are B15 and the layout is B16.  Press Enter to return to the
main menu, then enter B15 to compress the tiles for Rainbow Road, and B16 to compress the layout for Rainbow Road.




Building Data Packs
--------------------

Data packs are self contained archives that are made up of multiple files.

title-e.bin  = Title screen
select-e.bin = Player and cup select screens
final-e.bin  = Podium screen
j-s-c.bin    = Lakitu ("Jugem"), shadows and coins graphic are combined into one

For example, the title screen is a double compressed file that is made up of graphic tiles, colour palettes & layout files

title.sss
	title-j.bin (title-j.bin)
		\Source Files\final\title-j.ROM
			title.CGX       $0000 $2000 $0000
			title1.SCR      $0000 $0800 $2000
			title2-j.SCR    $0000 $1000 $2800
			d-point-j.SCR   $0000 $0800 $3800
			title.COL       $0000 $0200 $4000
			d-point.COL     $0000 $0200 #4200

So to update the graphic tiles for the title screen you'd need to edit title.CGX, then rebuild the data pack.




DAT files
---------
DAT files contain all of the assets needed for the game.  If you make any changes you will need to rebuild the DAT files
and then recompile the ROM.




Changing DAT files (Advanced users only)
--------------------------------------
**WARNING DO NOT CHANGE THESE FILES UNLESS YOU KNOW WHAT YOU ARE DOING**

\Source\Assets\rom\ROM1-e.txt
\Source\Assets\rom\ROM2-e.txt
\Source\Assets\rom\ROM3-e.txt
\Source\Assets\rom\ROM4-e.txt

These files contain the source filename and path as well as the data addresses of where to take from and place in the DAT
file.  The DAT files are then used to build a final ROM.



File types extensions
---------------------
SCR = Tile Layout
CGX = Graphics
COL = Colour Pallet
SSS = Double Compressed
CPR = Lower case file extention  = Compressed
BIN = Data 
DAT = Binary file with the contents of other assets
ROM = File Data to build a DAT file

Note: a lower case file extention also represents a compressed file.
e.g. sand.CGX would be the uncompressed, while sand.cgx is the compressed version.



File List
---------
../sound/se.bin                     # Instrument table, driver tunes, NSPC code, samples 0 - 19
../mode7/scr/sand/sand01.sss        # Koopa Beach 2 track layout
../mode7/scr/star/star01.sss        # Rainbow Road track layout          
../obj/kart/luigi.CGX               # Luigi driver sprite
../obj/others/nintendo.CGX          # Top row of Nintendo Logo
../obj/others/nintendo.CGX          # Bottom row of Nintendo Logo
../sound/sand.cpr                   # Koopa Beach music
../sound/castle.cpr                 # Bowser Castle music
../sound/dart.cpr                   # Choco Island music
../obj/others/lost.cpr              # Loser disappearance cloud sprite
../mode7/chr/circuit.cpr            # Mario Circuit road gfx (4bpp rev)
../mode7/chr/castle.cpr             # Bowser Castle road gfx (4bpp rev)
../sound/title.cpr                  # Title music                    
../obj/others/sand.cpr              # Dust cloud sprite
../bin/demo_kinopio.bin             # Demo recorded input Toad
../bin/demo_peach.bin               # Demo recorded input Princess
../mode7/scr/circuit/circuit01.sss  # Mario Circuit 3 track data
../mode7/scr/circuit/circuit02.sss  # Mario Circuit 1 track data
../mode7/scr/circuit/circuit03.sss  # Mario Circuit 4 track data
../mode7/scr/obake/obake02.sss      # Ghost Valley 3 track data
../mode7/scr/grass/grass01.sss      # Donut Plains 2 track data
../mode7/scr/ice/ice01.sss          # Vanilla Lake 2 track data
../mode7/scr/dart/dart02.sss        # Choco Island 2 track data
../mode7/scr/sand/sand02.sss        # Koopa Beach 1 track data
../mode7/scr/battle/battle06.sss    # Battle Course 1 track data
../mode7/scr/obake/obake03.sss      # Ghost Valley 1 track data
../sound/star.cpr                   # Rainbow Road music
../mode7/chr/dart.cpr               # Choco Island road gfx (4bpp rev)
../mode7/scr/grass/grass02.sss      # Donut Plains 3 track data
../mode7/scr/grass/grass03.sss      # Donut Plains 1 track data
../mode7/scr/castle/castle03.sss    # Bowser Castle 1 track data
../mode7/scr/castle/castle01.sss    # Bowser Castle 2 track data
../mode7/scr/castle/castle02.sss    # Bowser Castle 3 track data
../mode7/scr/obake/obake01.sss      # Ghost Valley 2 track data
../mode7/scr/battle/battle03.sss    # Battle Course 4 track data
../sound/ending.cpr                 # Credits music
../sound/final02.cpr                # Podium no cup music (when below 3rd place)
../bin/bg-data.cpr                  # Tile types and behaviors for each theme
../bin/demo_mario.bin               # Demo 1 recorded inputs for Mario
../obj/kart/mario.CGX               # Mario driver sprite
../obj/kart/koopa.CGX               # Bowser driver sprite
../obj/kart/peach.CGX               # Princess driver sprite
../obj/kart/cong.CGX                # DK Jr. driver sprite
../obj/others/pole.cpr              # Ghost Pillar sprite
../sound/obake.cpr                  # Ghost Valley music
../obj/others/mogura.cpr            # Monty Mole sprite
../obj/others/water.cpr             # Water/mud, grass effect and impact sprites
../obj/others/checker.cpr           # Winner Flag sprite
../obj/others/ball.cpr              # Battle Mode Balloon sprite
../obj/others/dossun.cpr            # Thwomp sprite
../back/chr/star.cpr                # Rainbow Road background gfx (2bpp)
../mode7/chr/ice.cpr                # Vanilla Lake road gfx (4bpp rev)
../bin/demo_yossy.bin               # Demo recorded inputs (1 - Yoshi)
../obj/others/j-s-c.bin             # Lakitu, shadow, coin and sparks sprites
../obj/others/pakkun.cpr            # Piranha Plant sprite
../obj/others/dokan.cpr             # Pipe sprite
../back/chr/abc.cpr                 # Race time font + Item icon sprites (2bpp)
../obj/others/pukupuku.cpr          # Cheep-Cheep sprite
../obj/others/perapera.cpr          # Squashed driver sprites
../back/chr/circuit.cpr             # Mario Circuit Track background graphics (2bpp)
../back/chr/obake.cpr               # Ghost Valley Track background graphics (2bpp)
../back/chr/grass.cpr               # Donut Plains Track background graphics (2bpp)
../back/chr/castle.cpr              # Bowser Castle Track background graphics (2bpp)
../back/chr/ice.cpr                 # Vanilla Lake Track background graphics (2bpp)
../back/chr/dart.cpr                # Choco Island Track background graphics (2bpp)
../back/chr/sand.cpr                # Koopa Beach Track background graphics (2bpp)
../back/scr/circuit.cpr             # Mario Circuit Track background layout (2bpp)
../back/scr/obake.cpr               # Ghost Valley Track background layout (2bpp)
../back/scr/grass.cpr               # Donut Plains Track background layout (2bpp)
../back/scr/castle.cpr              # Bowser Castle Track background layout (2bpp)
../back/scr/ice.cpr                 # Vanilla Lake Track background layout (2bpp)
../back/scr/dart.cpr                # Choco Island Track background layout (2bpp)
../back/scr/sand.cpr                # Koopa Beach Track background layout (2bpp)
../mode7/scr/battle/battle02.sss    # Battle Course 3 track layout
../mode7/scr/battle/battle05.sss    # Battle Course 2 track layout
../sound/final01.cpr                # Podium ceremony music
../bin/demo_kong.bin                # Demo recorded input Donkey Kong J.r.
../bin/demo_kame.bin                # Demo recorded input Koopa Troopa
../obj/others/mark.cpr              # Driver face and little position number sprites
../sound/grass.cpr                  # Donut Plains music
../mode7/scr/ice/ice02.sss          # Vanilla Lake 1 track layout
../color/ending.cpr                 # Credits color palette
../back/chr/moji-e.cpr              # Many font and a few icon gfx (2bpp)
../select/select-e.bin              # Player and cup selection screen gfx (2bpp) & layout
../title/title-e.bin                # Title and GP result screen gfx & layout - this is a compressed data pack.
../final/final-e.sss                # Podium screen gfx & layout double compressed data pack, could incode code?
../obj/kart/yossy.CGX               # Yoshi driver sprite
../mode7/chr/item.cpr               # Common road gfx (4bpp rev) ? blocks, speed boost arrows etc.
../obj/others/item.cpr              # Item sprites 
../color/circuit.cpr                # Mario Circuit color palettes
../color/obake.cpr                  # Ghost Valley color palettes
../color/grass.cpr                  # Donut Plains color palettes
../color/castle.cpr                 # Bowser Castle color palettes
../color/ice.cpr                    # Vanilla Lake color palettes
../color/dart.cpr                   # Choco Island color palettes
../color/sand.cpr                   # Koopa Beach color palettes
../color/star.cpr                   # Rainbow Road color palettes
../mode7/chr/star.cpr               # Rainbow Road road gfx (4bpp rev)
../obj/kart/kame.CGX                # Koopa driver sprite
../mode7/chr/grass.cpr              # Donut Plains road gfx (4bpp rev)
../mode7/scr/circuit/circuit04.sss  # Mario Circuit 2 track layout
../mode7/chr/sand.cpr               # Koopa Beach road gfx (4bpp rev)
../obj/kart/kinopio.CGX             # Toad driver sprite
../obj/others/killer.cpr            # Chain Chomp sprite
../mode7/chr/obake.cpr              # Ghost Valley road gfx (4bpp rev)
../drive/drive-data.bin             # Driver AI data for all tracks, zones and targets(drop points for Lakitu)
../sound/select.cpr                 # Menu music
../bin/tan-data.cpr                 # tan values for the AI to workout it's turning angle between points
../sound/circuit.cpr                # Mario Circuit music
../sound/battle.cpr                 # Battle Mode music
../sound/ice.cpr                    # Vanilla Lake music
../back/scr/star.scr                # Rainbow Road background layout
../mode7/scr/dart/dart03.sss        # Choco Island 1 track layout


Advanced users
--------------

If you want to edit the build.bat to make it work for your build.  Load the build.bat in a hex editor (take a backup first)
and delete FF FE 0D 0A from the start.

Why have I done this?  If you can't use a Hex editor you shouldn't be messing with the bat file.


Editing files
-------------

Suggested Tools for editing

Graphics:
	tilemolester
	yychr

Palettes:
	SNESPal

Music:
	PrixCompose
	AddMusicK
	
Binaries:
	XVI32

Code:
	Visual Studio
	Sublime Text 3








---------------------
     Final Notes
---------------------



If you are interested in updates to this project, or Super Mario Kart in general, come join the 
Super Mario Kart Workshop Discord!
	https://discord.gg/QNcKNQC


MrL's Patreon:
This program is provided completely free of charge, at no cost to the user. However, it has been
brought to my attention that some people would like to donate in order to support me in my efforts
in making more -- as well as better -- tools for the community as a whole. If this applies to you, 
donate via the link below. 10% of all proceeds earned through that donation link will go towards 
the Autistic Self Advocacy Network, a charity devoted to the betterment of autistic and disabled
individuals.
 
Patreon:
	https://www.patreon.com/MrL314 













---------------------------------------------------------------------------
Project L is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
---------------------------------------------------------------------------
