#-*-coding:utf-8 -*-
import sys
import requests
import ssl
import time
from config import *
#import logging
s = requests.Session()
getstatus='未初始化'
donestatus='未初始化'
loginstatus='未初始化'
normal-url="https://www.xxx.net/"#主站位置
post-url="//bbs.xxx.net/index.php?"#post时的jumpurl
login-url="https://www.xxx.net/login.php?"#登陆位置
login-url2="https://www.xxx.net/login.php"
day-get-url="https://www.xxx.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=15"#获取每日任务用的地址
day-got-url='https://www.xxx.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=15'#领取每日任务奖励地址

#log=open('/tmp/daylog.txt','r+')
#log.read()

reload(sys)
sys.setdefaultencoding('utf-8')

def slp():
    time.sleep(3)
def login(username,password):
    headers = {
           'Accept': 'text/html,application/xhtml+xml,*/*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN',
           'Cache-Control': 'no-cache',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }

    post_data = {
    'jumpurl':post-url,
    'step':'2',
    'cktime':'31536000',
    'lgt':'0',
    'pwuser':username,
    'pwpwd':password
    }
    s.headers.update(headers)
    login-url
    s.get(normal-url,verify=False)#取得正确的header
    slp()
    s.get(login-url,verify=False)
    slp()
    r=s.post(login-url2, data=post_data,verify=False)#登陆提交
    slp()
    #r.encoding = 'assci'
    #r.decoding= 'utf-8'
    global loginstatus
    #r.encoding='utf-8'
    #print r.text
    if "您已经顺利登录" in r.text:
        #print("login success!")
        loginstatus='成功'
    else:
        #print("login false!")
        loginstatus='失败'

def logout():
    s.cookies.clear()

def qiandaoday():
    get = s.get(daygeturl,verify=False)
    slp()
    done = s.get(day-got-url,verify=False)
    slp()
    global getstatus
    global donestatus
    if "完成" in get.text:
        #print("get-day-task-success")
        getstatus='成功'
    else:
        #print("get-day-task-false")
        getstatus='失败'
    if "完成" in done.text:
        #print("done-day-task-success")
        donestatus = '成功'
    else:
        #print("done-day-task-false")
        donestatus = '失败'



#sys.argv[0] 脚本名
#sys.argv[1] 模式
#sys.argv[2] 账号
#sys.argv[3] 密码
def main():
    time.sleep(10)
    for (i,j) in zip(username,password):
        login(i,j)
        qiandaoday()
        logout()
        reload(sys)
        sys.setdefaultencoding('GBK')
        temp='用户:',i,'本次签到时间:',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'签到模式:','day','登录状态',loginstatus,'获取任务',getstatus,'领取奖励',donestatus,'\n'
        temp=' '.join(temp)
        #logging.info(temp)
        #log.write(temp)
        print(temp)
        reload(sys)
        sys.setdefaultencoding('utf-8')
    #log.close()
main()
#app = main()