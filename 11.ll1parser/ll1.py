from fnf import first
from fnf import follow
import numpy as np
arr=[]
ter=[]
nter=[]
ss=raw_input("Enter Start Symbol")
n=int(raw_input("Enter the no of productions you want"))
for i in range(0,n):
    arr.append(raw_input())
d=dict()
for i in range(0,len(arr)):
    d[arr[i][0]]=''
for key in d:
    t=[]
    for i in range(0,len(arr)):
        if(arr[i][0]==key):
            t.append(arr[i][3:len(arr[i])+1])
    d[key]=t
for i in range(0,n):
	if arr[i][0] not in nter:
		nter.append(arr[i][0])
for i in range(0,n):
	for j in range(0,len(arr[i])):
		if(arr[i][j] not in nter and arr[i][j]!="-" and arr[i][j]!=">" and arr[i][j] not in ter and arr[i][j]!="{" and arr[i][j]!=" "):
			ter.append(arr[i][j])
for x in nter:
	l1=first(ter,nter,x,d)
	l=l1[0]
	k=l1[1]
	print "follow of"+x+"is"
	print set(l)
	print k
for x in nter:
	l=follow(ter,nter,x,d,ss)
	print "follow of"+x+"is"
	print set(l)
temp=[]
temp2=[]
for i in nter:
	for j in ter or "$":
		temp2.append('0')
	temp2.append("0")
	temp.append(temp2)
	temp2=[]
print temp
print ter
for i in range(len(nter)):
	fl=0
	print nter[i]
	for j in range(len(ter)):
		print ter[j]
		if ter[j] in first(ter,nter,nter[i],d)[0]:
			v=first(ter,nter,nter[i],d)[1]
			print v
			temp[i][j]=v[fl]
			fl=fl+1
	if "{" in first(ter,nter,nter[i],d)[0]:
		for j in range(len(ter)):
		    if ter[j] in follow(ter,nter,nter[i],d,ss):
			    temp[i][j]=v[fl]
			    fl=fl+1
		    if "$" in follow(ter,nter,nter[i],d,ss):
			    temp[i][len(temp[i]-1)]=v[fl]
			    fl=fl+1


print temp



