# Copyright (c) 2003,2017,2018 the SlytherMUD development team.
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

import logging
import socket
import select
import string
import os

import states.statefactory as statefactory

class sckInfo:

    def __init__(self):
        self.sck = None
        self.addr = 0
        self.username = ""
        self.recvq = ""    
        self.is_sock = False
        self.closed = False

        self.__game_state = None
        self.__player = None

        self.__logger = logging.getLogger('sckInfo')
        logging.basicConfig(level=logging.INFO)

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

    def change_state(self, config, world, state_number):
        self.game_state = statefactory.StateFactory.Create(self, config, world, state_number)

    def recv_string(self):
        if self.closed: return ""
        
        if os.name == "posix":
            x, _, _ = select.select([self.sck], [], [], 0)

            if self.sck in x:
                self.is_sock = True

        else: 
            type(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
            if type(self.sck)==socket.SocketType:
                 self.is_sock = True
                
        if self.is_sock:
            try:                                
                data = self.sck.recv(1024).decode()
                if not data: self.close()
                self.recvq += data
            
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
            self.__logger.info("Disconnecting {addr}".format(addr=self.addr))
            self.sck.shutdown(2)
            self.sck.close()
            self.closed = True
        except:
            pass
            