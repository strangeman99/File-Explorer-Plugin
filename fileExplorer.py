from flask import Flask, request, jsonify, send_file, Response
import os

app = Flask(__name__)

@app.route('/find-file', methods=['POST'])
def findFile():
	# Handling request
	data = request.json
	fileName = data.get('name')
	dirInfo = data.get('dirInfo')

	# Defult directory
	if not dirInfo:
		dirInfo = 'C:\\'

	result = []
	allowedTypes = (['.txt'])

	# Searching all allowed types
	for curType in allowedTypes:
		name = fileName+curType

		# Walking top-down from the root
		for root, dir, files in os.walk(dirInfo):
			if name in files:
				result.append(os.path.join(root, name))
				break

	return jsonify(result)

# Define the API endpoint for the plugin logo
@app.route('/logo.png', methods=['GET'])
def plugin_logo():
    filename = 'logo.png'
    return send_file(filename, mimetype='image/png')

# To run the app locally
app.run(debug=True, host='127.0.0.1', port=8085)