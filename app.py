from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) #  separer avec un /add
def home():
    if  request.method == 'POST':
        value = request.form['uploadfile']
        val = os.path.abspath(value)
        base_url = "http://10.0.0.138:8080/videobox/check"
        file = {'file': open(val, 'rb')} # open video file as binary
        r = requests.post(base_url, files=file) # we create full url for machinebox
        json_response = r.json() # json response
        return render_template('home.html', value=val, result=json_response['id'], status = json_response['status'])
  
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, port=9000)