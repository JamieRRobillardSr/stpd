l1 = [ "The",  "fox",  "jumped",  "over",  "the",  "fence",  "." ]
s1 = ""

for word in l1:
    if (word == "."):
        s1 = s1.strip()
        s1 += word
    else:
        s1 += word + " "

print(s1)
