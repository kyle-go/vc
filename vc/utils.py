# -*-coding:utf-8-*-

"""
    a library for create verification-code

    url: https://github.com/kylescript/vc
    Author: kyle.script@gmail.com
"""

import os
import random
import tempfile

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

CUR_PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

# 待挑选的字符，由于一些字体原因，这里去掉容易混淆的 iI lL oO 10 字符, 还剩下54个字符
rand_chars = "abcdefghgkmnpqrstuvwxyzABCDEFGHGKMNPQRSTUVWXYZ23456789"
rand_fonts = (CUR_PATH + "fonts/ChalkboardSE-Light.ttf",
              CUR_PATH + "fonts/PrincetownStd.otf",
              CUR_PATH + "fonts/londrina-solid.ttf")


# 获取4个随机字符，已经去除了容易混淆的iI lL oO 10 字符了
def _get_rand_chars():
    rand_chars_len = len(rand_chars)
    rand_fonts_len = len(rand_fonts)
    result = []
    for i in range(0, 4):
        rchar = rand_chars[random.randint(0, rand_chars_len - 1)]
        rfont = rand_fonts[random.randint(0, rand_fonts_len - 1)]
        result.append((rchar, rfont))
    return result


def _draw_image_char(img, c, font, pos_x, index):
    pox_y = 0
    if "ChalkboardSE-Light.ttf" in font:
        pox_y = -12
    if "PrincetownStd.otf" in font:
        pox_y = 6
    if "londrina-solid.ttf" in font:
        pox_y = -5
    font = ImageFont.truetype(font, 36)
    draw = ImageDraw.Draw(img)
    draw.text((pos_x, pox_y), c, (25, 95, 88), font=font)
    if index == 1:
        img = img.rotate(random.randint(-8, 8), center=[22.5, 18])
    if index == 2:
        img = img.rotate(random.randint(-4, 4), center=[10 + 25, 18])
    if index == 3:
        img = img.rotate(random.randint(-2, 2))
    return img


def create_image():
    im = Image.new("RGBA", (120, 36), (0, 0, 0, 0))
    pos_x = 10
    index = 0
    vcode = ""
    cf = _get_rand_chars()
    for c in cf:
        vcode += c[0]
        im = _draw_image_char(im, c[0], c[1], pos_x, index)
        pos_x += 25
        index += 1

    tf = tempfile.mktemp(suffix=".png")
    im.save(tf)
    im.close()
    return vcode, tf
