import random
def function():
    x=0.0
    y=0.0
    sum=10000000
    inner=0
    for i in range(sum):
        x=random.random();
        y=random.random();
        if(y<=pow(x,2)):
            inner=inner+1
    return inner/sum
print(function())

