#!/usr/bin/env bash
file="."
msg="msg"
if [ $# -ge 2 ]; then
    file=$1
    msg=$2
fi
git add "$file"
git commit -m "$msg"
git push
