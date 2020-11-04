# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 20:17:52 2020

@author: sushil.kasar
"""


import pandas as pd
import time
import schedule
import pymssql
from mattermostdriver import Driver

def attach_on_MM(from_id, msg_text, filename):
    try:
        SERVER_URL = ' '
        OK_BOT_USER = ''
        OK_BOT_PASSWORD = ''
        mm_client = Driver({
            'login_id':  ,
            'password': ,
            'url': SERVER_URL,
            'scheme': 'https',
            'basepath': '/api/v4',
            'verify': True,
            'port': 443,
            # 'auth': TokenAuth,
            'auth': None,
            'timeout': 30,
            'request_timeout': None,
            'debug': False
        })
        mm_client.login()
        # Currently logged in user.
        mm_bot_user = mm_client.users.get_user(user_id='')
        """
        create_channel_response = mm_client.channels.create_direct_message_channel([
            from_id,
            mm_bot_user['id']
        ])
        print("Created chanel: " + str(create_channel_response['id']))
        """
        # track the file id and pass it in `create_post` options, to attach the file
        # channels = mm_client.channels.get_channel_by_name(channel_name='hd-hourly-report', team_id='j16s68h77j8kxq8x9wr5fn8aqw'
        file_id = mm_client.files.upload_file(
            channel_id=from_id,
            files={'files': (filename, open(filename, 'rb'))}
            )['file_infos'][0]['id']
        mm_client.posts.create_post(options={
            'channel_id': from_id,
            'message': msg_text,
            'file_ids': [file_id]})
        mm_client.logout()
        return ('Responce 200')
    except:
        return ('Responce error')
    
def job():
    server=''
    username=''
    password=''
    db_name=''
    base_query= """
    
                """
    conn=pymssql.connect(server,username,password,db_name)
    drop_data=pd.read_sql(base_query,conn); conn.close()
    drop_data.to_csv("XX.csv", index=False)
    attach_on_MM(" #channel id", "#File name", "XX.csv")

if __name__ == "__main__":
    schedule.every().day.at("05:30").do(job) #scheduled at morning 5:30am.
    
    while True:
        schedule.run_pending()
        time.sleep(1)

#use this code for any alternate for sending attachment on 07:30 am.
if __name__ == "__main__":
    while True:
    
        hr = int(datetime.now(timezone('Asia/Kolkata')).time().hour)
        minute = int(datetime.now(timezone('Asia/Kolkata')).time().minute)
    if (hr == 7) & (minute == 30):
        for tries in range(10):
            print("====== TRY ====== :", tries+1)
            try:
                job()
                time.sleep(60)
                break
            except Exception as exc:
                print(str(exc))
                continue
    else:
        time.sleep(50)

