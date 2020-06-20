#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "jsantos93, mcaac, OtacilioN, peedrohj"
__version__ = "1.0.0"

import sys
from image_crawler import download

IMAGE_LIMIT_PER_SEARCH = 300 #Google blocks when put more than 300

def exec_full_pipeline():
    exec_image_crawling()
    print("exec full pipeline")

def exec_image_crawling():
    download("analog electric meter", IMAGE_LIMIT_PER_SEARCH)
    download("analog electricity meter", IMAGE_LIMIT_PER_SEARCH)
    download("electricity meter", IMAGE_LIMIT_PER_SEARCH)
    download("electric meter", IMAGE_LIMIT_PER_SEARCH)
    download("energy meter", IMAGE_LIMIT_PER_SEARCH)
    download("medidor de energia", IMAGE_LIMIT_PER_SEARCH)
    download("medidor de energia analogico", IMAGE_LIMIT_PER_SEARCH)
    download("medidor de energia eletrica", IMAGE_LIMIT_PER_SEARCH)

if __name__ == "__main__":
    print(sys.argv)
    run_type = sys.argv[1]
    if run_type == "--full":
        exec_full_pipeline()
    elif run_type == "--image-crawler":
        exec_image_crawling()
    else:
        print("Warning you should define the run type")
        print("Calling full pipeline by default")
        exec_full_pipeline()
