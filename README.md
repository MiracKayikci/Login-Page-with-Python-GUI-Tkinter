# Login Screen with Python GUI (Tkinter) 💻

This project creates a simple login screen using Python and the Tkinter library. The application is designed to demonstrate how to build a graphical user interface (GUI) with various components, including image assets, buttons, and text fields. The login screen allows users to enter a username and password, which are validated against predefined credentials. It also includes a GitHub button that opens the GitHub page of the project. 🚀

## Features 🌟

- A visually appealing login screen with a modern design 🖥️.
- Username and password fields with validation 🔑.
- A GitHub button that opens the project repository 💼.
- Real-time date and time display on the top of the window 🕒.
- A login attempt counter to restrict the number of failed login attempts ❌.

## Prerequisites 📋

To run this project, you need to have Python installed on your machine along with the `tkinter` library. `tkinter` is included with most Python installations by default, so no separate installation is usually required.

## Installation 🛠️

### Clone the Repository

To get started, first clone this repository to your local machine:

```bash
git clone https://github.com/MiracKayikci/Login-Screen-with-Python-GUI-Tkinter.git
```
## Folder Structure 📂
Once you've cloned the repository, the project structure should look like this:

Login-Screen-with-Python-GUI-Tkinter/ 

│
├── images/               
│   ├── login.png          
│   ├── adam.png           
│   ├── kilit.png          
│   ├── buyukresim.png     
│   └── github.png         
│
├── main.py                
├── ui_setup.py           
└── README.md              

The images/ folder contains all the image assets used in the application. The main.py file is the main application file where the logic for the login screen resides. The ui_setup.py file is used to organize and set up the user interface components.

## Usage 🚀
Run the Application
After cloning the repository, navigate to the project directory and run the following command:
```
python main.py
```

This will launch the login screen in a new window. You can enter the predefined username and password (admin:admin). If the credentials are correct, the window will close. If the credentials are incorrect, you will receive an error message, and your login attempts will be reduced. After three failed attempts, the program will exit.

## Components 🧩
Main Screen: The login screen consists of a user icon, a lock icon for password input, and a login button.

- GitHub Button: Clicking the GitHub button will open the project's repository in your web browser.
- Date and Time: The top of the window shows the current date and time, which is updated every second using the update_datetime function in main.py.
## Code Explanation 📚
- UI Setup: The ui_setup.py file handles the layout and visual components of the GUI. It defines how the window is divided into top, middle, and bottom frames. The middle section contains the user and password input fields, along with buttons for login and GitHub.

- Login Logic: The login logic in main.py validates the entered credentials. If the credentials are correct, the application closes. If they are incorrect, it shows an error message and decrements the attempts counter.

- Date and Time Update: The current date and time are displayed on the window and updated every second using the update_datetime function in main.py
