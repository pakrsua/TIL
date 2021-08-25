# 곱셈

N1 = int(input())
N2 = int(input())

print(N1*(N2%10))
print(N1*((N2%100)//10))
print(N1*(N2//100))
print(N1*N2)