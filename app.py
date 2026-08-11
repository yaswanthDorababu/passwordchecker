from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash

from main import passwordchecker
from database import (
create_tables,
create_user,
get_user_by_email,
save_history,
get_history,
get_dashboard_stats
)


app = Flask(__name__)
app.secret_key = "password-checker-secret-key"

create_tables()

# ==========================================
# HOME
# ==========================================
@app.route("/")
def index():
    return render_template(
        "index.html",
        user_name=session.get("user_name")
    )


# ==========================================
# PASSWORD RESULT
# ==========================================
@app.route("/result", methods=["POST"])
def checking():
    password = request.form.get("password", "")
    result, score = passwordchecker(password)

    common = False
    try:
        with open(
            "common_passwords.txt",
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:
            common_password_list = {
                line.strip().lower()
                for line in file
                if line.strip()
            }

        if password.lower() in common_password_list:
            common = True

    except FileNotFoundError:
        print("common_passwords.txt not found")

    # Save password history if user is logged in
    if "user_id" in session:
        save_history(
            session["user_id"],
            result,
            score,
            common
        )

    return render_template(
        "result.html",
        result=result,
        score=score,
        common=common
    )


# ==========================================
# REGISTER
# ==========================================
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not name or not email or not password:
            error = "Please fill in all fields."
        else:
            user_id = create_user(name, email, password)
            if user_id is None:
                error = "An account with this email already exists."
            else:
                return redirect(url_for("login"))

    return render_template("register.html", error=error)


# ==========================================
# LOGIN
# ==========================================
@app.route("/login", methods=["GET", "POST"])
def login():
    print("LOGIN ROUTE:", request.method)

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        print("EMAIL:", email)
        user = get_user_by_email(email)
        print("USER:", user)

        if user is None:
            print("USER NOT FOUND")
            return render_template("login.html", error="Email not registered.")

        if check_password_hash(user["password"], password):
            print("PASSWORD MATCHED")

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_email"] = user["email"]

            print("LOGIN SUCCESS")
            print("USERNAME:", user["name"])

            return redirect(url_for("index"))

        print("PASSWORD DID NOT MATCH")
        return render_template("login.html", error="Incorrect password.")

    return render_template("login.html")


# ==========================================
# LOGOUT
# ==========================================
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ==========================================
# DASHBOARD
# ==========================================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    history_data = get_history(session["user_id"])
    total_checks = len(history_data)

    excellent_count = 0
    good_count = 0
    weak_count = 0

    for item in history_data:
        result = item["result"]

        if result == "Excellent":
            excellent_count += 1
        elif result == "Good":
            good_count += 1
        else:
            weak_count += 1

    if total_checks > 0:
        strong_percentage = round((excellent_count / total_checks) * 100)
    else:
        strong_percentage = 0

    recent_history = history_data[:3]

    return render_template(
        "dashboard.html",
        total_checks=total_checks,
        excellent_count=excellent_count,
        good_count=good_count,
        weak_count=weak_count,
        strong_percentage=strong_percentage,
        recent_history=recent_history,
        user_name=session.get("user_name")
    )









# ==========================================
# PASSWORD GENERATOR
# ==========================================
@app.route("/generator")
def generator():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("generator.html")


# ==========================================
# PASSWORD HISTORY
# ==========================================
@app.route("/history")
def history():
    if "user_id" not in session:
        return redirect(url_for("login"))

    history_data = get_history(session["user_id"])
    return render_template("history.html", history=history_data)


# ==========================================
# PROFILE
# ==========================================
@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = get_user_by_email(session["user_email"])

    if user is None:
        session.clear()
        return redirect(url_for("login"))

    return render_template(
        "profile.html",
        user=user
    )


# ==========================================
# RUN APPLICATION
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)
