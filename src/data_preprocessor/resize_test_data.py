import setting.cfg as cfg  # cfg file to get paths
from npy_append_array import NpyAppendArray as npy_file
import cv2
import os
from glob import glob
import numpy as np


cfg.remove_file(cfg.resize_test_data_out)
cfg.remove_file(cfg.test_data_framename)


def read_img(path):

    return cv2.resize(cv2.imread(path), [224, 224])


names = []

with npy_file(cfg.resize_test_data_out) as frames:
    for vid_name in glob(cfg.test_data_path+"*"):
        print(vid_name)
        for frame_name in glob(os.path.join(vid_name, "*")):
            frames.append(np.expand_dims(read_img(frame_name), axis=0))
            names.append(
                f'{os.path.basename(vid_name)}_{os.path.basename(frame_name[:-4:])}')


np.save(cfg.test_data_framename, names)

names_file = np.load(cfg.test_data_framename, mmap_mode='r')
print(names_file.shape)
frames_file = np.load(cfg.resize_test_data_out, mmap_mode='r')
print(frames_file.shape)
