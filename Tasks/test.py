import cmath

def DFT():
    samples = [0, 1, 2, 3]
    indices = [0, 1, 2, 3]
    N = len(samples)
    result = []
    for k in range(N):
        sum = 0
        for n in range(N):
            sum += indices[n] * cmath.exp(-1j *2* cmath.pi * k * n / N)
        result.append(sum)
    return result
print(DFT())