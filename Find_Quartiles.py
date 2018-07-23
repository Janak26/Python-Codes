r = int(input())
q = list(sorted(map(int, input().split())))

def median(x,y):
    if x%2 ==1:
        m = int((x/2)+1)
        print(y[m-1])
    elif x%2 ==0:
        m = int((x/2)-1)
        p = int((x/2))
        u = (y[m])
        v = (y[p])
        j = ((u+v)/2)
        print (int(j))


a = int(r/2)
if r%2 == 1:
    b = q[0:a]
    c = q[a+1:]
elif r%2 ==0:
    b = q[0:a]
    c = q[a:]

m1 = median(a, b)
m = median(r,q)
m2 = median(a, c)
