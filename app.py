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
    contact_list = [
        { 
        "social_media":"GitHub",
        "link_of_social_media": "https://github.com/thierry-chatauan",
        "icon": "github-icon.png"
    },
    {
        "social_media":"LinkedIn",
        "link_of_social_media": "https://ie.linkedin.com/in/thycbs",
        "icon": "icons8-linkedin-50.png"
    }
    ]
    
    return render_template('contact.html', contact_list = contact_list)

@app.route('/skillsandprojects')
def skillsandprojects():
    skills_data = {
        "technical": [
            "Front-End: HTML5, CSS3, JavaScript (DOM manipulation, APIs)",
            "Back-End: Python, Flask (building this portifolio project )"
        ],
        "soft": [
            "Self-learning (documenting my coding journey)"
        ]
    }
    projects = [
    {
        "name_of_project": "Web page developed with HTML and CSS",
        "link_of_project": "https://thierry-chatauan.github.io/ucd-website-project/"
    },
    {
        "name_of_project": "To-do list built with vanilla JavaScript",
        "link_of_project": "https://thierry-chatauan.github.io/ucd_js_project/"
    }
]
    return render_template('skillsandprojects.html', skills=skills_data, projects=projects)


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
        response = requests.post("https://674edcf2bb559617b26d0bca.mockapi.io/api/v1/users", submitted_data)
        redirect('/leaveamessage')
        
    try:
        response = requests.get("https://674edcf2bb559617b26d0bca.mockapi.io/api/v1/users")
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Error fetching API data: {e}")
    return render_template('leaveamessage.html', messages=data)

if __name__ == '__main__':
    app.run(debug=True, port = 3000)