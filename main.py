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

import sys
import socket
import string        
import config
import sckInfo
import slurpFile
import states.state1 as state1

class Slyther(object):

    def __init__(self):
        self.__cfg = config.Config()
        self.__socks = []
        self.__mud_socket = None

    def start(self):
        try:
            self.__main_loop()
        except KeyboardInterrupt:
            sys.exit(0)
            self.__shutdown()
        except:
            self.__shutdown()
            raise

    def __shutdown(self):
        for sck in self.__socks:
            sck.close()
            self.__mud_socket.shutdown(2)
            self.__mud_socket.close()


    def __entered_state(self, stateNumber, sInfo):
        """Called when a new game_state is entered into,
        stateNumber = new game_state, sInfo is the
        sckInfo object pertaining to that player."""
        
        if stateNumber == 1:
            sInfo.game_state = state1.State1(sInfo, self.__cfg)
    
    def __interpret_comm(self, dat, sInfo):
        dat = dat.strip("\n")
        dat = dat.strip("\r")
        
        sInfo.game_state.process_input(dat)
    
    def __main_loop(self):
        
        self.__mud_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__mud_socket.setblocking(0)
        self.__mud_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__mud_socket.bind((self.__cfg.listen_address, self.__cfg.listen_port))
        self.__mud_socket.listen(5)
        self.__socks.append(sckInfo.sckInfo())
    
        #main game loop starts here...
        while 1==1:
                    
            try:
                current_socket = self.__socks[len(self.__socks)-1]
                current_socket.sck, current_socket.addr = self.__mud_socket.accept()
                self.__entered_state(1, current_socket)
                self.__socks.append(sckInfo.sckInfo())
                                        
            except socket.error:
                pass        
    
            for sck in self.__socks:                    
                lineIn = sck.recvString()
    
                if lineIn=="": continue
    
                self.__interpret_comm(lineIn, sck)

if __name__=="__main__":
    s = Slyther()
    s.start()
