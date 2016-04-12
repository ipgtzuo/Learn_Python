#encoding=utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# from django.shortcuts import render
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# Create your views here.
# def getcode(request):#add by ying.zhou:生成验证码
#     return  render(request, 'auth/register.html', {'form': ''})
# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
image.save('raw.jpg', 'jpeg');
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)

image.save('code.jpg', 'jpeg');
# print image.__dict__
# print "<a>sdf<br>dsf</a>";
# #image.show();
# print image[1]