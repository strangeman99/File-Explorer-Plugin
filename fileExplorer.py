from flask import Flask, request, jsonify, send_file, Response
import os

app = Flask(__name__)

@app.route('/find-file', methods=['POST'])
def findFile():
	# Handling request
	data = request.json
	fileName = data.get('name')
	dirInfo = data.get('dirInfo', 'C:\\')

	result = []
	allowedTypes = ('.txt')

	# Walking top-down from the root
	for root, dir, files in os.walk(dirInfo):
		# Only searching for files of the allowed type
		files = [file for file in files if not file.endswith(allowedTypes)]
		if fileName in files:
			result.append(os.path.join(root, fileName))

	return jsonify(result)

# To run the app locally
app.run(debug=True, host='127.0.0.1', port=6969)