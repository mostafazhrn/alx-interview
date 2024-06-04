#!/usr/bin/python3
""" This code shall determine if all the boxes can be opened """


def canUnlockAll(boxes):
    """ This function shall return true if boxes can be opened else false """
    no_cle = [0]
    no_bx = len(boxes)
    for cle in no_cle:
        for bx in boxes[cle]:
            if bx < no_bx and bx not in no_cle:
                no_cle.append(bx)
    if len(no_cle) == no_bx:
        return True
    return False
