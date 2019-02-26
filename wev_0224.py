import string

f = open ("wev_optical.txt","w")
f2 = open ("wev_ptr.txt","w")
wev_width = 122

def isEven(n):
	if n % 2 == 0:
		return True
	else:
		return False
def normalWev():
	for i in range(wev_width):
		if i % 4 == 0:
			f.write("1")
		else:
			f.write("0")
	f.write("\n")

	for i in range(wev_width):
		if i % 4 == 2:
			f.write("1")
		else:
			f.write("0")
	f.write("\n")
#white even = i%4 = 0
#black even = i%4 = 1
#white odd = i%4 = 2
#black odd = i%4 = 3

def aSet():
	#24 = 120/5
	#A odd B odd
	for i in range(wev_width):
		if i % 4 == 0:
			f.write("1")
		else:
			f.write("0")
	f.write("\n")
	#A even
	for i in range(wev_width):
		if (i % 4 == 2) and (isEven(i // 24) == True): 
			f.write("1")
		else:
			f.write("0")
	f.write("\n")
	#A odd B even
	for i in range(wev_width):
		if i % 4 == 0 and (isEven(i // 24) == True):
			f.write("1")
		elif i % 4 == 2 and (isEven(i // 24) == False):
			f.write("1")
		else:
			f.write("0")
	f.write("\n")
	# A even
	for i in range(wev_width):
		if (i % 4 == 2) and (isEven(i // 24) == True): 
			f.write("1")
		else:
			f.write("0")
	f.write("\n")

def bSet():
	#A odd B odd
	for i in range(wev_width):
		if i % 4 == 0:
			f.write("1")
		else:
			f.write("0")
	f.write("\n")

	#B even
	for i in range(wev_width):
		if (i % 4 == 2) and (isEven(i // 24) == False): 
			f.write("1")
		else:
			f.write("0")
	f.write("\n")

	#A even B odd
	for i in range(wev_width):
		if i % 4 == 0 and (isEven(i // 24) == False):
			f.write("1")
		elif i % 4 == 2 and (isEven(i // 24) == True):
			f.write("1")
		else:
			f.write("0")
	f.write("\n")

	# B even
	for i in range(wev_width):
		if (i % 4 == 2) and (isEven(i // 24) == False): 
			f.write("1")
		else:
			f.write("0")
	f.write("\n")

def wev_optical():
	
	for row in range(2):
		 normalWev()

	for rows in range(2):
		for row in range(2):
			aSet()
		for row in range (2):
			bSet()

	for row in range(2):
		 normalWev()

def wev_black():
	for rows in range(20):
		wev_ptr()

def wev_ptr():
	#four rows a set
	for i in range(wev_width):
		if (i % 4 == 1) and (isEven(i // 15) == False):
			f2.write("0")
		else:
			f2.write("1")
	f2.write("\n")

	for i in range(wev_width):
		if (i % 4 == 3) and (isEven(i // 15) == True):
			f2.write("0")
		else:
			f2.write("1")
		
	f2.write("\n")

def mix():
	
	f3 = open("wev_optical.txt", "r")
	arrayA = []
	arrayA = f3.readlines()
	

	f4 = open("wev_ptr.txt", "r")
	arrayB = []
	arrayB = f4.readlines()
	print(arrayB)
	print(len(arrayB))

	f5 = open("wev_double.txt","w")
	for i in range (len(arrayB)):
		f5.write(arrayA[i])
		f5.write(arrayB[i])








wev_optical()
f.close()
wev_black()
f2.close()
mix()




	

	

	













