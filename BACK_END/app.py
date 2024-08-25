from flask import Flask, render_template, send_from_directory, jsonify
import course_schedule

app = Flask(__name__, static_folder='../FRONT_END', template_folder='../FRONT_END')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ASSETS/<path:filename>')
def assets(filename):
    return send_from_directory('../ASSETS', filename)

@app.route('/API/schedule/<course>', methods=['GET'])
def fetch_course_schedule(course):
    sched = course_schedule.get_schedule(course)
    return jsonify(sched)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
