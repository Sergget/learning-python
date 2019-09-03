# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    N=[]
    a=n
    while a!=0:
        N.append(a % 10)
        a = (a-a%10)/10
    for x in N:
        a=x+a*10
    if a == n: return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~200:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
        111, 121, 131, 141, 151, 161, 171, 181, 191
]:
    print('测试成功!')
else:
    print('测试失败!')