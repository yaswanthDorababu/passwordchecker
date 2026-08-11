# Password Strength Checker

## Project Overview

The Password Strength Checker is a web application developed using Python and Flask that evaluates the strength of a user-entered password. The application analyzes the password based on multiple security rules and provides instant feedback about its strength. It also displays a visual progress bar representing the password's security level.

---

# Objectives

* To help users create strong and secure passwords.
* To demonstrate the use of Flask for web application development.
* To implement password validation using Python regular expressions.
* To provide real-time password requirement checking using JavaScript.
* To improve user awareness about password security.

---

# Features

* Password strength analysis.
* Checks minimum password length.
* Detects uppercase letters.
* Detects lowercase letters.
* Detects numeric digits.
* Detects special characters.
* Real-time validation while typing.
* Dynamic progress bar showing password strength.
* User-friendly interface with HTML and CSS.
* Backend processing using Flask.

---

# Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask

## Python Modules

* re (Regular Expressions)
* Flask

---

# Functional Requirements

* User can enter a password.
* System validates password strength.
* System checks all password rules.
* System calculates a password score.
* System displays the strength as Weak, Good, or Excellent.
* System displays the password score using a progress bar.
* System provides immediate feedback to the user.

---

# Non-Functional Requirements

* Easy to use interface.
* Fast response time.
* Lightweight application.
* Easy to maintain.
* Portable across operating systems.
* Secure password validation logic.

---

# Password Validation Rules

The application checks whether the password contains:

* At least 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one numeric digit
* At least one special character

Each satisfied condition increases the password score.

---

# Software Requirements

* Python 3.x
* Flask
* Visual Studio Code
* Web Browser (Chrome, Edge, Firefox)

---

# Hardware Requirements

## Minimum

* Intel Core i3 Processor
* 4 GB RAM
* 500 MB Free Storage

## Recommended

* Intel Core i5 or above
* 8 GB RAM
* Windows 10/11 or Linux

---

# Project Structure

```
password_checker/
│
├── app.py
├── main.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    └── validation.js
```

---

# Working of the Project

1. User opens the Password Strength Checker webpage.
2. User enters a password.
3. JavaScript validates the password in real time.
4. The user clicks the **Analyze** button.
5. Flask receives the password.
6. Python calculates the password score.
7. Flask sends the result to the result page.
8. The application displays the password strength and progress bar.

---

# Advantages

* Improves password security awareness.
* Provides instant feedback.
* Easy to use.
* Lightweight and fast.
* Beginner-friendly Flask project.
* Easy to extend with additional security features.

---

# Future Enhancements

* Detect common passwords.
* Detect repeated characters.
* Detect sequential patterns (123456, abcdef).
* Password visibility toggle.
* Password generator.
* Password entropy calculation.
* Password breach detection using online APIs.
* Store password analysis history.
* Dark mode support.

---

# Conclusion

The Password Strength Checker is a simple and effective cybersecurity project that demonstrates the integration of Python, Flask, HTML, CSS, and JavaScript. It helps users create stronger passwords while providing practical experience in web development, backend programming, regular expressions, and client-side validation.
