import numpy as np

def matrix(A,b):
    A = [[float(item) for item in row] for row in A]
    for i in range(len(b)):
        b[i]=float(b[i])
    A = np.array(A)
    A0 = np.array(A)
    b = np.array(b)
    b0 = np.array(b)
    m,n=A.shape
    p=len(b)
    dk=[]
    for i in range(m):
        dk.append(0)
    for i in range(m):
         for j in range(n): 
            if A[i,j] == 0:
                dk[i]+=1
            else:
                break
    min=dk[0]
    o=0
    bo=[]
    thai=False
    for w in range(n-1):
        for i in range(m):
            if (i in bo)==False:
                if min> dk[i]:
                    min=dk[i]
                    o=i
        bo.append(o)
        for j in range(m):
            for k in range(n):
                if j in bo:
                    break
                else:
                    
                    thai=True
                    A[j,k]-= (A0[o,k])*( (A0[j,dk[o]])/ (A0[o,dk[o]]) )
                    
            if thai==True:
                b[j]-=b0[o]*( A0[j,dk[o]]/ A0[o,dk[o]] )
                thai=False
                
        min=n
        for r in range(m):
            dk[r]=0
        for t in range(m):
            for y in range(n): 
                if A[t,y] == 0:
                    dk[t]+=1
                else:
                    break
        for i in range(m):
            for j in range(n):
                A0[i,j]=A[i,j]
                b0[i]=b[i]
    for r in range(m):
            dk[r]=0
    for t in range(m):
        for y in range(n): 
            if A[t,y] == 0:
                dk[t]+=1
            else:
                break
    for i in range(m):
        for j in range(n):
            A[i,j]/=A0[i,dk[i]]
        b[i]/=A0[i,dk[i]]
    A0=A
    b0=b
    i=0
    l=0
    k=0
    j=0
    t=0
    y=0
    r=0
    for i in range(m):
        if dk[i]<n:
            l+=1
    x=[]
    for i in range(n):
        x.append(0)
    if l<n:
        for i in range(m):
            if dk[i]>=n and b[i]!=0:
                print('He phuong trinh vo nghiem')
            if dk[i]>=n and b[i]==0:
                print('He phuong trinh co vo so nghiem')
    if l==n:
        for i in range(m):
            if dk[i]>=n and b[i]!=0:
                print('He phuong trinh vo nghiem')
            if dk[i]>=n and b[i]==0:
                print('He phuong trinh co dung 1 bo nghiem')
        for j in range(n-1,-1,-1):
            pos=dk.index(j)
            # print(pos)
            for l in range(n):
                b[pos]-=A[pos,l]*x[l]
            x[j]=round(b[pos],2)
        print(x)
    if l>n:
        print('Day chac chan khong phai he phuong trinh bac thang =))))')
    
print(matrix([[2,3,1],[4,6,1],[1,5,1]],[11,19,14]))
