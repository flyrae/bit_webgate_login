#coding:utf-8
import requests
import time
user_name = '学号'
password = '密码'
post_dict_login = {
        'username': user_name,
        'password': password,
        'action': 'login',
        'ac_id': '1',
        'user_ip': '',
        'nas_ip': '',
        'user_mac': '',
        'save_me': '1',
        'ajax': '1'
    }

post_dict_logout = {
        'username': user_name,
        'password': password,
        'action': 'logout',
        'ac_id': '1',
        'user_ip': '',
        'nas_ip': '',
        'user_mac': '',
        'save_me': '1',
        'ajax': '1'
    }
logging_post = 'http://10.0.0.55:801/srun_portal_pc.php'
web_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        
    }

# r = requests.post(logging_post, data=post_dict_login,headers=web_headers)

def login():
    r = requests.post(logging_post, data=post_dict_login,headers=web_headers)
    if r.text == 'IP has been online, please logout.':
        logout()
        r = requests.post(logging_post, data=post_dict_login,headers=web_headers)
    return r.text.encode('utf-8')

def logout():
    r = requests.post(logging_post, data=post_dict_login,headers=web_headers)
    return r.text.encode('utf-8')

def main():
    while True:
        time.sleep(60*60)
        login()

if __name__ == '__main__':
    print 'start:'
    main()

