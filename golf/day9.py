def f(t):
 p=424;m=[0];s=[*range(p)]
 for r in range(1,1+t):q=r%23<1;v=(2,-6)[q];m=m[v:]+m[:v];exec(['m=[r]+m','s[r%p]+=r+m.pop()'][q])
 return max(s)