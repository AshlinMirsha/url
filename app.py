from flask import Flask , request,redirect,render_template_string
import string
import random
app=Flask(__name__)
URL_database={}
def generate_short_url():
    character=string.ascii_letters+string.digits
    return "".join(random.choices(character,k=6))
# homepage route
@app.route('/',methods=['GET','POST'])
def home():
    short_url=""
    if request.method=='POST':
        original_url=request.form['URL']
        code = generate_short_url()
        URL_database[code]=original_url
        short_url=request.host_url+code
    return render_template_string("""
        <h1>Python URL shortener</h1>
        <form method="POST">
            <input type="url" name="URL" placeholder ="Enter your long URL" required>
            <button type="submit">shorten URL</button>
            </form>
            <h3>{{short_url}}</h3>
            """,short_url=short_url)
#route for redirecting to the original url
@app.route('/<code>')#dynamic url parameter
def redirect_url(code):
    original_url=URL_database.get(code)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found",404
if __name__=="__main__":
    app.run(debug=True)




