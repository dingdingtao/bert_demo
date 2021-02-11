from flask import Flask, request, jsonify
import json
from bert_base.client import BertClient
import time
import numpy as np



def main_cli ():
    pass
    parser = argparse.ArgumentParser(description='API demo server')
    parser.add_argument('-ip', type=str, default="0.0.0.0",
                        help='chinese google bert model serving')
    parser.add_argument('-port', type=int, default=8910,
                        help='listen port,default:8910')

    args = parser.parse_args()

    flask_server(args)



# list 转成Json格式数据
def list_to_json(lst):
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    
    return str_json

app = Flask(__name__)

@app.route('/api/v0.1/query', methods=['POST'])
def class_pred():
    if  not request.data:   #检测是否有数据
        return ('fail')

    student = request.data.decode('utf-8')
    list_text = json.loads(student)['text']
    #print("total setance: %d" % (len(list_text)), list_text)
    with BertClient(ip='localhost', port=5575, port_out=5576, show_server_config=False, check_version=False, check_length=False, timeout=10000 ,  mode='CLASS') as bc:
        #start_t = time.perf_counter()
        rst = bc.encode(list_text)
        #print('result:', rst)
        #print('time used:{}'.format(time.perf_counter() - start_t))
    result_txt = list_to_json(rst)

    return result_txt


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)