import os
from flask import Flask

app = Flask(__name__)

# Get build info from file if it exists (created by pipeline)
build_info = "Build info not found."
build_info_path = os.path.join(os.path.dirname(__file__), 'buildinfo.txt')
if os.path.exists(build_info_path):
    try:
        with open(build_info_path, 'r') as f:
            build_info = f.read().replace('\n', '<br>') # Read and format for HTML
    except Exception as e:
        build_info = f"Error reading build info: {str(e)}"

@app.route('/')
def hello_world():
    # Display hello message and build info
    return f"""
    <h1>Hello World from Python Flask App!</h1>
    <h2>Deployed via Azure DevOps.</h2>
    <hr>
    <h3>Build Information:</h3>
    <pre>{build_info}</pre>
    """

if __name__ == '__main__':
    # Run the app (useful for local testing)
    # Azure App Service will use a production WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=8000)