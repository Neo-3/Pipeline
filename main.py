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
from image_data_augmentation import augment_data
import os
import shutil
import glob
import os.path
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
import math

SEARCHING_PARAMS = ["analog electric meter", "analog electricity meter", "electricity meter", "electric meter",
                    "energy meter", "medidor de energia", "medidor de energia analogico", "medidor de energia eletrica"]


def exec_full_pipeline():
    print("exec full pipeline")
    exec_image_crawling()
    exec_image_clustering()
    exec_image_data_augmentation()


def exec_image_crawling():
    IMAGE_LIMIT_PER_SEARCH = 300  # Google blocks when put more than 300
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
    print("Warning: Now you have to mannualy look to each cluster and select the good and bad examples")
    print("Once you select it create a folder called selected")
    print("Put the bad examples in selected/0 and good examples in selected/1")
    input("Press any key once you finish this process")


def _safe_create_dir(dir_name):
    try:
        os.makedirs(dir_name)
    except OSError:
        pass


def exec_image_data_augmentation():
    IMAGE_BASE_GROWTH_RATIO = 5
    train_test_ratio = 0.7
    bad_img_dir = './selected/0'
    good_img_dir = './selected/1'
    _safe_create_dir('augmented/test/1')
    _safe_create_dir('augmented/train/1')
    _safe_create_dir('augmented/test/0')
    _safe_create_dir('augmented/train/0')

    bad_files = glob.glob(os.path.join(bad_img_dir, '*.jpg'))
    good_files = glob.glob(os.path.join(good_img_dir, '*.jpg'))

    train_bad_files = bad_files[:math.floor(
        len(bad_files)*train_test_ratio)]
    test_bad_files = bad_files[math.floor(
        len(bad_files)*train_test_ratio):]

    train_good_files = good_files[:math.floor(
        len(good_files)*train_test_ratio)]
    test_good_files = good_files[math.floor(
        len(good_files)*train_test_ratio):]

    print("Augmenting bad examples train data")
    augment_data(bad_img_dir, train_bad_files, 'augmented/train',
                 IMAGE_BASE_GROWTH_RATIO, '0')

    print("Augmenting bad examples test data")
    augment_data(bad_img_dir, test_bad_files, 'augmented/test',
                 IMAGE_BASE_GROWTH_RATIO, '0')

    print("Augmenting good examples train data")
    augment_data(good_img_dir, train_good_files, 'augmented/train',
                 IMAGE_BASE_GROWTH_RATIO, '1')

    print("Augmenting good examples test data")
    augment_data(good_img_dir, test_good_files, 'augmented/test',
                 IMAGE_BASE_GROWTH_RATIO, '1')


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
        elif run_type == "--image-data-augmentation":
            exec_image_data_augmentation()
    else:
        print("Warning you should define the run type")
        print("Calling full pipeline by default")
        exec_full_pipeline()
