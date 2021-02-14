#wordcount
text="hai hello hai hello"
#op=hai=2 hello=2
words=text.split("")
dict={}
for word in words
    if (word not in dict)
        dict[word]=1
    else
        dict[word]+=1
print(dict)