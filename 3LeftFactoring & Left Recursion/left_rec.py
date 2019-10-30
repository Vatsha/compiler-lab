arr=[]
temp=[]
final=[]
alpha=[]
beta=[]
n=int(raw_input("Enter num of productions you want to enter :"))
for i in range(0,n):
    arr.append(raw_input())
for i in range(0,len(arr)):
    
    t=[]
    for j in range(0,len(arr[i])):
       
        if(arr[i][j]!="|"):
            t.append(arr[i][j])
        else:
            temp.append(t)
            t=[]
        if(j==len(arr[i])-1):
            temp.append(t)
    
    
    for x in range(0,len(temp)):
        if(x==0):
            if(temp[x][0]==temp[x][3]):
                print "Left recursion detected in the grammar"
                alpha.append(temp[x][4:len(temp[x])+1])
                
            else:
                final.append(arr[i])
                break
        else:
            if(temp[x][0]==temp[0][0]):
                alpha.append(temp[x][1:len(temp[x])+1])
            else:
                beta.append(temp[x])
        
    for i in range(0,len(alpha)):
        s=""
        for j in range(0,len(alpha[i])):
            s=s+alpha[i][j]
        
        final.append(temp[0][0]+"'"+"->"+s+temp[0][0]+"'"+"|Epsilon")
    for i in range(0,len(beta)):
        s=""
        for j in range(0,len(beta[i])):
            s=s+beta[i][j]
        
        final.append(temp[0][0]+"->"+s+temp[0][0]+"'")
    temp=[]
    t=[]
    alpha=[]
    beta=[]            
print final
