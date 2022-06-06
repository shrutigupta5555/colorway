
from flask import Flask, render_template, send_from_directory, request
import os
import webcolors
from string_random import generate
from predict import predict_colors

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
            colors = predict_colors(f'static/{name}.jpg')
            colorname = []
            # for i in colors:
                # colorname.append(webcolors.hex_to_name(str(i)))
    return render_template('results.html', name = name, colors = colors, colorname=['red', 'red', 'red', 'red', 'red'])

@app.route('/link/<url>')
def link(url):
    return render_template('link.html', url=url)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
