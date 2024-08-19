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

from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'miniupnpc',
]

setup(
    name='UPnP-Monitor',
    version='0.0.1',
    description='Monitor local UPnP activity',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vanyasem/UPnP-Monitor',
    download_url='https://github.com/vanyasem/UPnP-Monitor/archive/v0.0.1.tar.gz',
    author='Ivan Semkin',
    author_email='ivan@semkin.ru',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Networking :: Monitoring',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'upnp-monitor=upnp-monitor.app:main',
        ],
    },
    keywords=['upnp', 'monitor', 'networking', 'security', 'cybersecurity']
)
