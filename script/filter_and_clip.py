import wave as wave
import numpy as np
import scipy.signal as sp
from librosa import times_like, feature
import os
import glob
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from mylib.cis import wavread, wavwrite

# 閾値以下の音声区間の抽出
# start time, end timeを返す
def clipWaveByDB(wave, times, th_dB):
    start_idx, end_idx = -1, -1
    for i in range(0, len(wave)):
        if wave[i] >= th_dB:
            start_idx = i
            break

    for i in range(len(wave) - 1, -1, -1):
        if wave[i] >= th_dB:
            end_idx = i
            break

    start_t = times[start_idx]
    end_t = times[end_idx]
    return (start_t, end_t)

# time -> index
def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return (list[idx], idx)

def cnvTimeToIdx(times, start_t, end_t):
    _, start_idx = getNearestValue(times, start_t)
    _, end_idx = getNearestValue(times, end_t)
    return (start_idx, end_idx)

# ウィナーフィルター
def wiener(wave, fs, s_t, e_t, alpha=1.0, mu=10):
    # 短時間フーリエ変換を行う
    hz_list, t, stft_data = sp.stft(
        wave, fs=fs, window='hann', nperseg=512, noverlap=384)
    # 入力信号の振幅を取得
    amp = np.abs(stft_data)
    # 入力信号のパワー取得
    input_power = np.power(amp, 2.0)

    # 雑音のパワーを推定
    s_idx, e_idx = cnvTimeToIdx(t, s_t, e_t)
    noise_power = np.mean(
        np.power(amp, 2.0)[:, s_idx:e_idx + 1], axis=1, keepdims=True)
    # 入力信号の音量の1%を下回らないようにする
    eps = 0.01 * input_power
    # 出力信号の振幅を計算する
    processed_power = np.maximum(input_power - alpha * noise_power, eps)
    # 比率
    wf_ratio = processed_power / (processed_power + mu * noise_power)
    # 出力信号の振幅に入力信号の位相をかける
    processed_stft_data = wf_ratio * stft_data
    # 逆フーリエ変換
    t, data_post = sp.istft(processed_stft_data, fs=fs,
                            window='hann', nperseg=512, noverlap=384)
    return (t, data_post)

def clipMain(wav_fpath, dB_th, wiener_alpha, wiener_mu, skip=False, **args):
    # 音声ファイルの読み込み
    wave, fs = wavread(wav_fpath)

    if not skip:
        tlen = len(wave) / fs
        # rmsを計算
        rms = feature.rms(y=wave)
        # rms -> 振幅に変換
        volume_dB = 20 * np.log10(rms[0] * 2**(1 / 2))
        # 時間配列の生成
        times_rms = times_like(rms, sr=fs)  # rmsにおける時間軸
        times_wave = np.arange(0, len(wave) / fs, 1 / fs)  # wavファイルの時間軸

        # dBを基準に音声をクリップする
        s_t, e_t = clipWaveByDB(volume_dB, times_rms, dB_th)
        s_idx, e_idx = cnvTimeToIdx(times_wave, s_t, e_t)

        # 雑音区間の抽出（時間）
        fst_seg_tlen = s_t
        snd_seg_tlen = tlen - e_t
        # 長い方を選ぶ
        if fst_seg_tlen > snd_seg_tlen:
            noise_s_t = 0
            noise_e_t = s_t
        else:
            noise_s_t = e_t
            noise_e_t = tlen
    else:
        s_t = args['s_t']
        e_t = args['e_t']
        noise_s_t = args['noise_s_t']
        noise_e_t = args['noise_e_t']

    # ウィナーフィルタをかける
    t_filtered, wave_filtered = wiener(
        wave, fs, noise_s_t, noise_e_t, alpha=wiener_alpha, mu=wiener_mu)

    # 音声をclipする
    s_idx, e_idx = cnvTimeToIdx(t_filtered, s_t, e_t)
    wave_filtered_clipped = wave_filtered[s_idx:e_idx + 1]

    return (wave_filtered_clipped, fs, s_t, e_t, noise_s_t, noise_e_t)


if __name__ == '__main__':
    #############
    ### Const ###
    #############
    DATASET_PATH = '/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/cp'
    OUTPUT_DIR_PATH = '/Users/toranosuke/Desktop/experiment_dataset/2022-03-23_gym/filtered_and_clipped'
    FILE_NAME_PREFIX = 'rec_'
    DB_TH = 40
    ALPHA = 1.0
    MU = 10

    #######################
    ### Filter and Clip ###
    #######################
    id = 0
    err_lists = {
        'no_clipping': [],
        'all_clipping': []
    }
    try:
        for p in glob.iglob(DATASET_PATH + '/*/*/'):
            # output用ディレクトリを作成
            output_path = OUTPUT_DIR_PATH + p[len(DATASET_PATH):]
            output_path = f'{OUTPUT_DIR_PATH}/{DB_TH}dB_ALPHA{ALPHA}_MU{MU}{p[len(DATASET_PATH):]}'
            os.makedirs(output_path, exist_ok=True)

            # 処理
            for i in range(6):
                in_file_path = p + FILE_NAME_PREFIX + str(i) + '.wav'
                out_file_path = output_path + \
                    FILE_NAME_PREFIX + str(i) + '.wav'

                if i == 0:
                    wave, fs, s_t, e_t, noise_s_t, noise_e_t = clipMain(
                        in_file_path, DB_TH, ALPHA, MU)
                    # エラーリストへの追加
                    if noise_s_t == noise_e_t:
                        err_lists['no_clipping'].append(output_path)
                    if s_t == e_t:
                        err_lists['all_clipping'].append(output_path)
                else:
                    wave, fs, _, _, _, _ = clipMain(
                        in_file_path, DB_TH, ALPHA, MU, True, s_t=s_t, e_t=e_t, noise_s_t=noise_s_t, noise_e_t=noise_e_t)

                # ファイルの保存
                wavwrite(out_file_path, wave, fs)

            print(f'[id:{id}] audio filles has been completed: {output_path}')
            id = id + 1
    finally:
        # 設定ファイルへ書き出し
        with open(f'{OUTPUT_DIR_PATH}/{DB_TH}dB_ALPHA{ALPHA}_MU{MU}/config.json', 'w') as f:
            config_data = {
                'dataset_path': {DATASET_PATH},
                'output_dir_path': {OUTPUT_DIR_PATH},
                'db_th': {DB_TH},
                'wiener_filter': {
                    'alpha': {ALPHA},
                    'mu': {MU}
                },
                'err_lists': err_lists
            }
            json.dump(config_data, f, indent=2)
            print(
                f'dump config file to {OUTPUT_DIR_PATH}/{DB_TH}dB_ALPHA{ALPHA}_MU{MU}/config.json')
