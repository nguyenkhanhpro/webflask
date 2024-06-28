from flask import Flask,render_template,request,session
from models import * #import file model.py previously created
app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] ="khanh" #encode session
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql://root:@localhost/website"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) #tie db with flask app
def main():
    db.create_all() #create table
if __name__ == "__main__":
    with app.app_context(): #allow developer interact with flask via command line
        main()  
