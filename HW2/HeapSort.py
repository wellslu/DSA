def heapsort(x):
    a=len(x)
    y=[]
    for i in range(a):#有多少數字就pop多少次
        for j in range(len(x),-1,-1):#從後面開始往前檢查
            try:#由於list的index可能會超過，所以用try去做檢查，如果超過則直接跳過這回合的迴圈
                if x[j]>x[2*j+1]:
                    x[j],x[2*j+1] = x[2*j+1],x[j]
                if x[j]>x[2*j+2]:
                    x[j],x[2*j+2] = x[2*j+2],x[j]
            except:
                continue
        y.append(x.pop(0))#把最上面那個最小數pop到另一個list
    return y
