# Voor het starten van server het commando:
# set FLASK_APP=server.py vanaf normale command prompt
# set FLASK_ENV=development vanaf normale command prompt
# met alleen set commando kan je checken of deze gezet is
# server vanuit (venv) opstarten met flask run

from flask import Flask, render_template, url_for, request
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# Algemene route
@app.route('/<string:page_name>')
def htmlpage(page_name=None):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #return 'form submitted!'
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return 'Sorry, not saved to the database.'
    else:
        return "oops....thats not good!"

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file  = database.write(f"\n{email},{subject},{message}")
        # schrijf values naar file

def write_to_csv(data):
    with open('database.csv', newline='',  mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer  = csv.writer(database2, delimiter=",",  quotechar='"', quoting =csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        # schrijf values naar file



# @app.route('/index.html')
# def my_index():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# # @app.route('/about.html')
# # def about():
# #     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')


