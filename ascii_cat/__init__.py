#!/usr/bin/env python
"""
_ascii_cat_

ASCII Cat is a simple CLI for displaying cats as ascii art
on your command line

"""
import sys

__version__ = "0.0.0"
__copywrite__ = "Copyright 2016 Samantha Scharr"


def run():
    """ run ascii_cat """
    from ascii_cat.runner import main
    main(sys.argv[1:])
