# !/usr/bin/env python3
# coding: utf-8

import cis

def FetchFeaturesFromDataset(DATASET_PATH: str = '../dataset'):
    '''
    データセットの音声データから特徴量を抽出する関数

    Parameters
    ----------
    DATASET_PATH : str, default '../dataset'
        datasetへのpath

    Returns
    -------
    None
    '''

    ####################
    ### 各種パラメータ ###
    ####################

    # 被験者
    participants = ['s' + str(i) for i in range(1, 11)]
    # 発言
    utterances = ['recording' + str(i) for i in range(2)]
    # セッション
    sessions = ['trial1', 'trial2']
    # 部屋
    rooms = ['upstairs', 'downstairs']
    # 設置場所
    placements = ['wall', 'nowall']
    # ユーザとの距離
    distances = [str(i) for i in range(1, 6, 2)]
    # 極座標
    positions = []
    for i, d in enumerate(['A', 'B', 'C']):
        for p in range(0, 3):
            positions.append(d + str(p) + '_' + str(2*i+1) + '_' + str(45*p))
    # DoV angles
    angles = [str(i) for i in range(0, 360, 45)]
    # マイクチャンネル
    mic_channels = range(1, 5)

    #########################
    ### 各種特徴量を取得する ###
    #########################

    # ファイルのフェッチ
    id = 0
    file_paths = []
    for participant_id in participants:
        first_dir_name = participant_id
        for room_id in rooms:
            for device_placement_id in placements:
                for session_id in sessions:
                    second_dir_name = participant_id + '_' + room_id + \
                        '_' + device_placement_id + '_' + session_id
                    for polar_position_id in positions:
                        third_dir_name = polar_position_id
                        for utterance_id in utterances:
                            for dov_angle in angles:
                                # channel 0: 音声認識用に加工されている。channnel 5: 再生されたデータ→ch1~4を使用する
                                for mic_channel in mic_channels:
                                    filename = utterance_id + '_' + dov_angle + \
                                        '_' + str(mic_channel) + '.wav'
                                    file_path = DATASET_PATH + '/' + first_dir_name + '/' + \
                                        second_dir_name + '/' + third_dir_name + '/' + filename

                                    file_paths.append(file_path)

                                    v, fs = cis.wavread(file_path)

                                    if(id % 100 == 0):
                                      print(f'count: {id}')

                                    id = id + 1
    return file_paths
