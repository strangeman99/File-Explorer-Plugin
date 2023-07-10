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

# Define the API endpoint for the plugin manifest
@app.route('/ai-plugin.json', methods=['GET'])
def plugin_manifest():
    host = request.headers['Host']
    with open('./ai-plugin.json') as f:
        text = f.read()
        return Response(text, mimetype='text/json')

# Define the API endpoint for the OpenAPI specification
@app.route('/openapi.yaml', methods=['GET'])
def openapi_spec():
    host = request.headers['Host']
    with open('./openapi.yaml') as f:
        text = f.read()
        return Response(text, mimetype='text/yaml')

# To run the app locally
app.run(debug=False, host='127.0.0.1', port=8085)