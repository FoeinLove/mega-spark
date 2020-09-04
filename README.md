# MegaSpark说明
该项目旨在通过spark进行一站式数据分析与模型训练，保证最终落地的只有分析报告，可视化，以及模型训练评估结果，其次
该项目将pysaprk封装成mega对象来延续pandas的使用方法，进而实现在大数据场景下的使用pandas方法进行
数据分析和模型训练，消除相关同学在spark上投入的学习成本

目前提供以下模块：
* `ml`
* `sql`
* `entrance` 
  
  
```
# 本地安装
如果要给该项目贡献代码，在本地调试好后测试，本地安装方法

```python
$ git clone ...
$ cd megaspark
$ python install .
```

# 使用教程
以`magllan_ai.ml.mag_util.mag_metrics`模块为例，安装完成之后，可以使用以下方法导入使用

```
from libs.magellanai import *

data_df = read_csv("path/to/file.csv")
data_df.magellan.head(5)
```

# 打包发布

```
$ cd /path/to/megaspark
$ python setup.py sdist bdist_wheel
$ pip install twine
$ twine upload dist/*
```