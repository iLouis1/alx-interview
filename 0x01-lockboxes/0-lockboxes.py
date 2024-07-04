#!/usr/bin/python3
'''The lockBoxes Challenge'''


def canUnlockAll(boxes):
    '''This determines if all boxes can be opened or not
    Returns:
        True: If all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    k = 0

    while k < length:
        oldi = k
        opened_boxes.append(k)
        keys.update(boxes[k])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                k = key
                brek
        if oldi != k:
            continue
        else:
            break

    for k in range(length):
        if k not in opened_boxes and k != 0:
            return False
    return True
