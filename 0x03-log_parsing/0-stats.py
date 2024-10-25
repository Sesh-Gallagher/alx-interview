#!/usr/bin/python3
"""
Log parsing - script that reads stdin line by line and computes metrics:
"""

import sys

if __name__ == '__main__':

    def parseLogs():
        """
        Module that logs from standard input and generates reports
        Reports: Function prints log size after reading
                every 10 lines & at KeyboardInterrupt
        Raises: KeyboardInterrupt (Exception):
                handles this exception and raises it
        """

    count = 0
    filesize = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {i: 0 for i in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for i, j in sorted(stats.items()):
            if j:
                print("{}: {}".format(i, j))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
