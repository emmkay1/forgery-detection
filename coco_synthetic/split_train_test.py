import networkx as nx
import numpy as np
import os
from glob import glob
import sys
import skimage.io as io
import pdb


def contain_node(graph_list, node):
    for g in graph_list:
        if g.has_node(node):
            return True
    return False


data_dir = "./filter_tamper"
ext = "Tp*"
dataDir = "./cocostuff/coco"
dataType = "train2014"  # COCO2014 train directory
coco_img = lambda name: "COCO_train2014_{:012d}.jpg".format(int(name))
cls = ["person", "airplane", "dog", "train", "bed", "refrigerator"]
filenames = glob(os.path.join(data_dir, ext))

G = nx.Graph()
print(len(filenames))
for file in filenames:
    content = os.path.splitext(os.path.basename(file))[0].split("_")
    if content[-1] in cls:
        target_name = content[1]
        source_name = content[2]
        G.add_edge(target_name, source_name)

train = sorted(
    (G.subgraph(c) for c in nx.connected_components(G)), key=len, reverse=True
)[0:950]
test = sorted(
    (G.subgraph(c) for c in nx.connected_components(G)), key=len, reverse=True
)[950:]

with open("train_filter.txt", "w") as f:
    for file in filenames:
        content = os.path.splitext(os.path.basename(file))[0].split("_")
        if content[-1] in cls:
            target_name = content[1]
            source_name = content[2]
            if (
                target_name != source_name
                and contain_node(train, target_name)
                and contain_node(train, source_name)
            ):
                x1 = float(content[3])
                y1 = float(content[4])
                x2 = float(content[5])
                y2 = float(content[6])
                source_img = io.imread(
                    os.path.join(dataDir, dataType, coco_img(source_name))
                )
                target_img = io.imread(
                    os.path.join(dataDir, dataType, coco_img(target_name))
                )
                s_w, s_h = source_img.shape[:2]
                t_w, t_h = target_img.shape[:2]
                f.write(
                    "%s %.5f %.5f %.5f %.5f\n"
                    % (
                        file.split('\\')[1],
                        x1 * s_h / t_h,
                        y1 * s_w / t_w,
                        x2 * s_h / t_h,
                        y2 * s_w / t_w,
                    )
                )


with open("test_filter.txt", "w") as f:
    for file in filenames:
        content = os.path.splitext(os.path.basename(file))[0].split("_")
        if content[-1] in cls:
            target_name = content[1]
            source_name = content[2]
            if (
                target_name != source_name
                and contain_node(test, target_name)
                and contain_node(test, source_name)
            ):
                x1 = float(content[3])
                y1 = float(content[4])
                x2 = float(content[5])
                y2 = float(content[6])
                source_img = io.imread(
                    os.path.join(dataDir, dataType, coco_img(source_name))
                )
                target_img = io.imread(
                    os.path.join(dataDir, dataType, coco_img(target_name))
                )
                s_w, s_h = source_img.shape[:2]
                t_w, t_h = target_img.shape[:2]
                f.write(
                    "%s %.5f %.5f %.5f %.5f\n"
                    % (
                        file.split('\\')[1],
                        x1 * s_h / t_h,
                        y1 * s_w / t_w,
                        x2 * s_h / t_h,
                        y2 * s_w / t_w,
                    )
                )
