from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify("Hello rudy")

req_data=0
@app.route('/data',methods=['POST'])
def data_req():
	global req_data
	req_data = request.get_json()
	return jsonify(req_data)

print(req_data)
# @app.route('/data/<string:name>')
# def get_data(name):
# 	return jsonify(name)




if __name__ == '__main__':
    app.run(debug = True)