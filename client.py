#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#coding = utf8
'''
name : Liyiming
date : 2018-9-28
email : 1242809365@qq.com
modules : pymysql
This is an electranic_dictionary client
'''


from socket import *
import sys,traceback,time


def main():
    host = sys.argv[1]
    post = int(sys.argv[2])
    addr = (host,post)
    s = socket()
    try:
        s.connect(addr)
    except:
        traceback.print_exc()
        return

    while True:
        print('''
        ========Welcome=======
        -1.注册 2.登录 3.退出-
        ======================''')
        cmd = input('请输入命令：')
        if cmd not in ['1','2','3']:
            print('输入错误请重新输入')
        else:
            if cmd == '1':
                s.send('1'.encode())
                while True:
                    user_name = input('请输入用户名：')
                    password = input('请输入密码：')
                    password1 = input('请确认密码：')
                    if password == password1:
                        # s.send('1'.encode())
                        s.send(user_name.encode())
                        time.sleep(1)
                        s.send(password.encode())
                    data= s.recv(1024)
                    print(data.decode())
                    if data.decode() == '注册成功':
                        break
                    else:
                        break
            elif cmd == '2':
                s.send('2'.encode())
                while True:
                    user_name = input('请输入用户名,输入回车返回上一层')
                    if not user_name:
                        s.send('##'.encode())
                        break
                    password = input('请输入密码：')
                    s.send(user_name.encode())
                    time.sleep(1)
                    s.send(password.encode())
                    data = s.recv(1024)
                    if data.decode() == '登陆成功':
                        print('登陆成功')
                        while True:
                            print('''============================
-1.查单词 2.查看记录 3.退出-
============================''')
                            n = input('请输入您要做的事情：')
                            if n not in ['1','2','3']:
                                print('请重新输入')
                            else:
                                if n == '1':
                                    s.send('1'.encode())
                                    while True:
                                        l = input('请输入您要查询的单词,输入##退出:')
                                        if l == '##':
                                            s.send('##'.encode())
                                            break
                                        s.send(l.encode())
                                        data = s.recv(1024)
                                        print(data.decode())
                                elif n == '2':
                                    s.send('2'.encode())
                                    data = s.recv(1024)
                                    print(data.decode())
                                elif n == '3':
                                    s.send('3'.encode())
                                    break
                    else:
                        print(data.decode())
                        continue
            elif cmd == '3':
                s.send('3'.encode())
                sys.exit('谢谢使用，欢迎下次再来')












if __name__ == '__main__':
    main()












