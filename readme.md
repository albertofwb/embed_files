编写一个 python 程序，可以从以下集中 office 文件中提取内嵌文件

- dot 
- dotm 
- xlt 
- xlsm 
- pps 
- pptm 
- wps 
- wpt 
- dps 
- dpt 
- et 
- ett

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
