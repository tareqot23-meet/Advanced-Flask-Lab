from    flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://scontent.ftlv21-1.fna.fbcdn.net/v/t31.18172-1/1502644_10152506946962507_2442851309927378964_o.png?stp=c49.0.148.148a_dst-png_p148x148&_nc_cat=111&ccb=1-7&_nc_sid=1eb0c7&_nc_ohc=d-R_wjIm2d8AX_NugPv&_nc_ht=scontent.ftlv21-1.fna&oh=00_AT8CSjiG8-biys_qQ9tU-yrxzJSp6HANxsz5c3mFVk-G2Q&oe=62FD0A1B"

user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."

posts = {
    "https://scontent.ftlv1-1.fna.fbcdn.net/v/t39.30808-6/243021542_10158462822407507_4186737446569136175_n.jpg?stp=cp0_dst-jpg_e15_fr_q65&_nc_cat=101&ccb=1-7&_nc_sid=ed5ff1&_nc_ohc=nHa7N_8RkP0AX92LvUb&_nc_ht=scontent.ftlv1-1.fna&oh=00_AT8kLSHR6V-bvFjpXVVzHXWXviYhBJgkgHANsGlmTojibg&oe=62E08013": "2021 cohort's Y3 Accelerator!",
    "https://media-exp1.licdn.com/dms/image/C4D1BAQFTbpgMk3KTSg/company-background_10000/0/1614595305396?e=1659178800&v=beta&t=OiSIvxsPJiJkArJIzBCKVF0_-yEta9gv1qLVnViU8bo": "MEET graduation!",
    "https://pbs.twimg.com/media/FPvsO6xVkAEcrBm?format=jpg&name=900x900": "#Throwback to one of our favorite #MEETsummer events: #BowlingNight!",
    "https://pbs.twimg.com/media/FI_UkcnVIAAUvWN?format=jpg&name=medium": "2020 cohort in their Y1 summer!"}




@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html',image_link= image_link,user_bio=user_bio,posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
