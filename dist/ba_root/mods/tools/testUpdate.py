import _thread
import json
import requests

master = 'http://127.0.0.1:1234/'

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

if __name__ == '__main__':
    while True:
        choose = int(input("输入选择:"))
        match choose:
            case 1:
                data = {'name':"RuiCore BCS Test Server",
                        'port':str(43210),
                        'build':20995,
                        'bcsversion':78}
                postStatus(data)
            case 2:
                contributeData('/home/rui/rc/dist/ba_root/mods/README.md')
            case 3:
                data = {
                    'id':'account_id',
                    'display':'display_string',
                    'ip':'127.0.0.1',
                    'device':'device_id'}
                checkSpammer(data)
            case _:
                print('Unknown status code')