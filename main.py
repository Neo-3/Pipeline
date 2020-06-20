#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "jsantos93, mcaac, OtacilioN, peedrohj"
__version__ = "1.0.0"

import sys


def exec_full_pipeline():
    print("exec full pipeline")


if __name__ == "__main__":
    print(sys.argv)
    run_type = sys.argv[1]
    if run_type == "--full":
        exec_full_pipeline()
    else:
        print("Warning you should define the run type")
        print("Calling full pipeline by default")
        exec_full_pipeline()
