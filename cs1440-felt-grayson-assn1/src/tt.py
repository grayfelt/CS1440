#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage

import sys

if len(sys.argv) < 2:
    usage()
    sys.exit(1)
# error handling
else:
    tool = sys.argv[1]
    if tool == "cat":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='cat')
        else:
            cat(sys.argv)
    elif tool == "tac":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='tac')
        else:
            tac(sys.argv)
    elif tool == "cut":
        if sys.argv[2] == '-f':
            if len(sys.argv) < 5:
                usage(error="Too few arguments", tool='cut')

            else:
                cut(sys.argv)
        elif len(sys.argv) < 3:
            usage(error="Too few arguments", tool='cut')

        else:
            cut(sys.argv)
    elif tool == "paste":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='paste')

        else:
            paste(sys.argv)
    elif tool == "grep":
        if sys.argv[2] == 'v':
            if len(sys.argv) < 5:
                usage(error="Too few arguments", tool='grep')

            else:
                grep(sys.argv)
        elif len(sys.argv) < 4:
            usage(error="Too few arguments", tool='grep')

        else:
            grep(sys.argv)
    elif tool == "head":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='head')

        elif sys.argv[2] == '-n':
            if len(sys.argv) < 4:
                usage(error="Number of lines is required", tool='head')
            elif not sys.argv[3].isdigit():
                usage(error="Number of lines is required", tool='head')
            elif len(sys.argv) < 5:
                usage(error="Too few arguments", tool='head')
            else:
                head(sys.argv)
        else:
            head(sys.argv)
    elif tool == "tail":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='tail')
        elif sys.argv[2] == '-n':
            if len(sys.argv) < 4:
                usage(error="Number of lines is required", tool='tail')
            elif not sys.argv[3].isdigit():
                usage(error="Number of lines is required", tool='tail')
            elif len(sys.argv) < 5:
                usage(error="Too few arguments", tool='tail')
            else:
                tail(sys.argv)
        else:
            tail(sys.argv)
    elif tool == "sort":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='sort')

        sort(sys.argv)
    elif tool == "wc":
        if len(sys.argv) < 3:
            usage(error="Too few arguments", tool='wc')

        else:
            wc(sys.argv)
