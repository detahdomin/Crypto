from unittest import result
import string 
import random
import argparse



def gan_passwode():
    all_char_set=string.printable[:-6]
    all_char_set*=9
    result = ''.join(random.sample(all_char_set,k=9))
    return result

def create_password(pass_length,confuse=False):
    result= ""
    result += random.choice(string.ascii_uppercase)
    result += random.choice(string.ascii_letters)
    result += random.choice(string.ascii_lowercase)
    result += random.choice(string.digits)
    if confuse:
        result += 'Il'
        result += ''.join(random.sample(string.printable[:-6]*pass_length,pass_length-6))
    else:
        result += ''.join(random.sample(string.printable[:-6]*pass_length,pass_length-4))
    result = ''.join(random.sample(result,len(result)))
    return result

def evaluate_passwrod(password,show_info=True):
    result = False
    password_state =0b00000
    for char in password: 
        if char.isupper():
            password_state |= 0b10000
        elif char.islower():
            password_state |= 0b01000
        elif char.isdigit():
            password_state |= 0b00100
        else:
            password_state |= 0b00010
    if  len(password) >=8:
            password_state |= 0b00001 
    if (password_state==0b11111):
        if show_info:
            print('密码格式正确！')
        result = True 
    else:
        if show_info:
            NO = "密码格式错误，"
            if password_state & 0b10000 == 0:
                    NO+='密码没有英文大写,'
            if password_state & 0b01000 == 0:
                    NO+='密码没有英文小写,'
            if password_state & 0b00010 == 0:
                    NO+='密码没有符号,'
            if password_state & 0b00100 == 0:
                    NO+="密码没有数字,"
            if password_state & 0b00001 == 0:
                    NO+='长度不足8,'
            NO = NO[:-1]
            print (NO+"。")
        
    return result     


def main_passwordA():
    while 1:
        user_password =input("请用户输入密码,退出请输入Q:")
        if user_password == "Q":
            break
        elif evaluate_passwrod(user_password):
            pass

def main_passwrodB():
    while 1:
        user_passwrod = gan_passwode()
        if evaluate_passwrod(user_passwrod,show_info=False):
            print(f"新的密码为:{user_passwrod}") 
            break

def main_passwordC():
    parser = argparse.ArgumentParser(description='Generate new password.')
    parser.add_argument('-l', '--length' ,type=int,default=9,
                       help='length of password(default: 9)')
    parser.add_argument('-c', '--confuse' ,action='store_true',
                       help='use confuse characters(I & l)')
    args = parser.parse_args()
    for i in range(1):
        print(f"新生成的密码为:{create_password(args.length,args.confuse)}")

def main():
    while 1:
        yong_hu = input("检验密码请输入A,随机生成密码请输入B or C,退出请输入Q:")
        if yong_hu == "A":
            main_passwordA()
        elif yong_hu == "B":
            main_passwrodB()
        elif yong_hu == "C":
            main_passwordC()
        elif yong_hu == "Q":
            break
        else:
            print({}.format("抱歉没有这个指令"))
main()
