import re

reg = r"(^(?=.*[*.!@$%#]).{8,50})"

pattern = re.compile(reg)

password = 'hj@khjsdgjh'

res = pattern.search(password)
print(res)

if res:
    print("Valid Password")
else:
    print("Invalid Password")
