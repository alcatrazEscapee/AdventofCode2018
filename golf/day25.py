from networkx import*
def f(a):
 g,c=Graph(),[*map(eval,a)]
 for i in c:g.add_edges_from((i,j)for j in c if sum(abs(i[k]-j[k])for k in(0,1,2,3))<4)
 print(number_connected_components(g))