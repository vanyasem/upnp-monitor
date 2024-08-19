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
from time import sleep

import miniupnpc
import sys


class UPnPMonitor(object):
    def __init__(self):
        self.upnp = None
        self.igd_discovered = False
        self.igd_selected = False

    def initialize(self) -> miniupnpc.UPnP:
        """Initializes UPnP client"""
        self.upnp = miniupnpc.UPnP()
        self.igd_selected = False
        self.igd_discovered = False
        return self.upnp

    def discover_igd(self) -> int:
        """Discovers available IGDs"""
        if self.upnp is not None:
            self.upnp.discoverdelay = 200
            discovered_igd_count = self.upnp.discover()
            if discovered_igd_count > 0:
                self.igd_discovered = True
                return discovered_igd_count
            else:
                print('Failed to discover IGDs')
                sys.exit(1)

    def select_igd(self) -> str:
        """Automatically selects an IGD"""
        if self.upnp is not None and self.igd_discovered is True:
            try:
                igd_url = self.upnp.selectigd()
                self.igd_selected = True
                return igd_url
            except Exception as e:
                print('Failed to select IGD:', e)
                sys.exit(1)

    def connection_information(self):
        """Displays information about the IGD and the internet connection"""
        print('local ip address :', self.upnp.lanaddr)
        print('external ip address :', self.upnp.externalipaddress())
        print(self.upnp.statusinfo(), self.upnp.connectiontype())

    def list_redirections(self) -> list[tuple[str, str, int, str, int, str]]:
        """Lists all UPnP port redirections"""
        redirections = []
        port_index = 0
        while True:
            port_mapping = self.upnp.getgenericportmapping(port_index)
            if port_mapping is None:
                break
            (remote_port, protocol, (host_ip, host_port), description, is_enabled, remote_host, lease_duration) \
                = port_mapping
            redirections.append((protocol, host_ip, host_port, remote_host, remote_port, description))
            port_index += 1
        return redirections


def main():
    upnp_monitor = UPnPMonitor()
    upnp_monitor.initialize()
    upnp_monitor.discover_igd()
    upnp_monitor.select_igd()
    all_redirections = []
    while True:
        current_redirections = upnp_monitor.list_redirections()
        for redirection in current_redirections:
            if not all_redirections.__contains__(redirection):
                all_redirections.append(redirection)
                print(redirection)
        sleep(2)


if __name__ == '__main__':
    main()
