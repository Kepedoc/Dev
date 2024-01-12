import string
text = input("type a sentence:\n")
punc = ',.'
for x in text:
    if x in punc:
        text = text.replace(x, " ")
table = text.split()
longest = ""
for x in table:
    if len(x) > len(longest):
        longest = x
print("the longest word is:", longest,"\n")
