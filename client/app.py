from flask import Flask, request
from client_pdf import PdfRpcClient
import json

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/create_pdf', methods=['POST'])
def create_pdf():
    data = request.json
    print(data)
    name = data['name']
    email = email = data['email']
    phone = data['phone']
    address = data['address']
    userdata = {'name':name, 'email':email, 'phone':phone, 'address':address}
    pdf = PdfRpcClient()
    print(" [x] Generating  PDF")
    response = pdf.call(json.dumps(userdata))
    if response:
        decoded_response = response.decode("utf-8")
        return "<h1>"+decoded_response+"</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

