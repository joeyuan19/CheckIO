f=lambda n:(f(n-1)+f(n-2) if n-1 else 1) if n else 0
t=lambda n:((t(n-1)+t(n-2)+t(n-3) if n-2 else 1) if n-1 else 1) if n else 0
l=lambda n:(l(n-1)+l(n-2) if n-1 else 1) if n else 2
j=lambda n:(j(n-1)+2*j(n-2) if n-1 else 1) if n else 0
a=lambda n:(2*a(n-1)+a(n-2) if n-1 else 1) if n else 0
b=lambda n:((b(n-2)+b(n-3) if n-2 else 2) if n-1 else 0) if n else 3
c=lambda n:((c(n-2)+c(n-3) if n-2 else 1) if n-1 else 1) if n else 0

def f(n):
    x,y = 0,1
    for i in range(n):
        x,y = y,x+y
    return x

def t(n):
    x,y,z = 0,1,1
    for i in range(n):
        x,y,z = y,z,x+y+z
    return x

def l(n):
    x,y = 2,1
    for i in range(n):
        x,y = y,x+y
    return x

def j(n):
    x,y = 0,1
    for i in range(n):
        x,y = y,2*x+y
    return x

def a(n):
    x,y = 0,1
    for i in range(n):
        x,y = y,x+2*y
    return x

def b(n):
    x,y,z = 3,0,2
    for i in range(n):
        x,y,z = y,z,x+y
    return x

def c(n):
    x,y,z = 0,1,1
    for i in range(n):
        x,y,z = y,z,x+y
    return x

def g(n,P):
    for I,C in P[3]:
        if n == I:
            return C
    return sum(P[i] and P[i]*g(n-3+i,P) for i in range(3))

d={'f':f,'t':t,'l':l,'j':j,'pel':a,'per':b,'pa':c}
p={'f':(0,1,1,((0,0),(1,1))),
    't':(1,1,1,((0,0),(1,1),(2,1))),
    'l':(0,1,1,((0,2),(1,1))),
    'j':(0,2,1,((0,0),(1,1))),
    'pel':(0,1,2,((0,2),(1,1))),
    'per':(1,1,0,((0,3),(1,0),(2,2))),
    'pa':(1,1,0,((0,3),(1,0),(2,2)))}

def fibgolf(type, num):
    for i,_p in p.items():
        if type.startswith(i):
            return g(num,_p)

def check(type, num):
    for i,_f in d.items():
        if type.startswith(i):
            fn = _f(num)
            gn = g(num,p[i])
            assert fn == gn



def test():
    assert fibgolf('fibonacci', 10) == 55
    assert fibgolf('tribonacci', 10) == 149
    assert fibgolf('lucas', 10) == 123
    assert fibgolf('jacobsthal', 10) == 341
    assert fibgolf('pell', 10) == 2378
    assert fibgolf('perrin', 10) == 17
    assert fibgolf('padovan', 10) == 9

test()
