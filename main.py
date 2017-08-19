# Copyright (c) 2003,2017 the SlytherMUD development team.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


# Settings:

# Listen on which address for connections? Leave this one blank to listen on any
# address:
listen_address = ''

# Port to listen on for incoming mud connections:
listen_port = 3000

# which directory are your text files (motd, etc) located in?
text_dir = "text"

# what should your playerfile (p-file) be called?
pfile = "pfile.slythermud"

# -- End of settings -- #

import sys
import socket
import string		
import sckInfo
import slurpFile

socks = []
banner = slurpFile.slurpFile()

def startUp():
	global banner
	banner.fileName = text_dir+"/banner"
	banner.readFile()
		
def enteredState(stateNumber, sInfo):
	# Called when a new game_state is entered into,
	# stateNumber = new game_state, sInfo is the
	# sckInfo object pertaining to that player.
	if stateNumber == 1:
		#waiting for username. Therefore, we've just connected.		
		bannerMsg = banner.fileContent.split("\n")
		
		i = 0
		for bLines in bannerMsg:
			i+= 1
			if i < len(bLines) - 1:
				sInfo.sendString(bLines)
			else:
				sInfo.sendString(bLines, 0)			

	elif stateNumber == 2:
		sInfo.sendString("\nAre you sure you wish to be known as "+sInfo.userName+"? (y/n) ", 0)
	elif stateNumber == 3:
		sInfo.sendString("\nA password/phrase is needed for your new character.")
		sInfo.sendString("Please follow all the usual steps for a secure password")
		sInfo.sendString("Please type your password: ", 0)
	elif stateNumber == 4:
		sInfo.sendString("\nPlease confirm your password: ", 0)
	elif stateNumber == 5:
		sInfo.sendString("\nWhat is your sex? (m/f): ", 0)
	elif stateNumber == 6:
		#stateNumbers 6, 7 and 8 are reserved for when their
		#respective features are implemented and should not
		#be used unless you fancy fux0ring the code up :)...
		pass
	elif stateNumber == 7:
		pass
	elif stateNumber == 8:
		pass

def interpretComm(dat, sInfo):
	dat = dat.strip("\n")
	dat = dat.strip("\r")
	
	if sInfo.game_state == 1:
		#TODO: is name valid?
		#TODO: is name already taken?
		#TODO: switch state accordingly.
                pass
	elif sInfo.game_state == 2:
		if dat == "y":
			sInfo.game_state == 3
			enteredState(3, sInfo)
		else: #Nope, user is being indecisive :p
			sInfo.game_state == 1
			enteredState(1, sInfo)
	
	elif sInfo.game_state == 3:
		#TODO: encrypt dat, store dat.
                pass
	elif sInfo.game_state == 4:
		#TODO: encrypt dat, compare dat, change state accordingly.
                pass
	elif sInfo.game_state == 5:
		#TODO: get sex, change state.
                pass

def mainLoop():
	global socks
	
	mud_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mud_socket.setblocking(0)
	mud_socket.bind((listen_address, listen_port))
	mud_socket.listen(5)
	socks.append(sckInfo.sckInfo())

	#main game loop starts here...
	while 1==1:
				
		try:
			socks[len(socks)-1].sck, socks[len(socks)-1].addr = mud_socket.accept()
			socks[len(socks)-1].game_state = 1
			enteredState(1, socks[len(socks)-1])
			socks.append(sckInfo.sckInfo())
									
		except socket.error:
			pass		

		i=0
			
		for sck in socks:					
			
			lineIn = socks[i].recvString()

			if lineIn != -1:
				#TODO: Something with this you jack-ass!
                                print(lineIn)
				
			i+=1		

startUp()
mainLoop()
