from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

my_email = "YOUR EMAIL"
password = "YOUR_PASSWORD"

blog_url = "https://api.npoint.io/6004372280faf0feb361"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", all_post= all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["username"])
        print(data["email"])
        print(data["phone"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def read_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', request_post=requested_post)

def send_email(name, email, phone, message):

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send



# @app.route('/form-entry', methods=["POST"])
# def receive_data():
#




if __name__  == "__main__":
    app.run(debug=True)