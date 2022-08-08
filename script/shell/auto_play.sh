#!/bin/bash

TARGET_DIR_PATH=/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/cp/raspi-ubuntu-1
TARGET_FNAME=rec_0.wav

ERR_FILE_LIST_PATH=/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/out/err_file_list.csv

# エラーファイルリストの生成
id=0
echo "id,name" > $ERR_FILE_LIST_PATH
find $TARGET_DIR_PATH -type d -maxdepth 1 -mindepth 1 | sort | while read dir
do
    id=$(($id + 1))
    echo "${id},${dir##*/}" >> $ERR_FILE_LIST_PATH
done

id=0
find $TARGET_DIR_PATH -type d -maxdepth 1 -mindepth 1 | sort | while read dir
do
    # idに1加算
    id=$(($id + 1))
    # id判定
    if [ $id -le 0 ]; then
        continue
    fi

    # idとディレクトリ名の一部を表示する
    echo id: ${id}, ${dir##*/}

    # 音声の再生
    fpath=$dir/$TARGET_FNAME
    afplay $fpath

    # エラーを記録する
    # ファイルディスクリプションの問題で動かない
    # read -t 3 -p "Is there an error? :" str
    # echo $str
done