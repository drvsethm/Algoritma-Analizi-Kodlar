def power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

# Örnek kullanım
base = 3
exponent = 6
print("Power Result:", power(base, exponent))
#çıktı:729
