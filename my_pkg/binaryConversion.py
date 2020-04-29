#!/usr/bin/python

def bin_toOct(binList):
	octString = ""
	
	num = 0
	digit = 0
	for ch in reversed(binList):   #거꾸로 binList를 읽습니다.
		num += int(ch) * (2**digit)
		digit += 1
		if digit is 3: #binary 3자리 단위로 8진수 자리를 추가.
			octString += chr(ord('0')+num)
			num = 0
			digit = 0
	
	if num != 0:
		octString += chr(ord('0')+num)
	
	return octString[::-1]   #뒤집어서 반환
	
	
	



def bin_toDec(binList):
	num = 0
	digit = 0
	for ch in reversed(binList):
		num += int(ch) * (2**digit)
		digit += 1
	
	return num	







def bin_toHex(binList):
	hexString = ""
	
	num = 0
	digit = 0
	for ch in reversed(binList):
		num += int(ch) * (2**digit)
		digit += 1
		if digit is 4:  #binary 4자리 단위로 16진수 자리 추가
			if num >= 10:
				hexString += chr(ord('A')+num-10)
			else:
				hexString += chr(ord('0')+num)   #10 넘으면 A~F로 변경 
			num = 0
			digit = 0
	
	if num != 0:
		if num >= 10:
			hexString += chr(ord('A')+num-10)
		else:
			hexString += chr(ord('0')+num)
	
	return hexString[::-1]












