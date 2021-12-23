from fpdf import FPDF
import time
import json

def create(userdata):
    try:
        userdata = json.loads(userdata)
        text = ""
        for key,value in userdata.items():
            text += 'My '+key+' is : '+value+ "\n"
        # time.sleep(2)
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=20)
        pdf.cell(200, 10, txt=text, ln=1, align="L")
        pdf.output("test.pdf")
        return "PDF Created !"
    except Exception as e:
        return "Error Creating PDF !"