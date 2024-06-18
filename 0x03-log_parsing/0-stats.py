#!/usr/bin/python3
""" This script shall read stdin line by line and compute metrics"""
import sys


if __name__ == "__main__":
    """ This instance shall read stdin line by line and compute metrics"""
    try:
        sum_sz = 0
        stt_cd = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
        x = 0
        for line in sys.stdin:
            x += 1
            data = line.split()
            if len(data) > 2:
                sum_sz += int(data[-1])
                if data[-2] in stt_cd:
                    stt_cd[data[-2]] += 1
            if x == 10:
                print("File size: {}".format(sum_sz))
                for m, n in sorted(stt_cd.items()):
                    if n != 0:
                        print("{}: {}".format(m, n))
                x = 0
    except KeyboardInterrupt:
        print("File size: {}".format(sum_sz))
        for m, n in sorted(stt_cd.items()):
            if n != 0:
                print("{}: {}".format(m, n))
        raise
    print("File size: {}".format(sum_sz))
    for m, n in sorted(stt_cd.items()):
        if n != 0:
            print("{}: {}".format(m, n))
