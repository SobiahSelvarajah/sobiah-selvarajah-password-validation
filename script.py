import re

reg = r"(^(?=.*[*.!@$%#]).{8,})"

pattern = re.compile(reg)

password = 'hj@khjs8746382gjh'

res = pattern.search(password)
print(res)

if res:
    print("Valid Password")
else:
    print("Invalid Password")
