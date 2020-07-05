from flask import *
import os
import image_convertor as imgc
app = Flask(__name__)

imagelist = []
BG = imgc.Image.open("letters/bg.png")
sizeOfSheet =BG.width
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'

@app.route("/")
def home():
    cwd = os.getcwd()
    test=os.listdir(cwd)
    for item in test:
        if item.endswith(".pdf"):
            os.remove(item)
    for item in test:
        if item.endswith(".txt"):
            os.remove(item)
    return render_template("upload.html")

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
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
