#!/usr/bin/env python3

import re
import os
import io

copyright = """// Copyright 2017 Zack Guo <zack.y.guo@gmail.com>. All rights reserved.
// Use of this source code is governed by a MIT license that can
// be found in the LICENSE file.

"""

exclude_dirs = [".git", "_docs"]
exclude_files = []
include_dirs = [".", "debug", "extra", "test", "_example"]


def is_target(fpath):
    return os.path.splitext(fpath)[-1] == ".go"


def update_copyright(fpath):
    print(f"processing {fpath}")
    f = io.open(fpath, 'r', encoding='utf-8')
    fstr = f.read()
    f.close()

    if m := re.search(
        '^// Copyright .+?\r?\n\r?\n', fstr, re.MULTILINE | re.DOTALL
    ):
        fstr = fstr[m.end():]

    # add new
    fstr = copyright + fstr
    f = io.open(fpath, 'w',encoding='utf-8')
    f.write(fstr)
    f.close()


def main():
    for d in include_dirs:
        files = [
            os.path.join(d, f) for f in os.listdir(d)
            if os.path.isfile(os.path.join(d, f))
        ]
        for f in files:
            if is_target(f):
                update_copyright(f)


if __name__ == '__main__':
    main()
