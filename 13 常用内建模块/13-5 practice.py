# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：

# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

# -*- coding: utf-8 -*-
import hashlib
md5 = hashlib.md5()
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '306ce65217793efeab89eaf2d3e75487',
    'alice': 'd12c5f3ad53aeb6bf9833f0b1658a6c0'
}
def login(user, password):
    md5.update(password.encode('utf-8'))
    # print(db[user])
    # print(md5.hexdigest())
    return db[user]==md5.hexdigest()

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# 练习
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
# db = {}

# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')
# 然后，根据修改后的MD5算法实现用户登录的验证：

# -*- coding: utf-8 -*-
import random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')