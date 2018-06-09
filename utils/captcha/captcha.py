from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, os
import logging


class Verifycode(object):
    def __init__(self, width, height, num):
        self.width = width
        self.height = height
        self.num = num

    def getVerifycode(self):
        width = self.width
        height = self.height
        num = self.num
        code_lower, image_outs = self.veri_code(width, height, num)
        return code_lower, image_outs

    '''
    生成随机码
    '''

    def randon_code(self, length=6):
        code = ''
        char = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
        for i in range(length):
            index = random.randint(0, 54)
            code += char[index]

        return code

    '''
    随机颜色
    '''

    def randon_color(self, begin, end):
        return (random.randint(begin, end), random.randint(begin, end), random.randint(begin, end))

    # 生成图片
    def veri_code(self, width=160, height=40, length=6):
        # 创建image对象
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建font对象
        logging.info('系统路径:' + os.path.dirname(__file__))
        ttf = '/home/gujie/project/ihome/utils/captcha/fonts/Arial.ttf'
        font = ImageFont.truetype(ttf, 32)
        # 创建画布对象
        draw = ImageDraw.Draw(image)
        '''
        # 随机颜色填充每一个像素
        for x in range(0,width,10):
            for y in range(0,height,10):
                draw.point((x, y), fill=self.randon_color(64, 255))
        '''
        # 验证码
        code = self.randon_code(length)
        logging.info('验证码code:' + code)
        code_lower = ''  # 验证码code信息都变成小写
        # 随机颜色验证码写到图片上
        for t in range(length):
            draw.text((50 * t + 10, 5), code[t], font=font, fill=self.randon_color(32, 127))
            code_lower += code[t].lower()

        # 模糊滤镜
        # image = image.filter(ImageFilter.BLUR)

        image.save('/home/yanzhengma.png')

        image_out = open('/home/yanzhengma.png', 'rb')
        image_outs = image_out.read()
        return code_lower, image_outs
        # self.write(image_outs)
        # self.set_header("Content-Type", "image/png")
