from flask import Flask, render_template, redirect, url_for, request
import requests
import uuid

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skillsandprojects')
def skillsandprojects():
    skills_data = {
        "technical": [
            "Front-End: HTML5, CSS3, JavaScript (DOM manipulation, APIs)",
            "Back-End: Python, Flask (building a project management tool)"
        ],
        "soft": [
            "Problem-solving (debugging complex errors)",
            "Self-learning (documenting my coding journey)"
        ]
    }
    return render_template('skillsandprojects.html', skills=skills_data)

@app.route('/leaveamessage', methods=['GET', 'POST'])
def leaveamessage():
    submitted_data = None

    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        message = request.form.get('message')

        # Generate a unique UUID for this message
        unique_id = str(uuid.uuid4())

        # Pack form data into a dictionary
        submitted_data = {
            "id": unique_id,
            "name": name,
            "location": location,
            "message": message
        }
        response = requests.post("https://json-alura-geek.vercel.app/users", submitted_data)
        redirect('/leaveamessage')
        
    try:
        response = requests.get("https://json-alura-geek.vercel.app/users")
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Error fetching API data: {e}")
    return render_template('leaveamessage.html', messages=data)

if __name__ == '__main__':
    app.run(debug=True, port = 3000)