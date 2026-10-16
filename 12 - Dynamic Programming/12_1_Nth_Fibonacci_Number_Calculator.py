def fibonacci(n):
    if n< 0:
        return
    sequence = [0, 1]

    for i in range(2, n+1):
        if i == n+1:
            break
        value = sequence[i-1] + sequence[i-2]
        sequence.append(value)
   
    return sequence[n]

print(fibonacci(15))