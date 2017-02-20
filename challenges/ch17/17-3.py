import re

exp = ".oo"
msg = "The ghost that says boo haunts the loo."

result = re.findall(exp,  msg)
print(result)


