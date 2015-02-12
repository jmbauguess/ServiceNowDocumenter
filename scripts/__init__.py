#!/usr/bin/env python
# -*- coding: utf-8 -*-

from updateSetFetcher import UpdateSetFetcher
import sys

def main():
	if (len(sys.argv) < 2):
		print "Invalid use.  Usage: scriptname <update set name> <username> <password> <instance>"
		sys.exit(2)
	serviceNow = UpdateSetFetcher(sys.argv)
	serviceNow.main()
	
if __name__ == "__main__":
   main()