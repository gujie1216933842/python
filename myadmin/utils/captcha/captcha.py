from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, os
import logging


class Verifycode(object):
    def __init__(self, width, height, num, font_spacing):
        self.width = width  # 验证码图片宽度
        self.height = height  # 验证码图片的高度
        self.num = num  # 验证码图片上字符个数
        self.font_spacing = font_spacing  # 验证码字符间距

    def getVerifycode(self):
        width = self.width
        height = self.height
        num = self.num
        font_spacing = self.font_spacing
        code_lower, image_outs = self.veri_code(width, height, num, font_spacing)
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
    def veri_code(self, width=160, height=40, length=6, font_spacing=40):
        # 创建image对象
        image = Image.new('RGB', (width, height), (255, 255, 255))
        # 创建font对象
        logging.info('系统路径:' + os.path.dirname(__file__))
        ttf = os.path.join(os.path.dirname(__file__), 'fonts/Arial.ttf')
        # ttf = '/home/gujie/project/ihome/utils/captcha/fonts/Arial.ttf'
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
            draw.text((font_spacing * t + 10, 4), code[t], font=font, fill=self.randon_color(32, 127))
            code_lower += code[t].lower()

        # 模糊滤镜
        # image = image.filter(ImageFilter.BLUR)
        image_save_path = os.path.join(os.path.dirname(__file__), 'yanzhengma.png')
        image.save(image_save_path)
        image_out = open(image_save_path, 'rb')
        image_outs = image_out.read()
        return code_lower, image_outs  # 返回验证码和图片,验证码是需要存储在session中的
