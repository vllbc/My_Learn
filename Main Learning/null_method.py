# 修改前
# import decimal

# class CreateAccountError(Exception):
#     """Unable to create a account error"""

# class Account:
#     """一个虚拟的银行账号"""

#     def __init__(self, username, balance):
#         self.username = username
#         self.balance = balance

#     @classmethod
#     def from_string(cls, s):
#         """从字符串初始化一个账号"""
#         try:
#             username, balance = s.split()
#             balance = decimal.Decimal(float(balance))
#         except ValueError:
#             raise CreateAccountError('input must follow pattern "{ACCOUNT_NAME} {BALANCE}"')

#         if balance < 0:
#             raise CreateAccountError('balance can not be negative')
#         return cls(username=username, balance=balance)


# def caculate_total_balance(accounts_data):
#     """计算所有账号的总余额
#     """
#     result = 0
#     for account_string in accounts_data:
#         try:
#             user = Account.from_string(account_string)
#         except CreateAccountError:
#             pass
#         else:
#             result += user.balance
#     return result


# accounts_data = [
#     'piglei 96.5',
#     'cotton 21',
#     'invalid_data',
#     'roland $invalid_balance',
#     'alfred -3',
# ]

# print(caculate_total_balance(accounts_data))


# 空对象模式简介
# 额外定义一个对象来表示None

# 好处
# （1）它可以加强系统的稳固性，能有有效地防止空指针报错对整个系统的影响，使系统更加稳定。
# （2）它能够实现对空对象情况的定制化的控制，能够掌握处理空对象的主动权。
# （3）它并不依靠Client来保证整个系统的稳定运行。
# （4）它通过isNone对==None的替换，显得更加优雅，更加易懂。
import decimal


class Account:
    """一个虚拟的银行账号"""

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    @classmethod
    def from_string(cls, s):
        """从字符串初始化一个账号"""
        try:
            username, balance = s.split()
            balance = decimal.Decimal(float(balance))
        except ValueError:
            # raise CreateAccountError('input must follow pattern "{ACCOUNT_NAME} {BALANCE}"')
            return NullAccount()

        if balance < 0:
            return NullAccount()
        return cls(username=username, balance=balance)


def caculate_total_balance(accounts_data):
    """计算所有账号的总余额
    """
    return sum(Account.from_string(s).balance for s in accounts_data)


class NullAccount:
    username = ""  # 当发生错误时username的值
    balance = 0  # 当发生错误时balance的值

    def re_Null():
        return NotImplementedError


accounts_data = [
    'piglei 96.5',
    'cotton 21',
    'invalid_data',
    'roland $invalid_balance',
    'alfred -3',
]

print(caculate_total_balance(accounts_data))
