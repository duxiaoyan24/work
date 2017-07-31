#!/bin/bash

InputDataPath=/tmp/duxiaoyan/redis
times=13

total_count=`hadoop fs -du -h ${InputDataPath} | wc -l`
batch_size=$(($total_count/$times+1))

echo $total_count
echo $batch_size

hadoop fs -du -h ${InputDataPath} > paths_all
for((i=1;i<=${times};i++))
do
    paths_tmp=`python batch.py 2 ${batch_size} ${i}`
    echo $paths_tmp

    # [self code]
done


