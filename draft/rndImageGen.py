__author__ = 'nolan'
# coding=utf-8


import random
import time
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

_lower_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _lower_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(1, 10)))  # 数字
init_chars = ''.join((_lower_cases, _upper_cases, _numbers))
# pic_static_url = "../../static/dashboard/"
# fontType = pic_static_url + "fonts/fontello.ttf"
fontType = ImageFont.truetype('Arial.ttf', 36)

def generate_validate_code(size=(120, 30),
                             chars=init_chars,
                             img_type="GIF",
                             mode="RGB",
                             bg_color=(255, 255, 255),
                             fg_color=(0, 0, 255),
                             font_size=18,
                             font_type=fontType,
                             length=4,
                             draw_lines=True,
                             n_line=(1, 2),
                             draw_points=True,
                             point_chance=2):
    '''
    @todo: 生成验证码图片
    @param size: 图片的大小，格式（宽，高），默认为(120, 30)
    @param chars: 允许的字符集合，格式字符串
    @param img_type: 图片保存的格式，默认为GIF，可选的为GIF，JPEG，TIFF，PNG
    @param mode: 图片模式，默认为RGB
    @param bg_color: 背景颜色，默认为白色
    @param fg_color: 前景色，验证码字符颜色，默认为蓝色#0000FF
    @param font_size: 验证码字体大小
    @param font_type: 验证码字体，默认为 ae_AlArabiya.ttf
    @param length: 验证码字符个数
    @param draw_lines: 是否划干扰线
    @param n_lines: 干扰线的条数范围，格式元组，默认为(1, 2)，只有draw_lines为True时有效
    @param draw_points: 是否画干扰点
    @param point_chance: 干扰点出现的概率，大小范围[0, 100]
    @return: [0]: PIL Image实例
    @return: [1]: 验证码图片中的字符串
    '''
    width, height = size  # 宽， 高
    img = Image.new(mode, size, bg_color)  # 创建图形
    draw = ImageDraw.Draw(img)  # 创建画笔
    if draw_lines:
        create_lines(draw, n_line, width, height)
        if draw_points:
            create_points(draw, point_chance, width, height)
            strs = create_strs(draw, chars, length, font_type, font_size, width, height, fg_color)

    # 图形扭曲参数
    params = [1 - float(random.randint(1, 2)) / 100,0,0,0,
            1 - float(random.randint(1, 10)) / 100,
            float(random.randint(1, 2)) / 500,
            0.001,
            float(random.randint(1, 2)) / 500
            ]
    img = img.transform(size, Image.PERSPECTIVE, params)  # 创建扭曲

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）
    print img

    return img, strs


def create_lines(draw, n_line, width, height):
    '''绘制干扰线'''
    line_num = random.randint(n_line[0], n_line[1])  # 干扰线条数
    i = 0
    for i in range(line_num):  # 起始点
        begin = (random.randint(0, width/2), random.randint(0, height/2))
        # 结束点
        end = (random.randint(width/2, width), random.randint(height/2, height))
        draw.line([begin, end], fill=rndColor())

def create_points(draw, point_chance, width, height):
    '''绘制干扰点'''
    chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]
    for w in xrange(width):
        for h in xrange(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w, h), fill=rndColor2())

def create_strs(draw, chars, length, font_type, font_size, width, height, fg_color):
    '''绘制验证码字符'''
    '''生成给定长度的字符串，返回列表格式'''
    c_chars = random.sample(chars, length)
    strs = ' '.join(c_chars)  # 每个字符前后以空格隔开
#     font = ImageFont.truetype(font_type, font_size)
    font = ImageFont.truetype('Arial.ttf', 20)
    font_width, font_height = font.getsize(strs)
    draw.text(((width - font_width) / 3, (height - font_height) / 3), strs, font=font, fill=fg_color)
    return ''.join(c_chars)

# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())




if __name__ == "__main__":

    code_img = create_validate_code()


    # code_img[0].open('C:\Users\Administrator\Desktop')
    # ISOTIMEFORMAT = '%Y%m%d'
    # date = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    # pic_url = pic_static_url + "code/" + date
    # if(os.path.exists(pic_url) == False):
    #     os.makedirs(pic_url)
#     import thread
#     thread.exit()

    # code_img[0].save(pic_url+"/code.jpg")
    code_img[0].save("./code_new.jpg")
    # print code_img[0]
    # print pic_url+"/code.jpg"
    # print code_img[1]