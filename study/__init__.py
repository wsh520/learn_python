# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# a =L[0:3]
# print(a)
# b = L[-2:]
# print(b)
# """ 数组操作 """
# q = list(range(100))
# # for i in q:
# #     print(i)
# ''' 分片 '''
# ''' 第11 到最后一个 '''
# print(q[10:])
# ''' 前十个 '''
# print(q[:10])
# ''' 倒数10个 '''
# print(q[-10:])
# ''' 从后向前 '''
# print(q[:-10])
# ''' 所有数，每5个取一个 '''
# print(q[::5])
# ''' 前十个数，没隔两个取一个 '''
# print(q[:10:2])
# ''' 复制list '''
# print(q[:])

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Bob']
# ]
# # Apple
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Bart:
# print(L[2][1])


# tuple1 = (1,2,3,4,5)
# print(tuple1)
#
# # 分片 取 前三个
# print(tuple1[:3])
# # 2 ~ end
# print(tuple1[1:])
# # 1~3
# print(tuple1[1:3])
# # 倒序1-4
# print(tuple1[:-1])
# # 复制 tuple
# print(tuple1[:])
# # 所有数 每隔2个取一个数
# print(tuple1[::2])
#
# def trim1(s):
#     # 使用切片移除字符串两端的空白字符
#     return s.lstrip().rstrip()
#
# def trim(s):
#     # 查找第一个非空格字符的位置
#     start = 0
#     while start < len(s) and s[start] == ' ':
#         start += 1
#
#     # 查找最后一个非空格字符的位置
#     end = len(s) - 1
#     while end >= 0 and s[end] == ' ':
#         end -= 1
#
#     # 使用切片提取子字符串
#     return s[start:end + 1]
#
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# 类似Java的 switch case
# score = 'B'
#
# match score:
#     case 'A':
#         print('score is A.')
#     case 'B':
#         print('score is B.')
#     case 'C':
#         print('score is C.')
#     case _: # _表示匹配到其他任何情况
#         print('score is ???.')

# age = 9
#
# match age:
#     # case x if x < 10表示当age < 10成立时匹配，且赋值给变量x
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')

# args = ['gcc', 'hello.c', 'world.c', '-o', 'a.out']
args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件: case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')