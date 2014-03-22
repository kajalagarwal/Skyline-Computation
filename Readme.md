#mapper and reducer
Finding the skyline on dataset with multiple dimensions


This code is generating skyline for the  data set points collected by different station for different dimensions. 
FURTHER INFORMATION ON DATA SET CAN BE SEEN HERE #http://www.ncdc.noaa.gov/cgi-bin/res40.pl?page=gsod.html
In my code i am calculating skyline on TEMP, DEWP, SLP, MAX, STP, WDSP, MXSPD, GUST, MIN.
I am maximizing the attributes TEMP, DEWP, SLP, MAX and minimizing STP, WDSP, MXSPD, GUST and MIN.

We are using standard sequential skyline algorithm for the computation of skyline.
#code running direction

copy the mapper and reducer file named as mapper.py and reducer.py on your hadoop cluster.
#copy input file at hdfs
hadoop fs -copyFromLocal data.out    

#Deploy command for the map/reduce code 
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.5.0.jar -mapper ./mapper.py -reducer ./reducer.py -input data.out -output output -file mapper.py -file reducer.py

#multiple reducer
You can also increase the task for the reducer in your hadoop cluster as 
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.5.0.jar -D mapred.reduce.tasks=16 ....
you can also copy the above command in a shell script, so just need to run ./command_file_name.

#hadoop Output
you can check your output in file named as output in your hadoop cluster 

#Running time
we are also calculating here running time for both mapper and reducer separately.

