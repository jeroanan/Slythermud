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

import states.statefactory as statefactory

class sckInfo:
    sck = 0
    addr = 0
    username = ""
    recvq = ""    
    is_sock = False

    __game_state = None
    __player = None

    @property
    def game_state(self):
        return self.__game_state

    @game_state.setter
    def game_state(self, val):
        self.__game_state = val
        self.__game_state.enter()

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, val):
        self.__player = val
    
    def send_string(self, dat, crlf=True):
        if crlf:
            self.sck.send((dat+"\r\n").encode())
        else:
            self.sck.send(dat.encode())

    def change_state(self, config, state_number):
        self.game_state = statefactory.StateFactory.Create(self, config, state_number)

    def recv_string(self):
        
        if os.name == "posix":
            x, y, z = select.select([self.sck], [], [], 0)

            if self.sck in x:
                self.is_sock = True

        else: 
            type(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            if type(self.sck)==socket.SocketType:
                 self.is_sock = True
                
        if self.is_sock:
            try:                                
                self.recvq += self.sck.recv(1024).decode()
            
            except UnicodeDecodeError:
                pass
            except socket.error:
                pass

            if self.recvq.find("\n") != -1:
                self.sckLines = self.recvq.split("\n")
                self.recvq = self.recvq.lstrip(self.sckLines[0]+"\n")
                return self.sckLines[0]
                
        return ""

    def close(self):
        try:
            self.sck.shutdown(2)
            self.sck.close()
        except:
            pass

