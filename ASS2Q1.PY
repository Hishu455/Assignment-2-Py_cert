def fibonacci(n):
    lst = []
    prev_no=0
    curr_no=1
    for i in range(n):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        elif  i>=2:
            fib = prev_no + curr_no
            prev_no=curr_no
            curr_no=fib
            lst.append(fib)   
    return lst

def cube(lst):
    return lst**3

if __name__ == '__main__':
    n = int(input("Enter your range : "))
    print(list(map(cube, fibonacci(n))))