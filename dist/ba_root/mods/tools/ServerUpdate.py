'''
处理服务器各种需要请求和上传到外部服务的连接器
'''
from playersData import pdata
import time
import _thread
import urllib.request
from efro.terminal import Clr
import json
import requests
import _ba
VERSION=78

# master = 'https://bcsservers.ballistica.workers.dev/'
master = 'http://127.0.0.1:1234/'

def check():

    data = {'name':_ba.app.server._config.party_name,
    'port':str(_ba.get_game_port()),
    'build': _ba.app.build_number,
    'bcsversion':VERSION}
    _thread.start_new_thread(updateProfilesJson,())
    _thread.start_new_thread(checkChangelog,())
    _thread.start_new_thread(postStatus,(data,))

def updateProfilesJson():
    '''更新玩家档案到JSON文件'''
    profiles=pdata.get_profiles()

    for id in profiles:
        if "spamCount" not in profiles[id]:
            profiles[id]["spamCount"]=0
            profiles[id]["lastSpam"]=time.time()

    pdata.commit_profiles(profiles)

def postStatus(data):
    '''
    上传服务器地址，BCS版本和BS构建版本号

    data = {'name':_ba.app.server._config.party_name,
            'port':str(_ba.get_game_port()),
            'build': _ba.app.build_number,
            'bcsversion':VERSION}
    '''
    res = requests.post(master+'ping',
        json=data)
    return res

def contributeData(data):
    '''
    上传文件

    data = file()
    '''
    res = requests.post(master+'uploaddata',
        files={'file': open(data, 'rb')})
    return res

def checkSpammer(data):
    '''
    攻击者检测

    data = {
        'id':account_id,
        'display':display_string,
        'ip':ip,
        'device':device_id}
    '''
    def checkMaster(data):
        res = requests.post(master+'checkspammer',
        json=data)
        # TODO handle response and kick player based on status
    _thread.start_new_thread(checkMaster,(data,))
    return

def fetchChangelogs():
    '''
    从Github获取BCS更新日志
    '''
    url="https://raw.githubusercontent.com/imayushsaini/Bombsquad-Ballistica-Modded-Server/public-server/dist/ba_root/mods/changelogs.json"

    if 2*2==4:
        try:
            data=urllib.request.urlopen(url)
            changelog=json.loads(data.read())
        except:
            return None
        else:
            return changelog

def checkChangelog():
    '''
    如果有可用更新，则将其显示到终端
    '''
    changelog=fetchChangelogs()
    if changelog==None:
        print(f'{Clr.BRED} UNABLE TO CHECK UPDATES , CHECK MANUALLY FROM URL {Clr.RST}',flush=True)
    else:
        msg=""
        avail=False
        for log in changelog:
            if int(log)>VERSION:
                avail=True

        if not avail:
            print(f'{Clr.BGRN}{Clr.WHT} YOU ARE ON LATEST VERSION {Clr.RST}',flush=True)
        else:
            print(f'{Clr.BYLW}{Clr.BLU} UPDATES AVAILABLE {Clr.RST}',flush=True)
            for log in changelog:
                if int(log)>VERSION:
                    msg=changelog[log]["time"]
                    print(f'{Clr.CYN} {msg} {Clr.RST}',flush=True)

                    msg=changelog[log]["log"]
                    print(f'{Clr.MAG} {msg} {Clr.RST}',flush=True)
