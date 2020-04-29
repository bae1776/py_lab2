#!/usr/bin/python

import my_pkg


if __name__=='__main__':
	while True:
		select = int(input("Select menu: 1) conversion 2) union/intersection 3) exit ? "))
		if select is 1:
			binNumber = list(input("input binary number : "))
			print("=> OCT>", my_pkg.bin_toOct(binNumber))
			print("=> DEC>", my_pkg.bin_toDec(binNumber))
			print("=> HEX>", my_pkg.bin_toHex(binNumber))
		elif select is 2:
			firstList = input("1st list: ")
			secondList = input("2nd list: ")
			print("=> union", my_pkg.unionList(firstList, secondList))
			print("=> intersection", my_pkg.intersectionList(firstList, secondList))
		elif select is 3:
			print("exit the program...")
			break

	
