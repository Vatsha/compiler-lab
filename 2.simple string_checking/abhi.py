print("Grammar : S->aS|Sb|ab|E")
string = str(input('Enter a String : '))
false=0
if(string[0]=='a'):
	flag=0
	for c in string[1:]:
		if(c=='b'):	
			flag=1
			continue
		elif((flag==1) and (c=='a')): 
			print("The string does not belong to the specified grammar")
			false=1
			break
		elif(c=='a'):
			continue
		
	if false==0:
		print("String accepted")
