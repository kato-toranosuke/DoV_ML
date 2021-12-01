#!/bin/bash

# while read line
# do
#   echo $line

#   cmd1 = 'git rm --cached --ignore-unmatch '
#   cmd = $cmd1$line
#   git filter-branch --force --index-filter $(eval ${cmd}) --prune-empty --tag-name-filter cat -- --all
# done < ~/Desktop/lfs_files.txt

git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch ../out/ml_model_result/ExtraTreesClassifier_2021-10-31_no1/ExtraTreesClassifier_2021-10-31_no1.pkl" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch ../out/ml_model_result/ExtraTreesClassifier_2021-11-01_no1/ExtraTreesClassifier_2021-11-01_no1.pkl" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch ../out/ml_model_result/ExtraTreesClassifier_NoResampler_2021-11-27_no0/ExtraTreesClassifier_NoResampler_2021-11-27_no0.pkl" --prune-empty --tag-name-filter cat -- --all
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch ../out/ml_model_fitting_result/ExtraTreesClassifier_ClusterCentroids_2021-11-04_no0.sav" --prune-empty --tag-name-filter cat -- --all