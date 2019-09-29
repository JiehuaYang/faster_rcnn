import numpy as np
import os
#处理特定数据集对应的标注
# 首先是路径，其次是用的哪一部分的数据集train val 还是test 是否使用difficult这种标注
class VOCDataset:
    def __init__(self, data_dir, split='trainval', use_difficult = False, return_difficult = False):
        #先获取id列表
        id_list = os.path.join(data_dir,'ImageSets/Main/{0}.txt'.format(split))
        self.ids = [id.strip() for id in open(id_list)]

        self.data_dir = data_dir
        self.use_difficult = use_difficult
        self.return_difficult = return_difficult

        #标签的类别
        self.label_names = VOC_BBOX_LABEL_NAMES

    def __len__():
        return len(self.ids)

    def get_examples():
        id_ = self.ids[i]
        anno = ET.parse(
            os.path.join(self.data_dir, 'Annotations', id_ + '.xml'))
        bbox = list()
        label = list()
        difficult = list()



VOC_BBOX_LABEL_NAMES = (
    'aeroplane',
    'bicycle',
    'bird',
    'boat',
    'bottle',
    'bus',
    'car',
    'cat',
    'chair',
    'cow',
    'diningtable',
    'dog',
    'horse',
    'motorbike',
    'person',
    'pottedplant',
    'sheep',
    'sofa',
    'train',
    'tvmonitor')
