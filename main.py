import sys

from flask import Flask, render_template, logging
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import data_required,email_validator
from flask_bootstrap import Bootstrap
from flask_mail import Mail,Message
app=Flask(__name__)




app.secret_key="MohamedAli123456"
Bootstrap(app)
app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] ='mohamedalisaifudeen1@yahoo.com'
app.config['MAIL_PASSWORD'] ='opionphuapgtbfyj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail=Mail(app)
mail.init_app(app)
class Mytform(FlaskForm):
    name=StringField("Name",validators=[data_required()])
    email=StringField("Email")
    message=TextAreaField("Message",validators=[data_required()])
    submit=SubmitField("Message me",validators=[data_required()])

@app.route("/",methods=['Get',"Post"])
def home():
    form=Mytform()
    if(form.validate_on_submit()):
        msg = Message(
            'Hello Message from Portfolio Project',
            sender='mohamedalisaifudeen1@yahoo.com',
            recipients=['mohamedalisaifudeen2@yahoo.com']
        )
        msg.body = f"name:-{form.name.data}\n Email: {form.email.data}\n Message: {form.message.data}"
        mail.send(msg)
    return render_template("base.html",form1=form)

if(__name__=='__main__'):
    app.run(debug=True)