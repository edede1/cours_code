def recursive_calculation(n):
    if n == 0:
        return 0
    else:
        return n + recursive_calculation(n - 1)

result = recursive_calculation(4*3*2*10)
print("Le résultat est :", result)
