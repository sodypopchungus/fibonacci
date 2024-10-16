# fibonacci sequence

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") # for subscript indexes

mode = 0 # 0 = first N fibonacci numbers (including the seed [0, 1]);
         # 1 = (N-1)th fibonacci number (including the seed [0, 1]);

a = 0    # seed 0
b = 1    # seed 1

N = 100   # the number of iterations

for i in range(N):
    if mode == 0: print('F' + str(i).translate(SUB) + ' = ' + str(a))
    b = a + b
    a = b - a
    i = i + 1

if mode == 1: print('F' + str(N - 1).translate(SUB) + ' = ' + str(b - a))

