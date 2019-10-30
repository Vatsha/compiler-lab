def match(ss):
	global i
	global look
	i=i+1
	look=s[i]

def E():
	global flag
	global look
	if look=="n":
		match("n")
		T()
	if look=="$":
		flag=1
		print "SUCCESS"
def T():
	global d
	global look
	a=d['T']
	if look=="*":
		match("*")
		if look=="n":
			match("n")
			T()
		else:
			print "Rejected"
			exit()
	else:
		for i in range(len(a)):
			if "{" in a[i]:
				return
		print "Rejected"
		exit()

flag=0
d=dict()
d['E']=["nT$"]
d['T']=["*nT","{"]
print d
s=raw_input("Enter the string")
s=s+"$"
i=0
look=s[i]
E()
if flag==0:
	print "Rejected"