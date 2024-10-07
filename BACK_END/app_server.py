import os
from flask import Flask, request, render_template, send_from_directory, jsonify
import BACK_END.course_schedule_manager_server as csm

app = Flask(__name__, static_folder='../FRONT_END', template_folder='../FRONT_END')

# Load configurations from environment variables
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1']
app.config['HOST'] = os.getenv('FLASK_HOST', '0.0.0.0')
app.config['PORT'] = int(os.getenv('FLASK_PORT', 5000))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ASSETS/<path:filename>')
def assets(filename):
    return send_from_directory('../ASSETS', filename)

@app.route('/API/schedule/<course>', methods=['GET'])
def fetch_course_schedule(course):
    try:
        sched = csm.get_schedule(course)
        return jsonify(sched)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/API/available', methods=['GET'])
def available_courses():
    try:
        selected_courses = request.args.getlist('courses[]')
        return csm.get_available_courses(selected_courses)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Initializing the server in production mode")
    # Ensure WSGI server like Gunicorn is used in production, not Flask's built-in
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

