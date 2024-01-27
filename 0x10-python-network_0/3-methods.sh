#!/bin/bash
# option request
curl -sI "$1" | grep -i '^allow:' | cut -d' ' -f2-
