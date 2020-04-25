# Python的dnspython库使用指南


因为平时在测试DNS的时候有些操作手动完成不方便，所以需要用到脚本，而在Python里`dnspython`这个用于DNS操作的库十分强大，但是无奈网上大部分资料只列举了少部分的用法，所以记录一下我平时使用到的功能，基本上已经能应付大部分的使用场景了。想具体了解`dnspython`可以登录官方网站阅读使用文档

## 常用工具
最常用的用法是调用默认的resolver发送解析请求，如：

```python
from dns import resolver

ans = resolver.query("www.baidu.com", "A")
print("qname:",ans.qname)
print ("reclass:",ans.rdclass)
print ("rdtype:",ans.rdtype)
print ("rrset:",ans.rrset)
print ("response:",ans.response)
```

结果为：

```
('qname:', <DNS name www.baidu.com.>)
('reclass:', 1)
('rdtype:', 1)
('rrset:', <DNS www.a.shifen.com. IN A RRset>)
('response:', <DNS message, ID 64940>)
```

在这里解析任务默认发送给系统默认的dns服务器，其中比较重要的是`response`，在`dnspython`的官方文档里，`response`属于类`dns.message.Message`，这个类也是许多`DNS query`请求的返回结果，下面详细介绍下这个类。

类的主要成员变量有：

```python
int flags   #The DNS flags of the message.
int id    #The query id; the default is a randomly chosen id.
list of RRset addictional
list of RRset answer
list of RRset authority
```

`flags`属于返回DNS报文的标志位（详见《TCP/IP详解（卷一）》关于DNS的部分），可以利用以下代码打印DNS报文的各个标志位：

```python
#!/bin/env python2.7
ans = resolver.query("www.baidu.com", "A")

def FlagCount(flags, pos):
    if (flags/(2**pos))%2 == 1:
        return True
    else:
        return False

def GetFlags(flags):
    QR_pos = 15
    AA_pos = 10
    TC_pos = 9
    RD_pos = 8
    RA_pos = 7
    QR_flag = FlagCount(flags, QR_pos)
    AA_flag = FlagCount(flags, AA_pos)
    TC_flag = FlagCount(flags, TC_pos)
    RD_flag = FlagCount(flags, RD_pos)
    RA_flag = FlagCount(flags, RA_pos)
    flag_dic = {"QR":QR_flag, "AA":AA_flag, "TC":TC_flag, "RD":RD_flag, "RA":RA_flag}
        print "flag:",
    for flag in flag_dic:
        if flag_dic[flag]:
            print flag,

flags = ans.response.flags

GetFlags(flags)
```

返回结果为：

```
flag: AA RD QR RA
```

另外一个比较重要的类就是`RRset`，通常返回的三个`section`信息都使用这个类封装，常用的用法是使用类函数`to_text()`令解析结果以字符串形式显示。如：

```python
ans = resolver.query("www.baidu.com", "A")
for i in ans.response.answer:
    print i.to_text()
```

返回结果为：

```
www.baidu.com. 1200 IN CNAME www.a.shifen.com.
www.a.shifen.com. 119 IN A 220.181.112.244
www.a.shifen.com. 119 IN A 220.181.111.188
```

## 对自己搭建的DNS服务器发送请求
当需要对自己搭建的DNS服务器发送解析请求的时候，可以使用dns.query这个类，使用这个类可以对指定的地址、端口发送自定义的DNS解析请求，下面对主要的几个成员函数贴出官方文档的说明：

```python
##使用udp发送解析命令
udp(q, where, timeout=None, port=53, af=None, source=None, source_port=0, ignore_unexpected=False, one_rr_per_rrset=False)
Return the response obtained after sending a query via UDP.
Return dns.message.Message object

##使用tcp发送解析命令
tcp(q, where, timeout=None, port=53, af=None, source=None, source_port=0, one_rr_per_rrset=False)
Return the response obtained after sending a query via TCP.
Return dns.message.Message object
```

其中，形参`where`对应DNS服务器`IP`地址，`q`对应类`dns.message.Message`。返回的结果是`dns.message.Message`，上面已经介绍如何使用这个类。
我们可以通过`dns.message.make_query()`来构造一个解析请求。看一下`make_query()`函数的原型：

```python
make_query(qname, rdtype, rdclass=1, use_edns=None, want_dnssec=False, ednsflags=None, payload=None, request_payload=None, options=None)
```

基本上设置前两个数值就够了。因此，对自己搭建的DNS服务器发送解析请求可以简要按照以下步骤：

```python
import dns

SERVER = "1.1.1.1"#your DNS server
PORT = 53#DNS server port 
dns_query = dns.message.make_query("www.baidu.com", "A")
response = dns.query.udp(dns_query, SERVER, port = PORT)

for i in response.answer:
    print i.to_text()
```

## 操作自己搭建的DNS服务器

也可以通过`dnspython`对DNS进行动态更新。比如在`bind`服务器中可以使用`rndc`工具来对`bind`进行动态更新，但是操作`rndc`工具始终不大方便，而我们也可以选择使用`dns`.`update`对`bind`进行动态更新。

**一个简单的例子:**

已知一个`zone`的`tsig`（主辅同步加密）`key-value`为`{"default":"werasdfasdfweffs==",}`，我们就可以使用这个事务签名对这个`zone`进行更新操作。如，我要对`zone testqa.com`添加100个`rdata`为`"1.1.1.1"`的主机记录，分别是`www1~www100`，可以：

```python
import dns.tsigkeyring
import dns.update
import dns.query

ZONE = "testqa.com"

keyring = dns.tsigkeyring.from_text({'default.any': 'xxxxxxxxxxxxxxx'})
update_query = dns.update.Update(ZONE, keyring=keyring)
for i in range(1,101):
    update_query.add("testqa" + str(i), 60, "1.1.1.1")
```