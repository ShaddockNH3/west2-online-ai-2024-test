#三数最大
x=int(input())
y=int(input())
z=int(input())

#approach1
print(max(x,y,z))

#approach2
num_max=x
if num_max<y:
    num_max=y
if num_max<z:
    num_max=z
print(num_max)
