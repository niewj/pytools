import os

# 文件名中想要替换的字符串(替换前)
old_str = '\xa1\xbewww.hoh0.com\xa1\xbf'
# 文件名中想要替换的字符串(替换后)
trim_str = ''

for fname in os.listdir("."):
    print(fname, '\t', os.rename(fname, fname.replace(old_str, trim_str)))
    print(fname, '\t', os.rename(fname, fname.replace('\xa1\xa2', '-')))
