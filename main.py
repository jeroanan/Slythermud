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
import select
import sys
import socket
import time

import config
import database.build as db_build
import sckInfo
import world.build as world_build

class Slyther(object):

    def __init__(self):
        self.__cfg = config.Config()
        self.__socks = []
        self.__mud_socket = None
        self.__world = None
        self.__logger = logging.getLogger('Slyther')

        logging.basicConfig(level=logging.INFO)

    def start(self):
        try:
            db_build.Build(self.__cfg).build()
            self.__world = world_build.build()

            self.__mud_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__mud_socket.setblocking(0)
            self.__mud_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.__mud_socket.bind((self.__cfg.listen_address, self.__cfg.listen_port))
            self.__mud_socket.listen(5)

            self.__logger.info('Listening at {address}:{port}'.format(address=self.__cfg.listen_address,port=self.__cfg.listen_port))

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

    def __main_loop(self):

        while True:
            time.sleep(0.1)
                    
            r, _, _ = select.select([self.__mud_socket], [], [], 0)
            
            if self.__mud_socket in r:

                sck = sckInfo.sckInfo()
                sck.sck, sck.addr = self.__mud_socket.accept()

                self.__logger.info("New connection from {addr}".format(addr=sck.addr))
                sck.change_state(self.__cfg, self.__world, 1)
                self.__socks.append(sck)
    
            for sck in self.__socks:                    
                if sck.closed:
                    self.__socks.remove(sck)
                    next

                lineIn = sck.recv_string().strip("\n").strip("\r")
    
                if lineIn=="": continue
    
                sck.game_state.process_input(lineIn)
                

if __name__=="__main__":
    s = Slyther()
    s.start()
