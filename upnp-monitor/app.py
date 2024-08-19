# -*- coding: utf-8 -*-
##
# Copyright (c) 2024 Ivan Semkin.
#
# This file is part of UPnP-Monitor
# (see https://github.com/vanyasem/UPnP-Monitor).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
##

import miniupnpc
import sys


def main():
    upnp = miniupnpc.UPnP()

    upnp.discoverdelay = 200
    # discovery process, it usually takes several seconds (2 seconds or more)
    print('Discovering... delay=%ums' % upnp.discoverdelay)
    print(upnp.discover(), 'device(s) detected')

    # select an igd
    try:
        upnp.selectigd()
    except Exception as e:
        print('Exception :', e)
        sys.exit(1)

    # display information about the IGD and the internet connection
    print('local ip address :', upnp.lanaddr)
    print('external ip address :', upnp.externalipaddress())
    print(upnp.statusinfo(), upnp.connectiontype())

    # list the redirections :
    port_index = 0
    while True:
        port_mapping = upnp.getgenericportmapping(port_index)
        if port_mapping is None:
            break
        print(port_index, port_mapping)
        (port, protocol, (host_ip, host_port), description, is_enabled, r_host, lease_duration) = port_mapping
        # print port, description
        port_index += 1


if __name__ == '__main__':
    main()
