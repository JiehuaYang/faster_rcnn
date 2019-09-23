import numpy as np
import torch

from utils.config import opt
from data.dataset import Dataset
# *args tuples *kwargs dict
def train(**kwargs):
    #先获取参数
    opt._parse(**kwargs)

    #数据集
    dataset = Dataset(opt)




if __name__ == '__main__':
    # 可以在命令行中决定调用哪个函数
    import fire
    fire.Fire()
