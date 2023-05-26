from email.mime.text import MIMEText
import smtplib
import random
import re
# global smtp, verify_code


def init_mail():
    global smtp, verify_code
    verify_code = {}
    data = ''
    user = ''
    password = ''

    with open("C:\\Users\\86182\\Desktop\\password.txt", 'r') as f:
        data = f.readlines()
        user = data[0].strip('\n')
        password = data[1]
    smtp = smtplib.SMTP("pop.exmail.qq.com")
    smtp.login(user, password)


def check_verify(email, code):
    if verify_code[email] == code:
        verify_code.pop(email)
        return True
    return False


def send_verify_code(email):
    #if not validate_email(email):
    #    return False

    random_num = random.randint(10000, 99999)
    random_num_str = str(random_num)
    verify_code[email] = random_num_str

    msg = MIMEText(
        "您好！您正在尝试登录或者找回密码，这是您的验证码，他可能一直有效，但我们建议您尽快登录:\n" + random_num_str,
        "plain", "UTF-8")
    msg['From'] = "12011129@mail.sustech.edu.cn"
    msg['To'] = email
    msg['Subject'] = "邮件主题"

    try:
        smtp.send_message(msg)
        return True
    except smtplib.SMTPException:
        return False


def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@mail\.sustech\.edu\.cn$'
    if re.match(pattern, email):
        return True
    else:
        return False
