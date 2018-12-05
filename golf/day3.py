def f(a):
 s=1000;e=[0]*s*s
 for b in a:
  *_,p,q,u,v=map(int,''.join([c if 47<ord(c)<58else' 'for c in b]).split())
  for j in range(u*v):e[j//v+p+s*(j%v+q)]+=1
 print(sum(i>1for i in e))