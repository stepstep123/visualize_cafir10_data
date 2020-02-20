#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/20/20 9:25 AM
# @Author  : Jianghua Yu
# @File    : read_cifar_10.py
# @Software: PyCharm
import pickle as p
import numpy as np
from PIL import Image
import os

def load_cifar10(filename, num):
    with open(filename, "rb") as f:
        datadict = p.load(f, encoding="latin1") # 输出为字典类型
        images = datadict["data"]
        labels = datadict["labels"]
        images = images.reshape(num, 3, 32, 32) # 32*32, channel = 3,
        labels = np.array(labels) # 0 - 9
    return images, labels

class_name = "0"
def get_class_name(label_id):
    # class_name = "0"
    global class_name
    if(label_id == "0"):
        class_name = "airplane"
    elif(label_id == "1"):
        class_name = "automobile"
    elif(label_id == "2"):
        class_name = "bird"
    elif(label_id == "3"):
        class_name = "cat"
    elif(label_id == "4"):
        class_name = "deer"
    elif(label_id == "5"):
        class_name = "dog"
    elif(label_id == "6"):
        class_name = "frog"
    elif(label_id == "7"):
        class_name = "horse"
    elif(label_id == "8"):
        class_name = "ship"
    elif(label_id == "9"):
        class_name = "truck"
    return class_name

def mkdir_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
train_img_num = 0
test_img_num = 0
def save(binary_img_path_list, folder_name):

    global train_img_num # 需要global化才能重新读写，否则只能引用，不可修改
    global test_img_num
    for item in binary_img_path_list:
        images, labels = load_cifar10(item, 10000)
        for i in range(images.shape[0]):
            print("**************")
            print(i)
            img = images[i]
            img_r = img[0]
            img_g = img[1]
            img_b = img[2]
            img_r = Image.fromarray(img_r)
            img_g = Image.fromarray(img_g)
            img_b = Image.fromarray(img_b)
            imgs = Image.merge("RGB", (img_r, img_g, img_b))
            if folder_name=="train":
                name = folder_name + "_" + str(train_img_num) + ".png"
            else:
                name = folder_name + "_" + str(test_img_num) + ".png"
            class_name = get_class_name(str(labels[i]))
            print(class_name)
            save_path = os.path.join(folder_name, class_name, name)
            mkdir_folder(os.path.join(folder_name, class_name))
            imgs.save(save_path, "png")
            train_img_num += 1
            test_img_num += 1

if __name__=="__main__":

    binary_img_path = []
    binary_img_path.append("./Cifar-10/cifar-10-batches-py/data_batch_1") # cifar训练批次地址
    binary_img_path.append("./Cifar-10/cifar-10-batches-py/data_batch_2")
    binary_img_path.append("./Cifar-10/cifar-10-batches-py/data_batch_3")
    binary_img_path.append("./Cifar-10/cifar-10-batches-py/data_batch_4")
    binary_img_path.append("./Cifar-10/cifar-10-batches-py/data_batch_5")

    save(binary_img_path, "train")
    test_binary_img_path = []
    test_binary_img_path.append("./Cifar-10/cifar-10-batches-py/test_batch") # cifar测试集地址
    save(test_binary_img_path, "test")



