#!/bin/bash

# while read line
# do
#   echo $line

#   cmd1 = 'git rm --cached --ignore-unmatch '
#   cmd = $cmd1$line
#   git filter-branch --force --index-filter $(eval ${cmd}) --prune-empty --tag-name-filter cat -- --all
# done < ~/Desktop/lfs_files.txt

git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no0" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no1" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no2" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no3" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no4" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no5" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no6" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no7" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no8" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch out/2021-11-16_no9" --prune-empty --tag-name-filter cat -- --all
