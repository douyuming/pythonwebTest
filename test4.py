import random
def hongbao(total,num):
    i=0;
    while(i<num):
        if (i == num - 1):
            print('{0}:{1}'.format(i + 1,round( total,2)))
            break
        while(True):
            i_money=round(total*random.random(),2)
            if(i_money>=0.01):
                break
        total=total-i_money
        if(total/(num-i-1)<0.01):
            i=i-1
            total+=i_money
        else:
            print('{0}:{1}'.format(i+1,i_money))
        i=i+1
hongbao(1,10)
