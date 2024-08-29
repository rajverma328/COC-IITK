from flask import Flask, request, render_template, send_from_directory, jsonify
import course_schedule_manager as csm

app = Flask(__name__, static_folder='../FRONT_END', template_folder='../FRONT_END')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ASSETS/<path:filename>')
def assets(filename):
    return send_from_directory('../ASSETS', filename)

@app.route('/API/schedule/<course>', methods=['GET'])
def fetch_course_schedule(course):
    sched = csm.get_schedule(course)
    return jsonify(sched)

@app.route('/API/available', methods=['GET'])
def available_courses():
    selected_courses = request.args.getlist('courses[]')
    # print("Selected courses:", selected_courses)

    return jsonify("sched")

if __name__ == '__main__':
    print("Intialising the server")
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
