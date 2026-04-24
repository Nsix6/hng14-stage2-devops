#!/bin/bash
set -e

timeout 60 bash -c '
  JOB=$(curl -s -X POST http://localhost:3000/submit | jq -r .job_id)

  for i in {1..15}; do
    STATUS=$(curl -s http://localhost:3000/status/$JOB | jq -r .status)
    if [ "$STATUS" = "completed" ]; then
      exit 0
    fi
    sleep 3
  done

  exit 1
'