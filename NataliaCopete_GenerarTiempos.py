import numpy as np
import matplotlib.pyplot as plt



def fibonacci(N):
  if (N==0 or N==1):
    return N
  else:
    return fibonacci(N-2)+fibonacci(N-1)


def get_time(N):
   import time
   t0 = time.time()
   fibonacci(N)
   t1 = time.time()-t0
   return t1

for i in range(0,40):

  print(i,get_time(i))



