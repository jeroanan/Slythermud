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

import socket
import select
import string
import os

class sckInfo:
	sck = 0
	addr = 0
	game_state = 0
	username = ""
	recvq = ""	
	isSock = 0

	def sendString(self, dat, crlf=1):
		if crlf == 1:
			self.sck.send((dat+"\r\n").encode())
		else:
			self.sck.send(dat.encode())

	def recvString(self):
		
		if os.name == "posix":
			x, y, z = select.select([self.sck], [], [], 0)

			if self.sck in x:
				self.isSock == 1
		else: #windows is incredibly silly about using select.select() <tosslehoff 11/03>
			type(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
			if type(self.sck)==socket.SocketType:
                                self.isSock = 1
				
		if self.isSock == 1:
	               	try:                                
                            self.recvq += self.sck.recv(1024)
			
               		except socket.error:
                		pass

		if self.recvq.find("\n") != -1:
			self.sckLines = self.recvq.split("\n")
			self.recvq = self.recvq.lstrip(self.sckLines[0]+"\n")
			return self.sckLines[0]
		
		return -1

