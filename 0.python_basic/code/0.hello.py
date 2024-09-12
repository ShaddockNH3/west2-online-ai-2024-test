def is_even(n):
    if n==0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n==0:
        return False
    else:
        return is_even(n-1)

print(is_even(9))
print(is_odd(9))
