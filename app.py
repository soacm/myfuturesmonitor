import os
import datetime


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Use SQLite database

#db = SQL("sqlite:///project.db")

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#############################################################

@app.route("/")
@login_required
def index():
    if request.method == "GET":
        user_id = session["user_id"]
        user = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]["username"]
        return render_template("index.html", user = user)

#############################################################

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

#############################################################

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

#############################################################

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

    # Error checking
    if not username or not password or not confirmation or not email or password != confirmation:
        return apology("Check provided information!")

    # Using password function, then adding it with SQL db.execute
    hashedPassword = generate_password_hash(password)
    try:
        db.execute("INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", username, hashedPassword, email)
        return redirect("/")
    except:
        return apology("Select another Username")

######################### Pages #############################

@app.route("/usa")
@login_required
def usa():
    if request.method == "GET":
        favourites = db.execute("SELECT name FROM favourites")
        return render_template("usa.html", favourites = favourites)

@app.route("/europe")
@login_required
def europe():
    if request.method == "GET":
        favourites = db.execute("SELECT name FROM favourites")
        return render_template("europe.html",favourites = favourites)

@app.route("/favourites")
@login_required
def favourites():
    if request.method == "GET":
        # Get the watch list elements from the database
        favourites = db.execute("SELECT name FROM favourites")
        # Push to the front-end
        return render_template("favourites.html", favourites = favourites)

@app.route("/addfav", methods=["GET", "POST"])
@login_required
def addfav():
        if request.method == "POST":
            user = session["user_id"]
            name = request.form.get("submitbutton")
            # Insert into database
            db.execute("INSERT INTO favourites (user_id, name) VALUES (?, ?)", user, name)
            return redirect("/favourites")


@app.route("/clean", methods=["GET", "POST"])
@login_required
def clean():
    if request.method == "POST":
        # Empty the watch list
        db.execute("DELETE FROM favourites")
        return redirect("/favourites")

######################### Assets #############################

@app.route("/es")
@login_required
def es():
    if request.method == "GET":
        return render_template("es.html")

@app.route("/nq")
@login_required
def nq():
    if request.method == "GET":
        return render_template("nq.html")

@app.route("/ym")
@login_required
def ym():
    if request.method == "GET":
        return render_template("ym.html")

@app.route("/rty")
@login_required
def rty():
    if request.method == "GET":
        return render_template("rty.html")

@app.route("/dax")
@login_required
def dax():
    if request.method == "GET":
        return render_template("dax.html")

@app.route("/ftse")
@login_required
def ftse():
    if request.method == "GET":
        return render_template("ftse.html")

@app.route("/ftsemib")
@login_required
def ftsemib():
    if request.method == "GET":
        return render_template("ftsemib.html")

#############################################################


