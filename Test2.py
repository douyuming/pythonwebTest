import sys
import math
while 1:
    D=input()
    V=input()
    if D == 0 and V == 0:
        break;
    print (1/6*(math.pi)*(D*D*D-V*V*V))