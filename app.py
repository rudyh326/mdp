from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
	return jsonify("Hello World!")

@app.route('/bring',methods=['POST'])
def bring_req():
	req_data = request.get_json()
	return jsonify(req_data)

if __name__ == '__main__':
    app.run(debug = True)