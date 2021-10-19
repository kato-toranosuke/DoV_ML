function row = GetRowData(dir_path, attr, gp_tdoa_mic_channels, tlength)
%function GetRowData(dir_path, attr, gp_tdoa_mic_channels, tlength)
    %%%%%%%%%%%%%%%%%%%
    % GCC-PHAT & TDOA %
    %%%%%%%%%%%%%%%%%%%

    % channel1~4の音声データを読み込む
    voice_data = cell(length(gp_tdoa_mic_channels), 2);
    for ch = gp_tdoa_mic_channels
        fname = attr('utterance_id') + "_" + attr('dov_angle') + "_" + ch + ".wav";
        fpath = dir_path + '/' + fname;
        [v_, fs_] = audioread(fpath);
        voice_data(ch,:) = {v_, fs_};
    end

    % 各ペアについて計算
    mic_ch_pairs = nchoosek(gp_tdoa_mic_channels, 2);
    % GCC-PHATの特徴量を格納する配列を生成
    pair_gp_tdoa_features = zeros(length(mic_ch_pairs), 4);
    
    for i = 1:length(mic_ch_pairs)
        % マイクのチャンネル
        mic_ch1 = mic_ch_pairs(i, 1);
        mic_ch2 = mic_ch_pairs(i, 2);

        % 音声データを取得
        v1 = voice_data{mic_ch1, 1};
        v2 = voice_data{mic_ch2, 1};

        % サンプリング周波数を取得
        fs = voice_data{mic_ch1, 2};

        % GCC-PHATとTDOAを計算
        [tau, R, lag] = gccphat(v1, v2, fs);

        % ピークを検出
        [M, I] = max(R);
        M = abs(M);

        % ピークからtlength[sec]だけ切り出す
        dt = 1.0/fs;
        % 切り出す範囲のインデックスを計算
        delta_ix = floor(tlength/dt);
        start_ix = I - delta_ix;
        end_ix = I + delta_ix;
    
        % 範囲外のインデックスに対する処理
        if start_ix < 1
            start_ix = 1;
        end
        if end_ix > length(R)
            end_ix = len(data);
        end

        % 曲線下面積を求める
        index = [start_ix:end_ix];
        val = R(index);
        auc = sum(dt*abs(val));

        % 配列に格納する（最大ピーク値、チャンネル間遅延、曲線下面積、TDOA）
        pair_gp_tdoa_features(i, :) = [M lag(I) auc tau];
    end

    % 標準偏差、範囲、最小値、最大値、平均を求める
    gp_tdoa_features = [];
    for i = 1:4
        vals = pair_gp_tdoa_features(:, i);
        std_val = std(vals);
        max_val = max(vals);
        min_val = min(vals);
        range_val = max_val - min_val;
        mean_val = mean(vals);
    
        gp_tdoa_features(5*(i-1)+1:5*i) = [std_val range_val min_val max_val mean_val];
    end

    %%%%%%%%%%%%%%%
    %%% 属性情報 %%%
    %%%%%%%%%%%%%%%
    filename = attr('utterance_id') + "_" + attr('dov_angle') + "_" + attr('mic_channel') + ".wav";
    file_path = dir_path + '/' + filename;
    meta_data = [attr('id'), filename, attr('participant_id'), attr('room_id'), attr('device_placement_id'), attr('session_id'), attr('polar_position_id'), attr('distance'), attr('polar_angle'), attr('utterance_id'), attr('dov_angle'), attr('mic_channel')];

    % 行情報を生成
    row = [meta_data, gp_tdoa_features];

    fprintf('id: %s, file path: %s\n', attr('id'), file_path);
end