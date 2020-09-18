#######################################
#    RICOH as65c REMAKE   by MrL314   #
#######################################





If you have any questions, concerns, or considerations, contact me directly through 
my discord. I am usually active and try to respond within a reasonable time.
	MrL314#8106

		




If you are intending to use this as a general purpose assembler, BE CAREFUL!!!
This assembler was formatted after the programming practices used in SMK source
files, meaning that the syntax is very strict. As such,

   put ! before 2-byte word values
   put < before 1-byte direct-page values
   put > before 3-byte long values
   put # before const values

These are not necessary in data tables, but in code it is mostly necessary for this
assembler to work. 

Be advised when using storage directives in org sections, or any section not based 
around $000000 for that matter. I have not fully implemented that feature yet, as it
will require a significant modification to the general process of the assembler... so
for now just try to avoid those when possible, and just EQU the correct addresses. 
I hope to be able to fix that issue in a future release. 

I would also caution against near-labeled $ variables, as in my experience they tend to
have unintended behavior and in the end just make debugging a whole lot harder.

Not a ton of error checking/error handling has been completed yet (for the sake of getting
this out), so be advised that you are going to want to make sure everything is exactly
how you want it if creating custom code.


###############################
# Building SMK                #
###############################

Assuming you have the source files in the correct directories (as per the previous README),
to assemble the game, you simply need to run createROM.bat. This will assemble the
necessary files from their .asm counterparts, convert them into .REL and .LIS files, 
then link the files together into a final ROM. After that, it will place the asset file 
data into the correct places in the ROM. The output file will be a file in the directory above,
(the folder that has createSource.exe), named "final output.sfc". 

The build process will take some time. Please be patient with the builder. If you do not see any 
files being written, something is wrong with the build process. You are either missing files, or
the build environment is having issues. Is you are absolutely sure that everything is set up
correctly, and you are still having issues with files not showing up, please email me with the
system you are running this on, and any other relevant information.

After building, you will notice a file named "fhist.ahist". This file is here for ease of compilation.
The file stores a hashed version of each of the assembled files at the time of compilation. This way,
if you don't change anything in that file, the compiler does not need to waste time re-compiling it. 
If you want to force all files to be re-assembled, simply delete "fhist.ahist".




##############################
# REL debugging              #
##############################


To debug rel files, use the "rel reader.py" program. Simply run
	rel_reader.exe <file>




I will be writing a more in-depth instruction manual soon, but I would like to 
get a beta version of this out before it becomes too much hassle. So stay up
to date with the newest releases on the discord server:
	https://discord.gg/QNcKNQC



* side note, in my testing, Windows Defender was acting up and calling specifically assembler.exe
a trojan. I believe I was able to stop that issue from happening (thank pyinstaller for that issue).
However, if your antivirus software flags assembler.exe, or any of these programs as a Trojan, please
do not hesitate to contact me. I am more than willing to provide the source code so you can assemble
the program yourself, or even run the python script raw if that is your preference. 
If you could also send me the name of the specific antivirus program that flagged my software so I can
get in touch and warn them about false-positives, that would be very helpful!





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

