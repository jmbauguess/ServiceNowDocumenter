#!/usr/bin/env python
# -*- coding: utf-8 -*-

from updateSetFetcher import UpdateSetFetcher
import sys

def main():
	serviceNow = UpdateSetFetcher()
	if (len(sys.argv) < 2):
		print "Invalid use.  Usage: scriptname <update set name> <username> <password> <instance>"
		sys.exit(2)
	serviceNow.main(sys.argv[1:])
	
if __name__ == "__main__":
   main()