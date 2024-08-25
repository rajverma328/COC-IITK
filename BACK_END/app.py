from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='../FRONT_END', template_folder='../FRONT_END')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ASSETS/<path:filename>')
def assets(filename):
    return send_from_directory('../ASSETS', filename)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
