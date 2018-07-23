r = int(input())
q = (map(int, input().split()))
w = (map(int, input().split()))
z = [e for e,c in zip(q,w) for i in range(c)]
o = sorted(z)
#print(o)

def median(x,y):
    if x%2 ==1:
        m = int((x/2)+1)
        u = (y[m-1])
        return u
    elif x%2 ==0:
        m = int((x/2)-1)
        p = int((x/2))
        u = (y[m])
        v = (y[p])
        j = ((u+v)/2)
        return j


a = int(len(o)/2)
if (len(o))%2 == 1:
    b = o[0:a]
    c = o[a+1:]
elif (len(o))%2 ==0:
    b = o[0:a]
    c = o[a:]

m1 = median(a, b)
m = median((len(o)),o)
m2 = median(a, c)
print(round(float((m2-m1)),1))