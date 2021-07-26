from flask import Flask, request, jsonify
app = Flask(__name__)

import os
root_path = "/" + os.environ.get("HOSTNAME", "app")

# from queue import Queue
import queue
max_size = 3000
q = queue.Queue(maxsize=max_size)

# @app.route("/uwsgi01")
@app.route(root_path)
def hello():
    return "Hello 01"

@app.route(root_path + "/put", methods=["PUT"])
def put_s3path():
    # if q.full():
    #     raise
    try:
        q.put(s3path, block==True, timeout=60)
    except queue.Full as e:
        print(e)
    except Exception as e:
        # 予期せぬエラー
    print(f"put: qsize={q.qsize()}")
    return {}

@app.route(root_path + "/get", methods=["GET"])
def get_s3path():
    try:
        s3path = q.get(s3path, block==True, timeout=60)
    except queue.Empty as e:
        print(e)
    except Exception as e:
        # 予期せぬエラー
    print(f"get: qsize={q.qsize()}")
    return {}
# 
# @app.route('/', methods=['POST'])
# def post_json():
#     json = request.get_json()  # POSTされたJSONを取得
#     return jsonify(json)  # JSONをレスポンス

#from src import RefineDetDetectorCpu
#setting_file = "/app/src/setting.json"
#detector = RefineDetDetectorCpu(setting_file)
#detector.load_model()
#detector.set_transformer()
#
#@app.route("/", methods=["POST"])
#def example():
#    print("flask")
#    print("request.data", request.data)
#    # print("request.files", request.files, type(request.files))
#    # print(request.files["uploadFile"].filename)
#    # print(dir(request.files["uploadFile"]))
#    # print(request.files["uploadFile"])
#    # print(request.files["uploadFile"].stream)
#    print("request.files", type(request.files))
#    files = (request.files.items())
#    
#    for f in files:
#        image_binary = f[1].read()
#        det_results = detector.inference(image_binary)
#        
#    return jsonify(det_results)


#if __name__ == "__main__":
#    print("++++++++++++bbbbbbbbbbbb+++++++++++++++++++++++++++++++++++++++++++++++++++++")
#    app2.run()
#    print("++++++++++++aaaaaaaaaaaa+++++++++++++++++++++++++++++++++++++++++++++++++++++")
