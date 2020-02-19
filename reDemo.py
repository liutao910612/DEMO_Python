import re
"""
Python通过re模块提供对正则表达式的支持
"""
"""
re.match(pattern,string,flags=0)
pattern:匹配的正则表达式， string:要匹配的字符串，flags：为标志位，用于控制正则表达式的匹配方式，
如是否区分大小写和多行匹配。
"""
print(re.match("^\w[a-z]*\d$","hello1")) # <re.Match object; span=(0, 6), match='hello1'>

"""
re.search(pattern,string,flags=0):用于扫描整个字符串并返回一个成功匹配的字符串
pattern:匹配的正则表达式， string:要匹配的字符串，flags：为标志位，用于控制正则表达式的匹配方式，
如是否区分大小写和多行匹配。
"""
print(re.search("^\w[a-z]*\d$","hello1")) # <re.Match object; span=(0, 6), match='hello1'>

#两个函数的区别在于，第一个函数必须首字母匹配，而第二个函数只要字符串中有子字符串匹配就行。  AQ