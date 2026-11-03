Python URL Shortner

About the project
python url shortner is a simple web application developed by sing python and flask . it convert the long url into shorener link using randomly generated six-character code
when user clicks the shortened URL,the website redirect them to the original websie.

Technologies Used
 python
 Flask
 HTML
 Random Module
 String Module
 CSS
 Java Script

features 
 convert the long urls into shot url
 generate random 6 character code
 stores url mapping using a python dictionary
 redirect the user to the original website
 handle invalid short url with a 404 response
 404 means request or response dosent exist on server

Installation and setup

clone the repository
     https://github.com/AshlinMirsha/url.git
Navigate to the project folder
    cd URL_SHORTER
In Terminal
     sudo apt install python3-venv
     python3 -m venv venv
     source venv/bin/activate
     pip install flask
     python app.py
open in browser
200 - homepage loads successfully
302 - users needs to be redirected
404 - requested URL dosent exist

Testing
pytest testing

Auther
Ashlin Mirsha R K
CSE student

