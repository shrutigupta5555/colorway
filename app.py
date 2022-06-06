
from flask import Flask, render_template, send_from_directory, request
import os
from colorname import rgb_name
from string_random import generate
from predict import predict_colors
import cv2
from resize import get_image

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    name = ""
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            name = generate()
            # name = "hehe"
            uploaded_file.save(f'static/{name}.jpg')
            image = get_image(f'static/{name}.jpg')
            
            height, width = image.shape[:2]
            print(height, width)
            h = height/400
            w = width/h
            image = cv2.resize(image, (int(w), int(400)))  
            cv2.imwrite(f'static/{name}2.jpg', image)
            colors = predict_colors(f'static/{name}2.jpg')
            colorname = []
            for i in colors:
                colorname.append(rgb_name(str(i)))
    return render_template('results.html', name = name, colors = colors, colorname=colorname)

@app.route('/link/<url>')
def link(url):
    return render_template('link.html', url=url)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
