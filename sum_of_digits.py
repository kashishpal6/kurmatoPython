def sum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)

    return sum

n=12345
print(sum(n))
      