#!/usr/bin/env python3
# coding: utf-8

import pprint

def select_robot(array, key):
    # sort
    class_one_results = [i for i in array if i['predicted_class'] == 1]

    if len(class_one_results) > 0:
        max_proba_result = max(class_one_results, key=lambda x: x[key])
    else:
        max_proba_result = {'robot_id': -1}

    # pprint.pprint(array)
    # print('\n')
    # print(max_proba_result)
    # print('-------------\n')
    return max_proba_result

def select_robot_45(array, key):
    # extraction class 1
    class_one_results = [i for i in array if i['predicted_class'] == 1]
    # sort by robot_id
    class_one_results = sorted(
        class_one_results, key=lambda x: x['robot_id'])

    # 場合分け
    if len(class_one_results) == 1:
        max_proba_result = class_one_results[0]
    elif len(class_one_results) == 2:
        if class_one_results[0]['robot_id'] == 1 and class_one_results[1]['robot_id'] == 2:
            max_proba_result = class_one_results[0]
        elif class_one_results[0]['robot_id'] == 4 and class_one_results[1]['robot_id'] == 5:
            max_proba_result = class_one_results[1]
        else:
            max_proba_result = {'robot_id': -1}
    elif len(class_one_results) == 3:
        if class_one_results[0]['robot_id'] == 1 and class_one_results[1]['robot_id'] == 2 and class_one_results[2]['robot_id'] == 3:
            max_proba_result = class_one_results[1]
        elif class_one_results[0]['robot_id'] == 2 and class_one_results[1]['robot_id'] == 3 and class_one_results[2]['robot_id'] == 4:
            max_proba_result = class_one_results[1]
        elif class_one_results[0]['robot_id'] == 3 and class_one_results[1]['robot_id'] == 4 and class_one_results[2]['robot_id'] == 5:
            max_proba_result = class_one_results[1]
        else:
            max_proba_result = {'robot_id': -1}
    else:
        max_proba_result = {'robot_id': -1}

    # pprint.pprint(array)
    # print('\n')
    # print(max_proba_result)
    # print('-------------\n')
    return max_proba_result
