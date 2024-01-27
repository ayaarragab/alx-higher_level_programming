#!/bin/bash
# comment explains everything ISA
curl -sI "$1" -o text && content_length=$(grep -i '^Content-Length:' text | awk '{print $2}') && echo $content_length
