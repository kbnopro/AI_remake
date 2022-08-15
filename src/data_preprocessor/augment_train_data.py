from mmap import mmap
import setting.cfg as cfg
import cv2
import numpy as np
from npy_append_array import NpyAppendArray as npy_file
import random
from tqdm import tqdm

cfg.remove_file(cfg.augment_train_data_frames)
cfg.remove_file(cfg.augment_train_data_labels)

train_frames = np.load(cfg.resize_train_data_out, mmap_mode='r')
train_labels = np.load(cfg.train_data_label, mmap_mode='r')

cnt = 0

with npy_file(cfg.augment_train_data_frames) as aug_frames, npy_file(cfg.augment_train_data_labels) as aug_labels:
    for frame, label in tqdm(list(zip(train_frames, train_labels))):
        if random.randint(0, 1):
            frame = cv2.rotate(frame, rotateCode=cv2.ROTATE_90_CLOCKWISE)
        if random.randint(0, 1):
            frame = cv2.rotate(frame, rotateCode=cv2.ROTATE_180)
        frame = cv2.flip(frame, random.randint(-1, 1))
        for i in range(label*3+1):
            aug_frames.append(np.expand_dims(frame, axis=0))
            aug_labels.append(np.expand_dims(label, axis=0))
            frame = cv2.rotate(frame, rotateCode=cv2.ROTATE_90_CLOCKWISE)

aug_frames_file = np.load(cfg.augment_train_data_frames, mmap_mode='r')
print(aug_frames_file.shape)
aug_labels_file = np.load(cfg.augment_train_data_labels, mmap_mode='r')
print(aug_labels_file.shape)
