from flask import *
import os
import image_convertor as imgc
app = Flask(__name__)

imagelist = []
BG = imgc.Image.open("Letters/bg.png")
sizeOfSheet =BG.width
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'

def del_old():
    cwd = os.getcwd()
    test=os.listdir(cwd)
    for item in test:
        if item.endswith(".pdf") or item.endswith(".png") or item.endswith(".txt"):
            os.remove(item)
            
@app.route("/")
def home():
    return render_template("upload.html")

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':
        del_old()
        f = request.files['file'] 
        f.save(f.filename) 
        img = imgc.convertor(BG,sizeOfSheet,allowedChars)
        img.run(f.filename)
        img.makeimage()
        img.makepdf()
        return render_template("success.html", name = f.filename)




@app.route('/download', methods = ['POST','GET'])
def download():
    return send_file("final.pdf", as_attachment=True)

if __name__ == "__main__":
   app.run(threaded = True)
