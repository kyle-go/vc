# -*-coding:utf-8-*-

"""
    a library for create verification-code

    url: https://github.com/kylescript/vc
    Author: kyle.script@gmail.com
"""
import os
import sys
import base64
from vc.utils import create_image


def create_image_base64():
    """
        创建一个验证码 + 图片base64字符串流
    """
    code, file = create_image()
    b64str = "data:image/png;base64,"
    with open(file, "rb") as f:
        if sys.version_info.major == 2:
            b64str += base64.b64encode(f.read())
        else:
            b64str += base64.b64encode(f.read()).decode()
    os.remove(file)
    return True, {"code": code, "base64": b64str}


# 使用此方法时，注意删除临时文件
def create_image_file():
    """
        创建一个验证码 + 本地图片文件路径，注意使用完图片后删除
    """
    code, file = create_image()
    return True, {"code": code, "file": file}
