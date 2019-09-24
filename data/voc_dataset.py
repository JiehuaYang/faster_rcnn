import numpy as np

#处理特定数据集对应的标注
# 首先是路径，其次是用的哪一部分的数据集train val 还是test 是否使用difficult这种标注
class VOCDataset:
    def __init__(self, data_dir, split='trainval', use_difficult = False, return_difficult = False)
