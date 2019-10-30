tabl = {}
'''no = input("I number")
for i in range(no):
	x = input("number of value in \n")
	print i
	temp = []
	for j in range(x):
		temp.append((raw_input("symbol\n"),raw_input("to\n")))
	tabl[i] =temp'''
gramar= {1:("E","EAE"),2:("E","a"),3:("A","+"),4:("A","*")}
tabl = {0:[("a","s2"),("E","1")],1:[("$","accept"),("+","s4"),("*","s5")],2:[("+","r2"),("*","r2"),("$","r2")],3:[("a","s2"),("E","6")],4:[("a","r3")],5:[("a","r4")],6:[("+","s4"),("*","s5"),("$","r1"),("A","3")]}

stack = "$0"
string = raw_input("enter string")+'$'
action = {}
i = 0
while True:
	print "true"
	print stack[-1]
	line = tabl[int(stack[-1])]
	for element in line:
		print "ele"
		print element[0]
		print string[0]
		if element[0]==string[0]:
			if element[1][0] == "s":
				print "1----"
				action[i] =element
				stack = stack + string[0] + element[1][-1]	
				string = string[1:]
				print stack,"stack"
				print string,"string"
			elif element[1] == "accept":
				break
			elif element[1][0] == "r":
				print "2-----"
				l = len(stack)-2*len(gramar[int(element[1][-1])][1])
				print "index",l
				stack = stack[0:l]
				action[i] =element
				print stack
				line1 = tabl[int(stack[-1])]
				for ele in line1:
					if ele[0]==gramar[int(element[1][-1])-1][0]:
						stack = stack + gramar[int(element[1][-1])-1][0] + ele[1][-1]	
				print stack,"stack"
				print string,"string"
			else:
				print "not accepted"
				break
				
			
	i = i+1
	if i ==10:
		break
print action 
