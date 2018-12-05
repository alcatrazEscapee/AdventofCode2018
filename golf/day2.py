def f(a):
 t=u=0
 for b in a:
  i=j=0
  for c in b:n=b.count(c);i|=n==2;j|=n==3
  t+=i;u+=j
 print(t*u)