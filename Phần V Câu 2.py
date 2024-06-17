import math
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
    # Trường hợp 1:
    if len(constraint)<=1:
        for i in constraint:
                a.append(i[0])
                b.append(i[1])
                c.append(i[2])
                g+=1
        t=float(0)
        g=float(0)
        if a[0]==0:
            g=c[0]/b[0]
        elif b[0]==0:
            t=c[0]/a[0]
        elif 1==1:
            g=c[0]/b[0]
        if a[0]*(t+a[0])+b[0]*(g+b[0])-c[0]<=0:
            if alpha*t+beta*g<(alpha*(t+a[0])+beta*(g+b[0])):
                print('Co vo han phuong an toi uu')
            else:
                print(alpha*t+beta*g)
        elif a[0]*(t-a[0])+b[0]*(g-b[0])-c[0]<=0:
            if alpha*t+beta*g<(alpha*(t-a[0])+beta*(g-b[0])):
                print('Co vo han phuong an toi uu')
            else:
                print(alpha*t+beta*g)
    #Trường hợp 2:
    if len(constraint)>=2:
        for i in constraint:
                a.append(i[0])
                b.append(i[1])
                c.append(i[2])
                g+=1
        for l in range(g):
            for j in range(l,g):
                if a[l]*b[j]-a[j]*b[l] != 0:
                    o= intersectTwoLine(a[l],b[l],c[l],a[j],b[j],c[j])
                    x0.append(o[0])
                    y0.append(o[1])
        j=0
        for k in range(len(x0)):
            for l in range(len(a)):
                if a[l]*x0[k]+b[l]*y0[k]-c[l]<=0:
                    j+=1
            if j== len(a):
                x.append(x0[k])
                y.append(y0[k])
            j=0

        if x==[]:
            print('INVALID')
            exit()
        sumdegrees=0
        #Tìm tổng số đo các góc ở đỉnh của miền nghiệm
        for q in range(len(x)):
            for j in range(len(constraint)):
                if a[j]*x[q]+b[j]*y[q]-c[j]==0:
                    for l in range(j+1,len(constraint)):
                        if a[l]*x[q]+b[l]*y[q]-c[l]==0:
                            if ((b[q]-b[j])**2+(a[q]-a[j])**2) != 0:
                                if a[l] * (x[q]-b[j]) + b[l] * (y[q]+a[j]) - c[l]<=0 and a[j] * (x[q]-b[l]) + b[j] * (y[q]+a[l]) - c[j]<=0 :
                                    cos=(b[q]*b[j]+a[q]*a[j])/(math.sqrt((b[q]-b[j])**2+(a[q]-a[j])**2))
                                    radian=math.acos(cos)
                                    degree=math.degrees(radian)
                                    sumdegrees+=degree

                                if a[l] * (x[q]+b[j]) + b[l] * (y[q]-a[j]) - c[l]<=0 and a[j] * (x[q]-b[l]) + b[j] * (y[q]+a[l]) - c[j]<=0 :
                                    cos=(-b[q]*b[j]-a[q]*a[j])/(math.sqrt((b[q]-b[j])**2+(a[q]-a[j])**2))
                                    radian=math.acos(cos)
                                    degree=math.degrees(radian)
                                    sumdegrees+=degree

                                if a[l] * (x[q]+b[j]) + b[l] * (y[q]-a[j]) - c[l]<=0 and a[j] * (x[q]+b[l]) + b[j] * (y[q]-a[l]) - c[j]<=0 :
                                    cos=(b[q]*b[j]+a[q]*a[j])/(math.sqrt((b[q]-b[j])**2+(a[q]-a[j])**2))
                                    radian=math.acos(cos)
                                    degree=math.degrees(radian)
                                    sumdegrees+=degree

                                if a[l] * (x[q]-b[j]) + b[l] * (y[q]+a[j]) - c[l]<=0 and a[j] * (x[q]+b[l]) + b[j] * (y[q]-a[l]) - c[j]<=0 :
                                    cos=(-b[q]*b[j]-a[q]*a[j])/(math.sqrt((b[q]-b[j])**2+(a[q]-a[j])**2))
                                    radian=math.acos(cos)
                                    degree=math.degrees(radian)
                                    sumdegrees+=degree
        # print(sumdegrees)
        # Dựa vào số đo để nhận xét miền nghiệm đóng hay mở
        if sumdegrees==((len(x)-2)*180):             

            optimalVal=alpha*x[0]+beta*y[0]
            for q in range(len(x)):
                if alpha*x[q]+beta*y[q] > optimalVal:
                    optimalVal=alpha*x[q]+beta*y[q]
                    print('aaa')
            return optimalVal
        else:
            optimalVal=alpha*x[0]+beta*y[0]
            xmax=x[0]
            ymax=y[0]
            for q in range(len(x)):
                if alpha*x[q]+beta*y[q] > optimalVal:
                    optimalVal=alpha*x[q]+beta*y[q]
                    xmax=x[q]
                    ymax=y[q]
            g=0
            i=0
            q=0
            j=0
            l=0
            thai=True
            dk=[]
            for l in range(len(constraint)):
                dk.append(0)
            l=0
            for l in range(len(constraint)):
                for q in range(len(x)):
                    if a[l]*x[q]+b[l]*y[q]-c[l]==0:
                        dk[l]+=1
            l=0
            q=0
            # print(dk)
            #Xem hàm mục tiêu tiến ra vô cùng hay có giá trị tối ưu
            for l in range(len(constraint)):
                if dk[l]==1:
                    for i in range(len(x)):
                        if a[l]*x[i]+b[l]*y[i]-c[l]==0:
                            if (x[i]!=xmax and y[i]!=ymax and alpha*x[i]+beta*y[i] != optimalVal):
                                print(optimalVal)
                                exit()
                            else:
                                for q in range(len(constraint)):
                                    if a[q]*(x[i]-b[l])+b[q]*(y[i]+a[l])-c[q]<=0 and alpha*(x[i]-b[l])+beta*(y[i]+a[l]) > optimalVal:
                                        optimalVal='INFINITE'
                                        return optimalVal
                                    elif (a[q]*(x[i]+b[l])+b[q]*(y[i]-a[l])-c[q])<=0 and (alpha*(x[i]+b[l])+beta*(y[i]-a[l])) > optimalVal:
                                        optimalVal='INFINITE'
                                        return optimalVal
                                    elif 1==1:
                                        return optimalVal
                                
print(LPMax2Var (6, 25, [[3, 5, 240] , [0, 1, 12], [-1, 0, 0], [0,-1, 0]]))