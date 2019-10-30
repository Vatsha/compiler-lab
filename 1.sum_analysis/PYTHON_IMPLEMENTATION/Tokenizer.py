import re
def isOperator(str):
	for i in range(0,len(str)):
		list={"+","-","*","/","%","=","==","++","--","!=",">",">=","<=","<","&&","||","!","&","|","^","~","<<",">>","+=","-=","*=","/=","%=","<<=",">>=","&=","^=","|="}
		if str[i] in list:
			print str[i],"Is a operator"
def isKeyword(str):
	li=""
	for i in range(0,len(str)):
		if str[i]== ' ':
			list={"False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"}
			if li in list:
				print "isKeyWord"
			li=""
		else:
			li=li+str[i]
def isDelimeter(str):
	for i in range(0,len(str)):
		list={"," ,";" ,"'",'"' , "{" , "}" , "(" , ")" , "|" , "/" , "\\" }
		if str[i] in list:
			print str[i],"is a Delimeter"
def isIdentifier(str):
	pattern = re.compile("(int [a-z]*[A-Z]*[0-9]*)|(float [a-z]*[A-Z]*[0-9]*)|(double [a-z]*[A-Z]*[0-9]*)|(char [a-z]*[A-Z]*[0-9]*)")
	if (pattern.match(str)):
		x=pattern.match(str).group()
		for i in range(0,len(x)):
			if x[i]==' ':
				y=x[i+1:len(x)]
		print y,"Is a Identifier"
def isConstant(str):
	x=[]
	j=0
	for i in range(0,len(str)):
		if str[i]==' ':
			x.append(str[j:i])
			j=i+1
	x.append(str[j:len(str)-2])
	for i in range(0,len(x)):
		pattern=re.compile("(\d)*")
		if(pattern.match(x[i]).group()):
			print (pattern.match(x[i]).group()),"Is Constant"
with open("summation.c","r") as f:
	for line in f:
		isOperator(line)
		isDelimeter(line)
		isIdentifier(line)
		isKeyword(line)
		isConstant(line)
