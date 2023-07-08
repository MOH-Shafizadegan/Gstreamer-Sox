#!/bin/bash

duration=$1
threshold=$2
date=$(date +%Y-%m-%d-%H-%M-%S)

rm -f static/*.wav
rm -f result.txt

# Record audio from microphone for 10 seconds and save it as input.wav
sox -d static/input$date.wav trim 0 $duration

# Get the maximum amplitude of input.wav in dBFS (decibels relative to full scale)
rms_amp=$(sox static/input$date.wav -n stats : newfile : restart 2>&1 | grep 'RMS lev dB' | awk ' { print $4 }' )

echo $rms_amp
# Compare the maximum amplitude with the threshold and print the result
if [ $(echo "$rms_amp < $threshold" | bc -l) -eq 1 ]; then
  echo "The sound level $rms_amp is below the threshold $threshold" > result.txt
else
  echo "The sound level $rms_amp above or equal to the threshold $threshold" > result.txt
fi

