# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

# someone@gmail.com
# bill.gates@microsoft.com

# -*- coding: utf-8 -*-
import re


def is_valid_email(addr):
    if re.match(r'[\w\d.]+@\w+.com',addr):
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')