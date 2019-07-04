#========================================================#
#                                                        #
#  setup.py - PyPI 用 setup スクリプト                   #
#                                                        #
#                            (C) 2019-2019 VIPPOOL Inc.  #
#                                                        #
#========================================================#

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath( path.dirname( __file__ ) )

with open( path.join( here, 'README.en.md' ), encoding = 'utf-8' ) as f:
	long_description = f.read()

setup(
	name = 'vippool_storage',
	version = '1.1.5',
	description = 'A simple interface for the block chain',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/vippool/storage',
	author = 'VIPPOOL Inc.',
	author_email = 'dev-team@vippool.net',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
	],
	keywords = 'blockchain',
	packages = find_packages( exclude = [ 'tests' ] ),
	install_requires = [
		'future',
		'six',
	],
)
