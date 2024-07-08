#!/usr/bin/env bash
file="."
msg="commit message"
if [$# >= 2]; then
    file=$1
    msg=$2
fi
git add $file
git commit -m msg
git push
