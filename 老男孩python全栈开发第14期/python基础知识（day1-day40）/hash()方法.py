"""
hash()方法
字典寻址采用了hash算法，每次运行程序时dict["key"]的hash值不变，只寻址一次，因此不受到字典数量大小影响。取值速度大于列表。
__hash__(): hash()方法内部调用了__hash__()
"""