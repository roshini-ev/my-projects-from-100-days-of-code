from flask import Flask, render_template, url_for
import requests
app = Flask(__name__)
URL = "https://api.npoint.io/674f5423f73deab1e9a7"

posts = requests.get(URL).json()

@app.route('/')
def index():
    return render_template("index.html",posts=posts)
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html",post=requested_post)

if __name__ == '__main__':

    app.run(debug=True)
