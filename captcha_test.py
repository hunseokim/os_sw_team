from captcha.image import ImageCaptcha

image = ImageCaptcha(width=160, height=90)

txt_captcha = '3ck8Bei'

image.generate(txt_captcha)
image.write(txt_captcha, 'captcha_result.png')