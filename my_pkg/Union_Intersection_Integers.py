#!/usr/bin/python

def to_intList(listStr):  #listStr is const - String을 정수 list로 바꾸어서 반환합니다.
	lst = listStr.strip("[]").split(',')

	for i in range(0, len(lst)):
		if (not lst[i].isdigit()):
			lst[i] = lst[i].strip()
		lst[i] = int(lst[i])

	return lst






def unionList(listStrA, listStrB):
	listA = to_intList(listStrA)	#정수 List로 변환
	listB = to_intList(listStrB)
	
	listA.sort()			#오름차순 정렬 
	listB.sort()

	resultList = []
	Acur = 0
	Bcur = 0

	while (Acur < len(listA) and Bcur < len(listB)):
		if (listA[Acur] < listB[Bcur]):
			resultList.append(listA[Acur])
			Acur += 1
		elif (listA[Acur] > listB[Bcur]):
			resultList.append(listB[Bcur])
			Bcur += 1
		else:
			resultList.append(listA[Acur])
			Acur += 1
			Bcur += 1

	while (Acur < len(listA)):  #남은 원소들도 빠짐없이 추가해야한다.
		resultList.append(listA[Acur])
		Acur += 1

	while (Bcur < len(listB)):
		resultList.append(listB[Bcur])
		Bcur += 1
	
	return resultList







def intersectionList(listStrA, listStrB):
	listA = to_intList(listStrA)   
	listB = to_intList(listStrB)
	
	listA.sort()		     
	listB.sort()

	resultList = []
	Acur = 0
	Bcur = 0
	
	while (Acur < len(listA) and Bcur < len(listB)):
		if (listA[Acur] < listB[Bcur]):
			Acur += 1
		elif (listA[Acur] > listB[Bcur]):
			Bcur += 1
		else:
			resultList.append(listA[Acur])
			Acur += 1
			Bcur += 1
	
	#교집합은 남은 것들은 버린다. 

	return resultList


