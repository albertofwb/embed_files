import os
from typing import List


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
    

# 实现 dot 内嵌文档的解析
class EmbedOfficeFileDot(AbstractEmbedOfficeFile):
    def list_embed_files(self) -> List[str]:
        raise NotImplementedError()
    