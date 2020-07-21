from flask import Flask, request, abort
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def eb101():
    return '{"userId":1,"userName":"xiaoming"}'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)

