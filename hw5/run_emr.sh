#!/bin/bash
MAPPER=$(basename $1)
REDUCER=$(basename $2)
INPUT=$3
OUTPUT=$4
LOCAL_OUTPUT=$5
STREAMING_JAR=/usr/lib/hadoop/hadoop-streaming.jar
hadoop fs -rm -r -skipTrash "${OUTPUT}"
hadoop jar ${STREAMING_JAR} \
    -D mapred.job.name='BDM_Lab5' \
    -D mapred.map.tasks=2 \
    -files "${MAPPER}","${REDUCER}" \
    -mapper "${MAPPER}" \
    -reducer "${REDUCER}" \
    -input "${INPUT}" \
    -output "${OUTPUT}" \
    -numReduceTasks 1

if [ ! -z "${LOCAL_OUTPUT}" ]; then
    rm -f "${LOCAL_OUTPUT}"
    hadoop fs -getmerge "${OUTPUT}/part*" "${LOCAL_OUTPUT}"
fi
