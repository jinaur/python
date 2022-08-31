n = int(input())

count = 0
def my_func(a) :
    global count
    if a == 0 :
        count += 1
        return
    if a-2 >= 0 :
        my_func(a-2)
    if a-3 >= 0 :
        my_func(a-3) 
    my_func(a-1)
    return count


print(my_func(n))
