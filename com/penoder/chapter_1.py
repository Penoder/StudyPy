str = "Hello Python"
print(str)

str = "Python"
print(str)

arr = ["Today ", "Is ", 5]
print(arr)

arr[2] = "Monday"
print(arr)

# 集合 无序，不重复
students = {"LiHua", "HanMeiMei", "LiLei", "Tom", "Jane", "LiHua"}
# TypeError: set expected at most 1 arguments, got 4 ---> Set 集合最多一个参数
teacher = set("ZhangSan")  # 等同于 teacher = {'Z', 'h', 'a', 'n', 'g', 'S', 'a', 'n'}
# 集合不支持 + 操作符，List列表 和 Tuple 元组可以
print(students, teacher)

print("Lihua" in students)
print("Z" in teacher)

"""
Python 第一课： 基本数据类型
    1. Python 中的变量不需要声明，变量在使用前必须赋值，此时变量才会被创建；
    2. Python 中，变量就是变量，没有类型；常说的"类型"是指在内存中对象的类型；
    3. Python3 的六个标准数据类型：Numbers(数字)、String(字符串)、List(列表)、Tuple(元组)、Sets(集合)、Dictionaries(字典)；

A、Numbers(数字)
    Python3 支持 int、 float、 bool、 complex(复数)。内置的 type() 函数可以查询变量对应的对象类型。
    数字类型的变量 的 数值运算需要区分与 Java 的有 除法 和 乘方等；例如：
    2 / 4 = 0.5 得到的是一个 浮点型的数，而 2 // 4 = 0， 等到的是整型，后面的除法才类似 Java 中的除法操作。
    另外： ** 表示的是乘方，如 2 ** 5 = 32 表示 2 的 5 次方。

    注意：
    1. Python 可以同时为多个变量赋值，例如 a, b = 1, 2
    2. 一个变量可以通过赋值指向不同类型的对象
    3. 数值的除法运算 / 和 // 的区别
    4. 混合运算中， Python 会将整型转成浮点型

B、String(字符串)	
    Python 中的字符串采用 单引号 或者是 双引号 括起来，需要使用转义可以采用 反斜杠（\）进行特殊字符的转义; 如果不想要转义字符生效，可以在字符串前面添加 r，表示原始字符。
    字符串可以采用 * 用来重复，例如 'Python' * 2 等于 PythonPython
    
    Python中的字符串有两种索引方式，一种是从左到右，索引从0开始依次增加；第二种是从右到左，从-1开始依次减少； 
    另外，不像Java 中存在单独的字符类型，Python中一个字符对应的也是字符串，只是长度为1.

    字符串的裁剪，Python中可以采用str[startIndex:endIndex] 裁切出字符串 str 中 startIndex 到 endIndex 的一段字符串，左闭右开，
    等同于 Java 中的 str.subString(startIndex, endIndex), 不同的是，Python中，冒号两边的索引可以省略，
    左边startIndex 省略表示从最左边开始， 右边endIndex 省略表示到最后结束.
    例如：str = "Hello Python"、 str[:] = "Hello Python"、 str[6:] = "Python"、 str[:6] = "Hello"

    注意：Python中的字符串 可以 重新赋值，例如 str = 'a'、 然后继续 str = 'b' 但是不能 str[0] = 'b' 修改字符串内容，否则会抛出：
    TypeError: 'str' object does not support item assignment。 

C、List(列表)
    List 是Python中使用最为频繁的数据类型，列表写在 方括号之间，采用逗号分隔元素，每个元素对应的数据类型可以不同；例如 arr = ["Python ", "Today is", 16]
    和字符串一样，列表也具有索引，以及可以被裁切；列表裁切之后得到的是一个新的列表；
    另外：列表支持 + 操作符，例如 a = [1, 2, "3"]  a + [4, 5] = [1, 2, "3", 4, 5]; 列表还有不同于字符串的地方，列表中的元素可以改变，
    以上面 arr 列表为例，arr[2] = " Monday", 则打印 arr 会得到 Python Today is Monday
    
    List 内置了很多的函数，后面用到在讲。

D、Tuple(元组)
    元组和列表比较相像，不同的是元素写在小括号中，采用逗号分隔，并且元组中的元素不能够被修改；虽然元组的元素不可以变化，但是它包含的元素可以是可变化的对象，例如某个元素是 列表List；元组同 List 支持 + 操作符。

    另外：元组比较特殊的有元素为0个和1个的情况，元素为0时是一个空元组，tuple1 = () 表示一个空元组，当元素为1 时，需要在元素后面加上逗号，如 tuple2 = ("Python",)。

    String、List、Tuple 都属于 Sequence(序列)

E、Sets(集合)
    集合 是一个 无序的，无重复的元素的集合，（Java中Set集合？）基本功能是进行成员关系测试和消除重复元素。
    可以使用大括号 或者 set()函数创建set集合，注意：创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。

F、Dictionaries(字典)
    字典（dictionary）是Python中另一个非常有用的内置数据类型。
    字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
    关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
    在同一个字典中，关键字还必须互不相同。
    这不是 Java 中的 Map集合吗？？？
    
"""
