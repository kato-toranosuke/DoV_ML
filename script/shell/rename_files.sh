#!/bin/zsh

# ロボットの数
N=5
# 日付
DATE="2022-03-23"
# path
DATA_PATH="/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/raspi-ubuntu-"
OUT_PATH="/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/out"
CP_PATH="/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/cp"
# file name
DEL_LIST="all-del-file-list.txt"

for i in `seq 1 $N`
do
    cd $CP_PATH/raspi-ubuntu-$i
    rename -s 1m_0 1m_30 $DATE-standup-AGC-30deg_1m_0_trial*
done

# for i in `seq 1 $N`
# do
#     cd $CP_PATH/raspi-ubuntu-$i

#     mv 2022-03-23-standup-AGC-15deg_1m_60_trial26 2022-03-23-standup-AGC-15deg_1m_60_trial11

#     mv 2022-03-23-standup-AGC-15deg_3m_105_trial26 2022-03-23-standup-AGC-15deg_3m_105_trial1
#     # mv 2022-03-23-standup-AGC-15deg_3m_105_trial32 2022-03-23-standup-AGC-15deg_3m_105_trial27

#     # mv 2022-03-23-standup-AGC-15deg_3m_120_trial32 2022-03-23-standup-AGC-15deg_3m_120_trial30
#     # mv 2022-03-23-standup-AGC-15deg_3m_120_trial33 2022-03-23-standup-AGC-15deg_3m_120_trial31

#     mv 2022-03-23-standup-AGC-15deg_3m_75_trial26 2022-03-23-standup-AGC-15deg_3m_75_trial17
#     mv 2022-03-23-standup-AGC-15deg_3m_75_trial27 2022-03-23-standup-AGC-15deg_3m_75_trial8

#     mv 2022-03-23-standup-AGC-15deg_5m_75_trial26 2022-03-23-standup-AGC-15deg_5m_75_trial11

#     mv 2022-03-23-standup-AGC-30deg_1m_120_trial26 2022-03-23-standup-AGC-30deg_1m_120_trial7

#     mv 2022-03-23-standup-AGC-30deg_1m_150_trial26 2022-03-23-standup-AGC-30deg_1m_150_trial18
#     mv 2022-03-23-standup-AGC-30deg_1m_150_trial27 2022-03-23-standup-AGC-30deg_1m_150_trial7

#     mv 2022-03-23-standup-AGC-30deg_3m_120_trial26 2022-03-23-standup-AGC-30deg_3m_120_trial3
#     # mv 2022-03-23-standup-AGC-30deg_3m_120_trial32 2022-03-23-standup-AGC-30deg_3m_120_trial30

#     mv 2022-03-23-standup-AGC-30deg_3m_30_trial26 2022-03-23-standup-AGC-30deg_3m_30_trial20

#     mv 2022-03-23-standup-AGC-30deg_3m_60_trial26 2022-03-23-standup-AGC-30deg_3m_60_trial15
#     mv 2022-03-23-standup-AGC-30deg_3m_60_trial27 2022-03-23-standup-AGC-30deg_3m_60_trial4

#     # mv 2022-03-23-standup-AGC-30deg_3m_90_trial31 2022-03-23-standup-AGC-30deg_3m_90_trial30

#     mv 2022-03-23-standup-AGC-30deg_5m_120_trial26 2022-03-23-standup-AGC-30deg_5m_120_trial14
#     mv 2022-03-23-standup-AGC-30deg_5m_120_trial27 2022-03-23-standup-AGC-30deg_5m_120_trial20

#     mv 2022-03-23-standup-AGC-30deg_5m_150_trial26 2022-03-23-standup-AGC-30deg_5m_150_trial15
#     mv 2022-03-23-standup-AGC-30deg_5m_150_trial27 2022-03-23-standup-AGC-30deg_5m_150_trial22

#     mv 2022-03-23-standup-AGC-30deg_5m_60_trial26 2022-03-23-standup-AGC-30deg_5m_60_trial4

#     mv 2022-03-23-standup-AGC-30deg_5m_90_trial26 2022-03-23-standup-AGC-30deg_5m_90_trial16
#     mv 2022-03-23-standup-AGC-30deg_5m_90_trial27 2022-03-23-standup-AGC-30deg_5m_90_trial17
# done