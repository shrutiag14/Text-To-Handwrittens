# Text-To-Handwritten
Handwritten assignments are so boring. All you have to do is writing long pages and that too boring content.
So, To get rid of this boring work, I was thinking to create a software which will ease my work.

Here, is the link of the text to handwritten software.

Basically in this, You have to upload a .txt file and eventually it will convert into your own handwritten font as in the format of .pdf. Handwritten font can be changed, you can Upload your own letters in the letter folder section and can deploy on any server(i deployed it on heroku) and you can also run it on local server.

website link: https://text-to-hand.herokuapp.com/

LETTER FOLDER: It contains lowercase and uppercase letters and numbers as in png format

STATIC: where we placed any additional images which support web page.

TEMPLATES: This folder contains html file i.e success and upload file.
            Upload file used so that user can upload the file and after uploading success page prompt where the user can sucessfully download the pdf.

PROCFILE: Heroku web application requires procfile. This generally declare application process type. This procfile requires Gunicorn, the production web server. 

ImageConvertor.py: It contain python code which do the conversion.

server.py: It contain the code which deploy on the server.


