# row = ['0', '01']

# n = 6
# k = 2

# a = '0'
# b = '01'
# for i in range(2, n):
#     a, b = b, (b + b[(len(b) - len(a)):] + a)
#     print(b)


# n = 7
# k = 2


# def kthGrammar(n, k):
#     s = '0'
#     di = {'0': '01', '1': '10'}
#     t = s.maketrans(di)
#     for x in range(1, n-1):
#         s = s.translate(t)
#         print(s)

# kthGrammar(n, k)

# def kthGrammar(n, k):
#     a = k//2
#     if a % 2:
#         s = "01"
#         return s[(k%2)+1]
#     return 0
# print(kthGrammar(5, 10))

def kthGrammar(n, k):
    if n == 1 and k == 1:
        return 0
    if n == 1 and k == 2:
        return 1
    length = 2**(n-1)
    middle = length // 2

    if k <= middle:
        return kthGrammar(n-1, k)
    else:
        return 1 - kthGrammar(n-1, k-middle)


print(kthGrammar(4, 7))
