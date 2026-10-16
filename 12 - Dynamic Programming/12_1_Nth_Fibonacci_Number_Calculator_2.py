def fibonacci(n):
    if n < 0:
        return
    sequence = [0, 1]

    for i in range(2, n+1):
        prev1 , prev2 = sequence[i-1], sequence[i-2]
        current_sum = prev1 + prev2
        if i != n:
            prev1, prev2 = prev2, current_sum
        sequence.append(current_sum)
        print(sequence)  # Debug statement to show the sequence being built
   
    return sequence[n]

print(fibonacci(15))