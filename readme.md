编写一个 python 程序，可以从以下几中 office 文件中提取内嵌文件

1. doc
1. dot 
1. dotm 
1. xlt 
1. xlsm 
1. pps 
1. pptm 
1. wps 
1. wpt 
1. dps 
1. dpt 
1. et 
1. ett

主要内嵌的文件为图片
- tif
- jpg
- jpeg
- bmp
- png
- dib

## 编码风格简述

1. class 命名使用首字母大写的驼峰命名法
2. 代码在 pycharm 中不应出现红色波浪线或者警告
3. 代码应该有注释，注释应该清晰明了，因此不需要提供文档

## 编码之前

本项目提供了一个基础的抽象类，在实现任何类型的文件提取之前，应该先继承该类，然后实现其中的两个方法

- list_embed_files
- extract_embed_file

```python
class AbstractEmbedOfficeFile:
    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise ValueError(f"No such file: '{file_path}'")
        self.file_path = file_path

    def list_embed_files(self) -> List[str]:
        # return a list of embedded files but do not extract them
        raise NotImplementedError()
    
    def extract_embed_file(self, embed_file_name: str, output_path: str) -> None:
        # extract the embedded file to the output path
        raise NotImplementedError()
```

[res](./res) 目录中是样本文件，可以用来测试

依赖的第三方库加起来不可以超过 10 MB
程序运行过程中可允许产生任何临时文件

##  编程语言的选择

可以使用其它开发语言，但使用其它语言有如下要求

1. 提供完整源代码

2. 该语言支持静态编译，打包后不能超过 **30 MB** 并且你需要提供一键打包脚本，允许该项目可由他人维护

3. 支持如下调用方式 

   1. 在这种用法下，不生成任何临时文件 `--list-embed-files /path/to/office`

      1. 返回值应为`json`格式方便上层解析 `["f.bmp", "2.png"]`

   2. 仅在指定路径生成文件    ` --extract-embed-files /path/to/offfice  embed_filename --output-path /path/to/extract`

      ​	`embed_filename` 由上面的结果指定