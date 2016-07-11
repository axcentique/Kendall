#!/bin/bash
#
# Find the correct Physio data for 4D data set
# Uses sls_extractphysio to get cardiac and respiration files
# 
#


if [ $# -lt 4 ]
then
  echo "Usage: sls_findphysio subjectid scantype scantime occasion"
  echo "<scantype> = REST, TASK, NBACK1, or NBACK2 <scantime>= seconds"
  echo "occasion = 1,2,3 or 4"
  echo "Assumes SLS folder structure beneath timepoint"
  echo "Finds correct physio file and extracts cardiac and resp data into files"
  echo "Run in folder which contains subject folder"
  exit 1
fi

inputfile=$1
scantime=$2
subjectid=$3
scantype=$4

# Call sls_extractphysio to create cardiac and resp files
/mnt/home/gpauley/sls_extractphysio ${inputfile} ${scantime} > physiooutput.txt
awk '{print $5}' physiooutput.txt > ${subjectid}_${scantype}_cardio.txt
awk '{print $6}' physiooutput.txt > ${subjectid}_${scantype}_resp.txt
rm -f physiooutput.txt



