"""
    本章玩一下元组： 元组 和 列表是近亲关系，所以在实际的使用过程当中是非常类似的
"""

list1 = ["Pen", 2, [3, 9]]
print(list1)

# 向列表中增加元素 append 方法将待添加的元素增加到最后面
list1.append("a")  # 向列表中添加一个元素
print(list1)
list1.append([2, 3, 5])  # 向列表中添加一个列表

# 向列表中拓展元素 extend
list1.extend("b")  # 拓展一个元素
print(list1)
list1.extend([1, "coder"])  # 拓展一个列表中的元素
print(list1)
list1.extend([[1, 3, 5]])  # 拓展一个列表
print(list1)

# ------------------------------------- 上面是添加的操作 -------------------------------------
# 使用 remove 方法进行元素的移除，必须保证列表当中存在需要移除的元素
list1.remove("coder")
print(list1)
# ValueError: list.remove(x): x not in list
# list1.remove("元素不存在")

# 使用 del 语句进行移除
del list1[7]  # 类似与 Java 中的数组下标，移除第 i 个元素
print(list1)

# 另外一种方式就是出栈，列表相当于是一种 栈的数据结构，调用 pop 方法可以将栈顶的元素出栈
# 如果向 pop 方法传递参数索引，可以将栈中指定数据移除？？？ （不对啊，栈不是先进后出吗？还可以指定某个先出？）
list1.pop()
print(list1)
list1.pop(2)
print(list1)

# 另外，列表还有一些官方 API， 例如
list1.reverse()  # 集合倒转
print(list1)

# list1.sort()    # 默认从小到大排序, 不过元素的类型不一致，造成 TypeError
# print(list1)

del list1

# ----------------------------------------------- 元组 --------------------------------------
tuple1 = (1,)  # 如果创建的元组只有一个元素，需要在后面添加一个逗号表示元组类型
print(tuple1)
print(type(tuple1))
tuple2 = 1, 1, 2, 3, 5, 8
print(tuple2)
print(type(tuple2))
# 元组 声明 并不一定需要 () 来包含元素，关键是元素之间需要带上 逗号
