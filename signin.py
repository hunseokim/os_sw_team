from msilib.schema import ComboBox
from tkinter import *
import tkinter.messagebox as msgbox
import random
import string
from tkinter.ttk import Combobox
from captcha.image import ImageCaptcha
import re

def is_email_valid(email):
    REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if not re.fullmatch(REGEX_EMAIL, email):
        return False
    else:
        return True

root = Tk()
root.title("CLOUD") #창 이름
root.geometry("540x360+200+100") #윈도우/창이 나타나는 위치를 지정


title = Label(root, text = "CLOUD 회원가입", font = ("맑은 고딕", '25','bold'))
#title.grid(row = 1, column = 1)
title.pack()


mainFrame = Frame(root)
mainFrame.pack()

#이름
nameframe = Frame(mainFrame)
nameframe.pack()
labelname = Label(nameframe, text = "이름", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelname.grid(row = 1, column=0)
name = Entry(nameframe)
name.grid(row = 1, column = 1)



ischecked=0
#성별
sexframe = Frame(mainFrame)
sexframe.pack()
labelsex = Label(sexframe, text = "성별", width = 16, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelsex.grid(row = 1, column=0)

sex = IntVar()
male = Radiobutton(sexframe, text = "남성", anchor = "e", variable = sex, value = 1) #남성은 1
female = Radiobutton(sexframe, text = "여성", anchor = "e", variable = sex, value = 2) #여성은 2
male.grid(row=1, column=1)
female.grid(row=1, column=2)


#이메일
emailframe = Frame(mainFrame)
emailframe.pack()
labelemail = Label(emailframe, text = "e-mail", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelemail.grid(row = 1, column=0)
email = Entry(emailframe)
email.grid(row = 1, column = 1)

#패스워드
pwframe = Frame(mainFrame)
pwframe.pack()
labelpw = Label(pwframe, text = "password", width = 10, font = ("맑은 고딕", '9','bold'), anchor = "w")
labelpw.grid(row = 1, column=0)
pw = Entry(pwframe, show = '*')
pw.grid(row = 1, column = 1)

def print_random():
    _LENGTH_=6
    string_pool = string.ascii_uppercase + string.digits

    result = ""
    for i in range(_LENGTH_):
        result += str(random.choice(string_pool))
    return result

#보안문자
randomframe = Frame(mainFrame)
#새로고침
def refresh_btncmd():
    global randomframe
    global txt_captcha
    randomframe.pack()

    image = ImageCaptcha(width=160, height=90)
    txt_captcha = print_random()
    image.generate(txt_captcha)
    print(txt_captcha)
    image.write(txt_captcha, 'captcha_result.png')
    photo = PhotoImage(file='captcha_result.png')

    labelrandom = Label(randomframe, image=photo)
    labelrandom.grid(row = 1, column=0)
refresh_btncmd()
randstr = Entry(randomframe, width = 15, font = 8)
randstr.place(x = 40, y = 20)
randstr.grid(row = 2)

ref_btn = Button(randomframe, text = "새로고침", anchor = "e", command = refresh_btncmd)
ref_btn.grid(row = 1, column = 1)


#등록 버튼 기능
def signin_btncmd():
    if email.get() == "" or is_email_valid(email.get())==False or pw.get() == "" or name.get() == "" or (sex.get()!= 1 and sex.get()!= 2) or randstr.get().upper()!=txt_captcha:
        msgbox.showwarning("오류", f"입력되지 않은 정보가 있습니다. 다시 확인하세요.")
    else:
        msgbox.showinfo("알림", "회원가입이 완료되었습니다")

#등록 버튼
signin_btn = Button(root, text = "등록", anchor = CENTER, command=signin_btncmd, width = 10, height = 2)
signin_btn.pack()


root.mainloop()