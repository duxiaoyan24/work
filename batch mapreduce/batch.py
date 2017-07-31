#!/bin/env python
# coding=utf-8

import sys

def load_paths():
    paths = []
    with open("paths_all") as f:
        for line in f:
            path = line.strip().split(" ")[-1]
            if path.find("SUCCESS") < 0:
                paths.append(path)
    return paths


def get_times(total, batch_size):
    if total % batch_size == 0:
        return total / batch_size
    else:
        return total / batch_size + 1


def run():
    mode = sys.argv[1]
    batch_size = int(sys.argv[2])

    paths = load_paths()
    if mode == "1":
        print get_times(len(paths), batch_size)
    if mode == "2":
        batch_time = int(sys.argv[3])
        ret_paths = []
        for i in range(batch_size * (batch_time - 1), batch_size * batch_time):
            if i < len(paths):
                ret_paths.append(paths[i])
        print ",".join(ret_paths)


if __name__ == "__main__":
    run()

