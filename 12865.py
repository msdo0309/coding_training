
### PARAM ###

enable_print = 1

### Variable ###
# N : total number
# K : target wieght
# X : [[weight, value]]

N = 0
K = 0
X = []

### FUNC ###

def PRINT(*args, **kwargs):
    if (enable_print == 1):
        print(*args, **kwargs)

def get_input():

    N, K = map(int, input().split())

    for i in range(N):
        X1, X2 = map(int, input().split())
        X.append([X1, X2])

    PRINT(N, K)
    PRINT(X)

def get_input_2():
    N = 4
    K = 7
    X = [[6, 13], [4, 8], [3, 6], [5, 12]]

    PRINT(N, K)
    PRINT(X)

def find_max_value(target_weight):
    # CASE0 : 
    # CASE1 : 
    # CASE2 : 
    # CASE3 : 

### MAIN ###

get_input_2()

for i in range(K):
    find_max_value()