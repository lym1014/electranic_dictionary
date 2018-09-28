'''
name : Liyiming
date : 2018-9-28
email : 1242809365@qq.com
modules : pymysql
This is an electranic_dictionary server
'''

from socket import *
import os,time,signal,pymysql,sys,traceback


dict_path = './dict.txt'
host = '0.0.0.0'
post = 8888
addr = (host,post)
def main():
    sql1 = pymysql.connect('localhost','root','lym653512','electranic_dictionary')
    sql2 = sql1.cursor()
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(addr)
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            a,b = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except:
            traceback.print_exc()
            continue

        pid = os.fork()
        if pid == 0:
            while True:
                data= a.recv(1024)
                print(data.decode())
                if data.decode() == '1':
                    while True:
                        data1= a.recv(1024)
                        data2= a.recv(1024)

                        sql2.execute('select * from user_information where user_name = %s',[data1.decode()])
                        r = sql2.fetchone()
                        if r is None:
                            try:
                                sql2.execute('insert into user_information(user_name,password) values(%s,%s)',
                                             [data1.decode(), data2.decode()])
                                sql1.commit()
                                a.send('注册成功'.encode())
                                break
                            except:
                                a.send('注册失败'.encode())
                                break
                        else:
                            a.send('用户名已存在'.encode())
                            break
                elif data.decode() == '2':
                    while True:
                        data1 = a.recv(1024)
                        if data1.decode() == '##':
                            break
                        data2 = a.recv(1024)
                        sql2.execute('select * from user_information where user_name = %s and password = %s',[data1.decode(),data2.decode()])
                        r = sql2.fetchone()
                        if r is not None:
                            a.send('登陆成功'.encode())
                            while True:
                                data = a.recv(1024)
                                if data.decode() == '1':
                                    while True:
                                        data3 = a.recv(1024)
                                        if data3.decode() == '##':
                                            break
                                        sql2.execute('select maining from dictionary5 where word = %s',[data3.decode()])
                                        r = sql2.fetchone()
                                        if r is None:
                                            a.send('该单词不存在'.encode())
                                        else:
                                            a.send(r[0].encode())
                                            sql2.execute('insert into history1(name,word) values(%s,%s)',[data1.decode(),data3.decode()])
                                            sql1.commit()
                                elif data.decode() == '2':
                                    sql2.execute('select word,time from history1 where name = %s',[data1.decode()])
                                    r = sql2.fetchall()
                                    if r != ():
                                        a.send(str(r).encode())
                                    else:
                                        a.send('您未查询过任何单词'.encode())
                                elif data.decode() == '3':
                                    break
                        else:
                            a.send('登录失败，请重新输入'.encode())
                elif data.decode() == '3':
                    continue









if __name__ == '__main__':
    main()




