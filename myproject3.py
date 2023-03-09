### 함수
def x_func(n1, n2):
    return n1 * n2

### 전역
num1, num2, res = 100, 200, 0
### 메인
res = x_func(num1, num2)
print(num1, '*', num2, '=', res)
