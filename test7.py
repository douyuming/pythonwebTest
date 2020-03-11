import jieba
def getDicAndInput():
    dic=[]
    input_=""
    flag=True
    file=open("Exp.txt","rt")
    for line in file:
        if(line=='DICTIONARY_DEFINE_OVER\n'):
            flag=False
            continue
        if(flag):
            dic.extend(line.split())
        else:
            input_=input_+line
    return input_,dic
getDicAndInput()
str=""
dic=[]
str,dic=getDicAndInput()
ls = jieba.lcut(str)
for i in range(len(ls)):
    if (len(ls[i]) >= 2):
        for char in dic:
            if (char[0] == ls[i][0] and char[-1] == ls[i][-1] and len(char) == len(ls[i])):
                ls[i] = char
                i = i + 1
                break
    i = i + 1;
str = ""
for word in ls:
    str = str + word;
print(str)
