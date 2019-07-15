name =["sam","john","ama"]
def sqr(x): return x ** 2
 
L=list(map(len,name))
print(L)
sqr(2)

squares =list(map(sqr,L))
print(squares)


a = lambda
#>>> sum = lambda x,y: x+y
#>>> sum (6,6)
#12
#>>> f2 = lambda x,y,z: x+y/z
#>>> f2(7+6/2)
#>>> f2(7,6,2)
#10.0
#>>> p = lambda x: print(x)
#>>> p(1)
#1
#>>> m = lambda y,q: print(y+q)
#>>> m(3,6)
#9
#>>> items = [1,2,3,4,5]
#>>> print(items)
#[1, 2, 3, 4, 5]
#>>> list(map(lambda o: o **2,items))
#[1, 4, 9, 16, 25]

#>>>filter
#.......
#>>> def too_old (y): return y < 30
#... 
#>>> ages =[5,9,78,67,4,2,1]
# 
#>>> filter(too_old,ages)
#
#<filter object at 0x765d3970>
#>>> list(filter(too_old,ages))
#[5, 9, 4, 2, 1]
#>>> 
#
