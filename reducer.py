#!/usr/bin/python
import sys
import math
import time
from operator import itemgetter
start_time = time.time()            #reducer start time   
def reducer_function(data):         #sequential algorithm for skyline computation
  head=0
  tail=len(data)-1
  while head<tail+1 :
      i=head+1

      while i<=tail:
          if data[head][1][2]+data[head][1][3]+data[head][1][4]+data[head][1][5]>data[i][1][2]+data[i][1][3]+data[i][1][4]+data[i][1][5] and data[head][1][6]+data[head][1][7]+data[head][1][8]+data[head][1][9]+data[head][1][10]<data[i][1][6]+data[i][1][7]+data[i][1][8]+data[i][1][9]+data[i][1][10]:
              data[i]=data[tail]
              tail=tail-1
          elif data[i][1][2]+data[i][1][3]+data[i][1][4]+data[i][1][5]>data[head][1][2]+data[head][1][3]+data[head][1][4]+data[head][1][5] and data[i][1][6]+data[i][1][7]+data[i][1][8]+data[i][1][9]+data[i][1][10]<data[head][1][6]+data[head][1][7]+data[head][1][8]+data[head][1][9]+data[head][1][10]:    
              data[head]=data[i]
              data[i]=data[tail]
              tail=tail-1
              i=head+1
          else:
              i=i+1

      if head<tail+1:
          head=head+1

  return data[0:head]



    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def merge(a,b):                 #merge previous and current skyline to calculate local skyline
  return reducer_function(a+b)
#hadoop reducer function
current_key = 0
key = None
answer=[]                         
local_skyline_merge=[]            #initialize empty local skyline in starting

# input comes from STDIN
for line in sys.stdin:

    # remove leading and trailing whitespace 
    # parse the input we got from mapper.py
    line=line.strip()
    line = line.replace(',', '')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace("'", '')
    line=line.split()
    key= line[0]
    values= line[1:]
    
       
        

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: STN) before it is passed to the reducer
    if current_key == key:
        answer.append([key, values])
    else:
        if current_key:
            # write result to STDOUT
            local_skyline_merge= merge(local_skyline_merge,answer)
            answer=[]
        answer.append([key, values])
        current_key = key

    
    #print mapper_time_block as (answer)
  
if current_key==key:   # last bucket of mapper output has mapper time only so just print it
  print answer
  global_skyline=local_skyline_merge
    # convert count (currentliney a string) to int
  unique_key=[]  
  for point in range(len(global_skyline)):   #printing only STN, YEAR and MODA
      print ([global_skyline[point][0], global_skyline[point][1][0], global_skyline[point][1][1]])
   

key_times="Reducer_time"
value_time=time.time()-start_time   # FINAL REDUCER TIME
print [key_times], [value_time]     #printing Reducer time