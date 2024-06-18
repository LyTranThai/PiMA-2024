import sys
def intersectTwoLine(a1, b1, c1, a2, b2, c2):
  det = a1 * b2 - a2 * b1
  if det!=0 or ( det==0 and (a1==0 or a2==0 or b1==0 or b2==0)):
    x0 = (b2 * c1 - b1 * c2) / det
    y0 = (a1 * c2 - a2 * c1) / det
    return x0, y0
  else:
      return
def LPMax2Var (alpha , beta , constraint ):
    a=[]
    b=[]
    c=[]
    x=[]
    y=[]
    g=0
    x0=[]
    y0=[]
    # Tìm tọa độ giao điểm của các đỉnh của miền nghiệm
    for i in constraint:
            a.append(i[0])
            b.append(i[1])
            c.append(i[2])
            g+=1
    for l in range(g):
        for j in range(l,g):
            if a[l]*b[j]-a[j]*b[l] != 0:
                o= intersectTwoLine(a[l],b[l],c[l],a[j],b[j],c[j])
                x.append(o[0])
                y.append(o[1])
    j=0
    for k in range(len(x)):
        for l in range(len(a)):
            if a[l]*x[k]+b[l]*y[k]-c[l]<=0:
                j+=1
        if j== len(a):
            x0.append(x[k])
            y0.append(y[k])
        j=0
    # print(x0,y0)
    optimalVal=alpha*x0[0]+beta*y0[0]
    # print(optimalVal)
    for q in range(len(x0)):
        if alpha*x0[q]+beta*y0[q] > optimalVal:
            optimalVal=alpha*x0[q]+beta*y0[q]
    return optimalVal
print("Giá trị tối ưu:",LPMax2Var (6, 25, [[3, 5, 240] , [0, 1, 12], [-1, 0, 0], [0, -1, 0]]))
