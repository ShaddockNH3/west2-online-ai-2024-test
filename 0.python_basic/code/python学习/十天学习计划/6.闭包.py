def add(cnt):
    def ad():
        nonlocal cnt
        cnt+=1
        return cnt
    return ad

c=add(4)
print(c())
print(c())



