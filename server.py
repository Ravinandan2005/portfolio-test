from flask import Flask , render_template, url_for, request, redirect
import csv

app = Flask(__name__)
@app.route("/")#Default site
def default():
    return render_template('index.html')

@app.route("/<string:page_name>")#get input from the click and paste accordingly
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}\t{subject}\t{message}')

def write_to_csv(data):
    with open('database.csv', newline = '',mode='a') as database1:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database1,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])#Post is the one used to post and get is used to get data
def submit_form():
    if request.method == 'POST':# If the method is post where we have given in contact.html
        try:
            data = request.form.to_dict()#getting every data as dictionary 
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return "Oh File Not Saved To Database !"   
    else:
        return "Something Wwnt Wrong !"



if __name__ == '__main__':
    app.run(debug=True)#debug is used to apply changes if we save the python file instead of running again