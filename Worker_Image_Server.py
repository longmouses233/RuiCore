DEBUG = False

import logging  
import os  

logger = logging.getLogger('werkzeug')  
logger.setLevel(logging.ERROR)  
handler = logging.StreamHandler(open(os.devnull, 'w'))  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
handler.setFormatter(formatter)
logger.addHandler(handler)
  
from flask import Flask , request
app = Flask(__name__)

@app.route("/ping", methods=["POST"])
def get_server_info():
    data = request.json

    if(DEBUG):
        print(data)

    return 'ok'

@app.route("/uploaddata", methods=["POST"])
def save_file():
    data = request.files
    file = data['file']

    if(DEBUG):
        print(type(data))
        print(data)
        print(file.filename)

    # 文件写入磁盘
    file.save(file.filename)
    return 'ok'

@app.route("/checkspammer", methods=["POST"])
def get_client_info():
    data = request.json

    if(DEBUG):
        print(data)
        
    return 'ok'

if __name__ == '__main__':
    print('\033[1m\033[96mWorker Is Running\033[0m')
    app.run(host="0.0.0.0", port=1234, debug=DEBUG)
