import string
text = str(input("type a sentence:\n"))
punc = ''',.'''
for ele in text:
    if ele in punc:
        text = text.replace(ele, "")
table = text.split()
longest = ""
for x in table:
    if len(x) > len(longest):
        longest = x
print("the longest word is:", longest,"\n")
