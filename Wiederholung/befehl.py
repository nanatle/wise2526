s = "Hello World"

s.lower()      # 'hello world'
s.upper()      # 'HELLO WORLD'
s.capitalize() # 'Hello world'
s.title()      # 'Hello World'
s.swapcase()   # 'hELLO wORLD'

s = "Hello123"
s.isalpha()    # False (chỉ chữ cái mới True)
s.isdigit()    # False
s.isalnum()    # True (chữ + số)
s.islower()    # False
s.isupper()    # False
s.isspace()    # False
s.startswith("He")  # True
s.endswith("123")   # True
s = "banana"

s.count("a")     # 3
s.find("na")     # 2 (vị trí đầu tiên, không có trả -1)
s.index("na")    # 2 (không có sẽ báo lỗi)
s = "I like apple"

s.replace("apple", "banana")
# 'I like banana'
s = "apple,banana,orange"

s.split(",")
# ['apple', 'banana', 'orange']
lst = ["apple", "banana", "orange"]

",".join(lst)
# 'apple,banana,orange'

s = "  hello  "

s.strip()    # 'hello'
s.lstrip()   # 'hello  '
s.rstrip()   # '  hello'
s = "Python"

s[0]      # 'P'
s[-1]     # 'n'
s[0:4]    # 'Pyth'
s[:3]     # 'Pyt'
s[::2]    # 'Pto'

name = "Anna"
age = 20

f"My name is {name}, I am {age} years old"
"My name is {} and I am {}".format(name, age)

len("hello")  # 5
str(123)   # '123'