#!/bin/zsh

# ロボットの数
N=5
# 日付
DATE="2022-03-23"
# path
DATA_PATH="/Users/toranosuke/Desktop/data/raspi-ubuntu-"
OUT_PATH="/Users/toranosuke/Desktop/data/out"
CP_PATH="/Users/toranosuke/Desktop/data/cp"

mkdir -p $CP_PATH
# output lists of files
for i in `seq 1 $N`
do
    echo "$DATA_PATH$i"
    # -Fで区切り文字を指定。NFで最後のセクションを指定。
    find $DATA_PATH$i -name "$DATE*" | awk -F/ '{print $NF}' > "$OUT_PATH/raspi-ubuntu-$i.txt"
    # コピー先ディレクトリに全ファイルをコピー
    # cp -r "$DATA_PATH$i" "$CP_PATH/raspi-ubuntu-$i"
done

# generate the deleted file list(empty file)
all_del_file_list="all-del-file-list.txt"
echo -n >| "$OUT_PATH/$all_del_file_list"

# differentiate the lists
for i in `seq 1 $(($N-1))`
do
    for j in `seq $(($i+1)) $N`
    do
        # 追加分・削除分のみ抽出
        del_file_list="del-file-list-$i-$j.txt"
        diff -u "$OUT_PATH/raspi-ubuntu-$i.txt" "$OUT_PATH/raspi-ubuntu-$j.txt" | grep -e ^+ -e ^- | grep -v -e ^+++ -e ^--- | sed s/^-// | sed s/^+// > "$OUT_PATH/$del_file_list" >> "$OUT_PATH/$all_del_file_list"
    done
done

# ユニークな行をまとめる
uniq_all_del_list=`sort $OUT_PATH/$all_del_file_list | uniq`
echo $uniq_all_del_list > "$OUT_PATH/$all_del_file_list"

# 上記ファイルをもとに削除
# for i in `seq 1 $N`
# do
#     cat $OUT_PATH/$all_del_file_list | while read dir
#     do
#         # -f: 存在しないファイルでも警告しない
#         rm -rf $CP_PATH/raspi-ubuntu-$i/$dir
#     done
# done

# renumbering
for i in `seq 1 $N`
do
    sorted_list=`find $CP_PATH/raspi-ubuntu-$i -type d -maxdepth 1 -mindepth 1 | sort`
    echo $sorted_list | while read file
    do
        # trial noの取得
        echo $file
    done
done