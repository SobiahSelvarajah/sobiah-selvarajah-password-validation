import re

reg = r"[a-zA-Z0-9$%#@]{8,}\d$"

pattern = re.compile(reg)

password = 'hj3@khjsgjhhhjdg6'

res = pattern.search(password)
print(res)

if res:
    print("Valid Password")
else:
    print("Invalid Password")
