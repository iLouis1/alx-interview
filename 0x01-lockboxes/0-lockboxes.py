#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    x = 0

    while x < length:
        oldi = x
        opened_boxes.append(x)
        keys.update(boxes[x])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                x = key
                break
        if oldi != x:
            continue
        else:
            break

    for x in range(length):
        if x not in opened_boxes and x != 0:
            return False
    return True
