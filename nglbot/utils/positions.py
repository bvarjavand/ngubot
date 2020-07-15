import pandas as pd
import os
import pprint


def get_position_dict(printme=False):
    #     # TODO state detection
    #     # TODO inputs
    state_detection, inputs, buttons = split_positions()

    #     state_detection_clean = prep(state_detection)
    state_detection_dict = {}
    #     for row in state_detection_clean.values:
    #         depth = 0
    #         for key in row[1:3]:
    #             if key != "":
    #                 depth += 1
    #         if depth == 0:
    #             state_detection_dict[row[0]] = {"Button": [row[-2], row[-1]]}
    #         if depth == 1:
    #             state_detection_dict[row[0]][row[1]] = {"Button": [row[-2], row[-1]]}
    #         if depth == 2:
    #             state_detection_dict[row[0]][row[1]][row[2]] = {
    #                 "Button": [row[-2], row[-1]]
    #             }
    #     if printme:
    #         pprint.pprint(state_detection_dict)
    inputs_dict = {}

    buttons_clean = prep(buttons)
    buttons_dict = {}
    for row in buttons_clean.values:
        depth = 0
        for key in row[1:3]:
            if key != "":
                depth += 1
        if depth == 0:
            buttons_dict[row[0]] = {"Button": [row[-2], row[-1]]}
        if depth == 1:
            buttons_dict[row[0]][row[1]] = {"Button": [row[-2], row[-1]]}
        if depth == 2:
            buttons_dict[row[0]][row[1]][row[2]] = {"Button": [row[-2], row[-1]]}
    if printme:
        pprint.pprint(buttons_dict)
    return state_detection_dict, inputs_dict, buttons_dict


def split_positions():
    positions = os.path.join(os.path.dirname(__file__), "positions.xlsx")
    df = pd.read_excel(positions, header=None, usecols=list(range(2, 8)),)
    df = df.fillna("")
    state_detection = df.iloc[4:31]
    inputs = df.iloc[31:60]
    # print(state_detection.head())
    # print(inputs.head())
    buttons = df.iloc[60:]
    return state_detection, inputs, buttons


def prep(df):
    # only tested on buttons
    curr_0 = ""
    curr_1 = ""
    for row in df.values:
        if row[0] != "":
            curr_0 = row[0]
        else:
            row[0] = curr_0
        if row[1] != "":
            curr_1 = row[1]
        else:
            if row[2] != "":
                row[1] = curr_1
    return df


if __name__ == "__main__":
    _, _, df = get_position_dict(printme=True)
