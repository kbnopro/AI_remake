import os
import cv2
import csv
import setting.cfg as cfg
from glob import glob
import numpy as np
from npy_append_array import NpyAppendArray as npy_file

cfg.remove_file(cfg.resize_train_data_out)
cfg.remove_file(cfg.train_data_label)


def read_img(path):
    return cv2.resize(cv2.imread(path), [224, 224])


with npy_file(cfg.resize_train_data_out) as frames, npy_file(cfg.train_data_label) as labels:
    for vid_name in glob(os.path.join(cfg.train_data_path, "labels", "*")):
        print(vid_name)
        frames_path = vid_name.replace("labels", "frames")[:-4:]
        with open(vid_name) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[0] == 'Frame':
                    continue
                frames.append(np.expand_dims(
                    read_img(os.path.join(frames_path, row[0]+".PNG")), axis=0))
                labels.append(np.expand_dims(int(row[1]), axis=0))

frames_file = np.load(cfg.resize_train_data_out, mmap_mode='r')
print(frames_file.shape)
labels_file = np.load(cfg.train_data_label, mmap_mode='r')
print(labels_file.shape)
