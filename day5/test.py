def harmonic_mean(*inp):
    if len(inp) == 0:
        raise Exception("No input")

    if not all(type(x) in (int, float, complex, bool) for x in inp):
        raise Exception("At least a input argument isn't numeric type")

    if any(x in (0, False, 0j) for x in inp):
        raise Exception("Input should be a non-zero number")

    result = len(inp) / sum(1/x for x in inp)

    if type(result) == complex:
        real = round(result.real, 4)
        imag = round(result.imag, 4)
        return complex(real, imag)
    
    return result

# print(harmonic_mean())
# print(harmonic_mean(1, 1, 1))
# print(harmonic_mean('1', 1, 1))
# print(harmonic_mean(1, 0.2, -3.4, 9, 0.2j, False))
print(harmonic_mean(1, 0.2, -3.4, 9, 0.2j, True))

    