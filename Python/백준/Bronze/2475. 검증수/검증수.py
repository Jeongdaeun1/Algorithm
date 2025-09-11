a, b, c, d, e = map(int, input().split())
temp = a*a + b*b + c*c + d*d + e*e
answer = temp % 10
print(answer)