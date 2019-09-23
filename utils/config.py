#训练中用到的参数单独写在一个文件中定义config 类 然后定义好对象opt 在用到这些参数的位置例如train中 调对象opt
#pprint会分行打印输出 对于很长的一般就用pprint不用print
from pprint import pprint
class Config:

    #前下划线是一种默认的提醒程序员是一种私有方法，python并没有强制规定，只在使用*导入的时候无法导入前下划线函数 其他操作并无不同
    def _state_dict(self):
        #__dict__ 返回实例对象对应的属性字典
        # 下面这句话 体现了如果是要 return for循环的写法，就不可以把for循环写在外面for xxx: return xxx 这样子，这样直接返回了，for循环执行不完。
        # getattr(object, name[,default]) 获取对象属性值
        return {k: getattr(self, k) for k, _ in Config.__dict__.items()}



    def _parse(self, kwargs):



opt = Config()
