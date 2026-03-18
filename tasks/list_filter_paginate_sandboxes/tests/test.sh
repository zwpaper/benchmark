#!/bin/bash

REWARD=1

pytest /tests/test_outputs.py -v
if [ $? -ne 0 ]; then
  REWARD=0
fi

mkdir -p /logs/verifier
echo $REWARD > /logs/verifier/reward.txt
