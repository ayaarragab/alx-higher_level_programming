#!/bin/bash
# display exit code
curl -I -s $1 -o /dev/null -w "%{http_code}"
