from flask import Flask, request, jsonify
from client_pdf import PdfRpcClient
import json
from marshmallow import Schema, fields, ValidationError
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config["DEBUG"] = True


class UserDataSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    address = fields.String(required=True)

@app.route('/create_pdf', methods=['POST'])
def create_pdf():
    try:
        data = request.json
        validated_data = UserDataSchema().load(data)
        print("validated_data", validated_data, flush=True)
        required_keys = ['name', 'email', 'phone', 'address']
        if not all(key in validated_data for key in required_keys):
            return jsonify({'status': 'Error', 'message': 'Missing required keys'}), 400

        userdata = {key: validated_data[key] for key in required_keys}
        pdf = PdfRpcClient()

        logger.info("[x] Generating PDF")
        response = pdf.call(json.dumps(userdata))
        decoded_response = response.decode("utf-8")
        if decoded_response:

            logger.info("Request processed successfully")
            return jsonify({'status': 'Success', 'message': 'PDF Generated!'}), 200
        else:
            logger.info("Failed to generate PDF")
            return jsonify({'status': 'Error', 'message': 'Failed to generate PDF'}), 500
        
    except ValidationError as e:
        logger.error("Error...", str(e))
        return jsonify({"status": "Error", "message": str(e)}), 400

    except Exception as e:
        logger.error("Error...>>>", str(e))
        return jsonify({'status': 'Error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

