#!/bin/sh
if [ -z "$1" ]; then
    echo 'Please provide test image path as an argument' 
    exit 1
fi
#result=$(curl -F 'imagefile=@'$1'' http://127.0.0.1:8888/classification --silent)
#result=$(curl -F 'imagefile=@'$1'' http://ec2-13-232-211-181.ap-south-1.compute.amazonaws.com:8888/classification --silent)
result=$(curl -F 'imagefile=@'$1'' https://classificationmayank.herokuapp.com/classification --silent)
echo "$result"
