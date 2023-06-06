# Ngày 22/10/2022

#   Bài tập truy vấn max

#   Cách 1: Cây IT
'''
A = [-1e9] * 400005
def Update(k,L,R,i,x):
    global A
    if A[k]<x: A[k]=x
    if L<R-1:
        if i<(L+R)//2: Update(2*k+1,L,(L+R)//2,i,x)
        else: 
            Update(2*k+2,(L+R)//2,R,i,x)


def get(k,L,R,u,v):
    global A
    if L==u and R==v: return A[k]
    if v<=(L+R)//2: return get(2*k+1,L,(L+R)//2,u,v)
    if u>=(L+R)//2: return get(2*k+2,(L+R)//2,R,u,v)
    return max(get(2*k+1,L,(L+R)//2,u,(L+R)//2),get(2*k+2,(L+R)//2,R,(L+R)//2,v))



if __name__ == "__main__":
    n,m = map(int , input().split())
    for i,x in enumerate(list(map(int,input().split())),1): Update(0,1,n+1,i,x)
    for i in range(m):
        u,v = map(int,input().split())
        print (get(0,1,n+1,u,v+1))

'''


#   Cách 2: dùng load node

class node:
    def __init__(self,a,b):  #[a,b)
        self.elem=-1e9
        self.L,self.R=a,b
        if a+1==b: self.le,self.ri=None,None
        else:
            self.le=node(a,(a+b)//2)
            self.ri=node((a+b)//2,b)

def update(H,i,x):
    if H.elem<x: H.elem=x
    if H.le!=None: update(H.le if i<H.le.R else H.ri,i,x)

def get(H,u,v):
    if H.L==u and H.R==v: return H.elem
    if v<=H.le.R: return get(H.le,u,v)
    if u>=H.ri.L: return get(H.ri,u,v)
    return max(get(H.le,u,H.le.R),get(H.ri,H.ri.L,v))

if __name__ == '__main__':
    n,m=map(int,input().split())
    H=node(1,n+1)
    for i,x in enumerate(list(map(int,input().split())),1): update(H,i,x)
    for i in range(m):
        u,v=map(int,input().split())
        print(get(H,u,v+1))
