
from flask import Flask, render_template, send_from_directory, request
import os
from string_random import generate
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
            uploaded_file.save(f'static/{name}.jpg')    
    return render_template('results.html', name = name)

@app.route('/link/<url>')
def link(url):
    return render_template('link.html', url=url)

if __name__ == "__main__":
  app.run(debug=True, use_reloader=True)
