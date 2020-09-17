##########################
#  PROJECT L  by MrL314  #
##########################
version 0.4: Sep. 10, 2020



Contact Me: 
	email: LFmisterL314@gmail.com
	discord: MrL314#8106


Special thanks to:
	SmorBjorn
	Dirtbag
	Everyone in the SMK Workshop community!!
	and YOU!
	





So you're looking to assemble an SNES game? Well you've come to the right place.
PROJECT L is a general purpose assembler and linker for SNES games. The main 
project in mind was to be able to assemble Super Mario Kart directly from the
source files, however I have plans to make this project more general purpose in
the future!

This project is in no way affiliated with Nintendo. I have no connections to Nintendo,
so this entire project is a third party SDK for the SNES. As such, I expect most of you
to be coming here for assembling Super Mario Kart. Instructions to build SMK are given 
below. However, because this is completely third party, extra efforts have been taken
in order to ensure none of Nintendo's IP are used directly in the program. Since
a few files were indeed missing regarding SMK's source code, one of the files had to be
built from scratch, meaning I had to find another way around to both create that file
and keep Nintendo's data out of the program. You will see this later. For now, let's build
a Super Mario Kart English ROM!





################################
# Building SMK-e               #
################################

In order for this program to work correctly, you first need to have a copy of the leaked
data from the GigaLeak. I cannot, and will not, provide these files for you. You MUST find
these files elsewhere. 
Once you have obtained those files, you should have one folder named "other". This is the main
folder you will be working with. 
Navigate to "other/NEWS/テープリストア/NEWS_05/home". Copy the entirety of the "home" folder into
the same directory as this program. The folder that this readme is a part of should now hold
the following items:

as65c v0.4
home
README.txt
createSource.exe

If your folder does not look like this, make sure you copy the home FOLDER, not just the 
contents of the folder. The home folder should contain a few sub-folders, namely the users
of the NEWS_05 workstation. Make sure that you unzip every folder in the kimura directory.
If the folders are not unzipped, the program will not work.

After your folders are all organized, it is finally time to start building SMK!

Run "createSource.exe". You will be prompted to enter a key. This is a safety to ensure that 
none of the Nintendo code is in my files. I will not provide the exact keys for you, but the
keys are easy to figure out, and must be entered in the exact correct way.

Key #1: The name of this project, in all caps, with the space between the two parts.
Key #2: The name of the developer of this project. Case-sensitive. 
(Hint: both of the answers to these are in this file somewhere)

If you entered either of the keys incorrectly, the program will tell you such.  

However, if you entered both keys correctly, you should see a long list of actions that the 
source creator is doing. These are to both set up the correct code organization, and to make
edits to the source files in order to allow them to compile both correctly, and at all. 

Once that finishes, you should see a new folder in the same directory named "kimura". This folder
holds all of the relevant source code for building the SMK rom! If you intended only to gather
the relevant source files for the English retail build, you are done! However, if you intend to
either: build the full ROM, or start making edits to the code, you may proceed onto step 2, which 
can be found in the as65c v0.4 folder!


  Happy karting, 
      -MrL314 


For source, you may find the github here: https://github.com/MrL314/Project-L



If you are interested in updates to this project, or Super Mario Kart in general, come join the 
Super Mario Kart Workshop Discord!
	https://discord.gg/QNcKNQC



This program is provided completely free of charge, at no cost to the user. However, it has been
brought to my attention that some people would like to donate in order to support me in my efforts
in making more and better tools for the community as a whole. If this applies to you, feel free to
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
