#!/usr/bin/python
import sys
import math
import time
start_time = time.time()         #calculating start point

for b in sys.stdin:              #read from STDIN
   file=list(b)                  #split the string(line) in list
   STN=(''.join(file[0:6]))      #calculate the station number using the position and join them 
   MODA=(''.join(file[14:18]))   #calculate the MODA (month and date) using the position and join them  
   YEAR=(''.join(file[18:22]))   #calculate the YEAR using the position and join them
   TEMP=(''.join(file[24:30]))   
   if TEMP == "9999.9":                 #shows that it is missing
   	  TEMP="-9999.9"            #minimizing the missing values as we want this dimension to maximize
   DEWP=(''.join(file[35:41]))         #join the list
   if DEWP == "9999.9":                 #shows that it is missing
   	  DEWP="-9999.9"             #minimizing the missing values as we want this dimension to maximize
   SLP=(''.join(file[46:52]))
   if SLP == "9999.9":                   #shows that it is missing
   	  SLP="-9999.9"              #minimizing the missing values as we want this dimension to maximize
   MAX=(''.join(file[102:108]))
   if MAX == "9999.9":                     #shows that it is missing
   	  MAX="-9999.9"               #minimizing the missing values as we want this dimension to maximize
   STP=(''.join(file[57:63]))
   if STP == "9999.9":                      #shows that it is missing
   	  STP="99999.9"              #maximizing the missing values as we want this dimension to minimize
   WDSP=(''.join(file[78:83]))
   if WDSP == "999.9":                       #shows that it is missing
   	  WDSP="99999.9"             #maximizing the missing values as we want this dimension to minimize
   MXSPD=(''.join(file[88:93]))
   if MXSPD == "999.9":                      #shows that it is missing
   	  MXSPD="99999.9"            #maximizing the missing values as we want this dimension to minimize
   GUST=(''.join(file[95:100]))
   if GUST == "999.9":                        #shows that it is missing
   	  GUST="99999.9"             #maximizing the missing values as we want this dimension to minimize
   MIN=(''.join(file[110:116]))
   if MIN == "9999.9":                        #shows that it is missing
   	  MIN="99999.9"               #maximizing the missing values as we want this dimension to minimize
   key=[STN] #using station as a key
   values=[MODA]+[YEAR]+[TEMP]+[DEWP]+[SLP]+[MAX]+[STP]+[WDSP]+[MXSPD]+[GUST]+[MIN]	#values we are considering 
   print key, values
key_times="Mapper_time_in_seconds"
value_time=time.time()-start_time   #calculating final time
print [key_times], [value_time] #printing time key value pair
