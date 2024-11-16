import math
bin=int(input(),2)
ans=0 if bin<=1 else int(math.log2(bin-1))+1