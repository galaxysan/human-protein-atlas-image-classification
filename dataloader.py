import json
import os
import pandas
import numpy

import torch.utils.data as data
from PIL import Image


class XixiDataset(data.Dataset):
    def __init__(self, path,csvpath,  switch="train", transform=None):
        self.path = path
        self.transform = transform
        self.data=pandas.read_csv(os.path.join(path, csvpath))
        self.switch=switch

    def __getitem__(self, index):
        r = Image.open(os.path.join(self.path, self.switch, self.data.iloc[index,0]) + "_red.png")
        g = Image.open(os.path.join(self.path, self.switch, self.data.iloc[index,0]) + "_green.png")
        b = Image.open(os.path.join(self.path, self.switch, self.data.iloc[index,0]) + "_blue.png")
        y = Image.open(os.path.join(self.path, self.switch, self.data.iloc[index,0]) + "_yellow.png")
        img = Image.merge("RGBA",(r,g,b,y))
        if self.transform is not None:
            img = self.transform(img)
        label = [0 for i in range(28)]
        if self.switch == "train":
            orilist = list(map(int,(self.data.iloc[index,1].split(" "))))
            for i in orilist:
                label[i]=1
        target = numpy.asarray(label,dtype=numpy.float32)
        return img, target

    def __len__(self):
        return len(self.data)
