<h2>NoteBUDDY - Online Note Sharing Platform</h2>
NoteBUDDY is a Django-based web application that allows users to create, publish, and manage their notes online. Users can perform CRUD (Create, Read, Update, Delete) operations on their notes, and they have the option to publish notes for others to access on the Global Notes Zone. The project ensures user privacy through a robust user authentication system, allowing users exclusive access to their unpublished notes.

You can take a quick walkthrough of the project here --> https://youtu.be/6BuIg4eB66o

<h4>Features</h4>
<b>User Authentication:</b> Secure user accounts with authentication and authorization.<br>
<b>CRUD Operations:</b> Users can Create, Read, Update, and Delete their notes.<br>
<b>Privacy:</b> Unpublished notes are private to the user, ensuring data confidentiality.<br>
<b>Global Notes Zone:</b> Users can publish notes for others to access in the Global Notes Zone.

<h4>How to Run the Project</h4>
Follow these steps to run the NoteBUDDY project on your local machine:

<h4>Prerequisites</h4>
Python installed on your machine.
pip (Python package installer) installed.

<h4>Clone the Repository</h4>
--->   git clone https://github.com/your-username/NoteBUDDY.git
       cd NoteBUDDY

<h4>Create a Virtual Environment (Optional but recommended)</h4>
--->   python -m venv venv
       Activate the virtual environment:

<h4>For Windows:</h4>
--->   .\venv\Scripts\activate
<h4>For MacOS/Linux:</h4>
--->   source venv/bin/activate

<h4>Install Dependencies</h4>
--->   pip install -r requirements.txt

<h4>Apply Database Migrations</h4>
--->   python manage.py migrate

<h4>Create Superuser (Admin)</h4>
--->   python manage.py createsuperuser
    Follow the prompts to create a superuser account.

<h4>Run the Development Server</h4>
--->   python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the NoteBUDDY application.

Access Admin Panel<br>
Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials created earlier.
