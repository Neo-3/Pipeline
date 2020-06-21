#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "jsantos93, mcaac, OtacilioN, peedrohj"
__version__ = "1.0.0"

import sys
from image_crawler import download
from feature_extractor import extract_image
from image_clustering import create_cluster
import os, shutil, glob, os.path
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16

SEARCHING_PARAMS=["analog electric meter", "analog electricity meter", "electricity meter", "electric meter", "energy meter", "medidor de energia", "medidor de energia analogico", "medidor de energia eletrica"]

def exec_full_pipeline():
    print("exec full pipeline")
    exec_image_crawling()
    exec_image_clustering()

def exec_image_crawling():
    IMAGE_LIMIT_PER_SEARCH = 300 #Google blocks when put more than 300
    print("Start image crawling")
    for search_param in SEARCHING_PARAMS:
        download(search_param, IMAGE_LIMIT_PER_SEARCH)
    print("Finish image crawling with success")

def exec_image_clustering():
    print("Start image clustering")
    imgdir = './downloads'
    targetdir = "./pipelineClusters"
    model = VGG16(weights='imagenet', include_top=False)

    files = glob.glob(os.path.join(imgdir, '*.jpg'))
    files.sort()
    image.LOAD_TRUNCATED_IMAGES = True 
    features = []
    for i, imagepath in enumerate(files):
        print("Extracting features: ", i+1, "/", len(files), end="\r") 
        img = image.load_img(imagepath, target_size=(256, 256))
        features.append(extract_image(img, model))
    print("Extracting features: ", len(files), "/", len(files)) 
    create_cluster(files, features, targetdir)

if __name__ == "__main__":
    print(sys.argv)
    if(len(sys.argv) > 1):
        run_type = sys.argv[1]
        if run_type == "--full":
            exec_full_pipeline()
        elif run_type == "--image-crawler":
            exec_image_crawling()
        elif run_type == "--image-clustering":
            exec_image_clustering()            
    else:
        print("Warning you should define the run type")
        print("Calling full pipeline by default")
        exec_full_pipeline()
