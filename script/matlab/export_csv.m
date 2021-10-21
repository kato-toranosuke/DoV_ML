% ヘッダー行を追加する
header_attr = ["id" "filename" "participant_id" "room_id" "device_placement_id" "session_id" "polar_position_id" "distance" "polar_angle" "utterance_id" "dov_angle" "mic_channel"];
% マルチチャンネルver
header_gp_tdoa_multich = ["gp_max_val_ch1" "gp_max_ix_ch1" "gp_auc_ch1" "tdoa_ch1" "gp_max_val_ch2" "gp_max_ix_ch2" "gp_auc_ch2" "tdoa_ch2" "gp_max_val_ch3" "gp_max_ix_ch3" "gp_auc_ch3" "tdoa_ch3" "gp_max_val_ch4" "gp_max_ix_ch4" "gp_auc_ch4" "tdoa_ch4"];
header_multich = horzcat(header_attr, header_gp_tdoa_multich);

csv_fname_mutich = "../../out/matlab/test_multich.csv";
writematrix(header_multich, csv_fname_mutich);

% シングルチャンネルver
header_gp_tdoa_monoch = ["gp_max_val_std" "gp_max_val_range" "gp_max_val_min" "gp_max_val_max" "gp_max_val_mean" "gp_max_ix_std" "gp_max_ix_range" "gp_max_ix_min" "gp_max_ix_max" "gp_max_ix_mean" "gp_auc_std" "gp_auc_range" "gp_auc_min" "gp_auc_max" "gp_auc_mean" "tdoa_std" "tdoa_range" "tdoa_min" "tdoa_max" "tdoa_mean"];
header_monoch = horzcat(header_attr, header_gp_tdoa_monoch);

csv_fname_monoch = "../../out/matlab/matlab_gp_monoch.csv";
writematrix(header_monoch, csv_fname_monoch);

% ファイルアクセスの為の各種パラメータ
% 被験者
participant_ids = "s" + [1:10];
% 発言
utterance_ids = "recording" + [0:1];
% セッション
session_ids = ["trial1" "trial2"];
% 部屋
room_ids = ["upstairs" "downstairs"];
% 設置場所
device_placement_ids = ["wall" "nowall"];
% ユーザ距離
distance_ids = ["A" "B" "C"];
% ユーザ極座標
polar_angle_ids = [0 1 2];
% DoV angles
dov_angles = [0:45:315];
% GCC-PHAT, TDOA以外の計算に用いるマイクチャンネル(音声認識用に使用しているchannel0のみ特徴量抽出に利用する。)
mic_channel = 0;
% GCC-PHAT, TDOAの計算に用いるマイクチャンネル
gp_tdoa_mic_channels = [1:4];

%%%%%%%%%%%%
% Constant %
%%%%%%%%%%%%

% ファイルにアクセス
% データセットへのパス
DATASET_PATH = "../../../dataset";
% 出力ファイルへのパス
OUTPUT_PATH = "../../out/";
% ピークから切り出す秒数
tlength = 0.000236;
% id
id = 0;
for participant_id = participant_ids
    % 第1階層
    first_dir_name = participant_id;
    for room_id = room_ids
        for device_placement_id = device_placement_ids
            for session_id = session_ids
                % 第2階層
                second_dir_name = participant_id + '_' + room_id + '_' + device_placement_id + '_' + session_id;

                for distance_ix = 1:length(distance_ids)
                    distance_id = distance_ids(distance_ix);

                    for polar_angle_ix = 1:length(polar_angle_ids)
                        polar_angle_id = polar_angle_ids(polar_angle_ix);
                        polar_position_id = distance_id + polar_angle_id;
                        distance = 2*(distance_ix - 1) + 1;
                        polar_angle = 45*(polar_angle_ix-1);
                        % 第3階層
                        third_dir_name = polar_position_id + '_' + distance + '_' + polar_angle;

                        for utterance_id = utterance_ids
                            % 一度に書き込む行範囲（特徴量をまとめる配列）
                            rows = [];

                            for dov_angle = dov_angles
                                % 音声ファイルが格納されているディレクトリまでのパス
                                dir_path = DATASET_PATH + '/' + first_dir_name + '/' + second_dir_name + '/' + third_dir_name;
                                
                                % 属性値を格納する辞書の作成
                                keySet = {'id', 'participant_id', 'room_id', 'device_placement_id', 'session_id', 'polar_position_id', 'distance', 'polar_angle', 'utterance_id', 'dov_angle', 'mic_channel'};
                                valueSet = [id participant_id room_id device_placement_id session_id polar_position_id distance polar_angle utterance_id dov_angle mic_channel];
                                attr = containers.Map(keySet, valueSet);

                                % 特徴量の計算
                                row = GetRowData(dir_path, attr, gp_tdoa_mic_channels, tlength);

                                % CSVに書き込む（追加）
                                writematrix(row, csv_fname_monoch,"WriteMode","append");

                                id = id + 1;
                            end

                        end
                    end
                end
            end
        end
    end
end