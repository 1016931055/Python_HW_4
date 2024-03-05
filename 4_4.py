b,q,a=map(float,input().split())
i = 1
bn = b * i * q
while(bn < a):
    i += 1
    bn *= q
print(i+1)