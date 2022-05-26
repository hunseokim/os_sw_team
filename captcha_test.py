from captcha.image import ImageCaptcha

#보안문자
randomframe = Frame(mainFrame)
#새로고침
def refresh_btncmd():
    global randomframe
    randomframe.pack()

    image = ImageCaptcha(width=160, height=90)
    txt_captcha = print_random()
    image.generate(txt_captcha)
    image.write(txt_captcha, 'captcha_result.png')
    photo = PhotoImage(file='captcha_result.png')

    labelrandom = Label(randomframe, image=photo)
    labelrandom.grid(row = 1, column=0)
    rand = Entry(randomframe, width = 15, font = 8)
    rand.place(x = 40, y = 20)
    rand.grid(row = 2)
refresh_btncmd()