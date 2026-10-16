def square_root_bisection (target, tol = 0.01, it_num = 100):
   
    if target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
   
    if target == 0 or target == 1:
        print(f"The square root of {target} is {target}")
        return target

    low = 0
    high = max(1, target)


    for i in range(it_num):
        mid = (low + high)/ 2
        if high - low <= tol:
            print(f"The square root of {target} is approximately {mid}")
            return mid
       
        if mid * mid < target:
            low = mid
        else:
            high = mid
   
    print(f"Failed to converge within {it_num} iterations")
    return None

square_root_bisection(0.001, 1e-7, 50)