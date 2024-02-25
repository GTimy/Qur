from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import pyodbc
import pymysql
import datetime
from pprint import pprint
import mysql.connector
import json


###########
#Salut ajout Yacine 222222222222
##################

app = Flask(__name__)

@app.route('/ayahs/<int:surah_id>',methods=['GET'])
def get_ayahs(surah_id):

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='quran',
        charset='utf8mb4'
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT `text_ar` FROM `ayahs` WHERE `surah_id`="+str(surah_id))
    ayahs = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    return jsonify(ayahs)


@app.route('/', methods=['GET', 'POST'])

def index():  # put application's code here

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='quran',
        charset='utf8mb4'
    )

    sql = "SELECT id,name_ar FROM `surahs`"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    
    
    


    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/quran?charset=utf8mb4'
    # db = SQLAlchemy(app)
    #
    # class Surahs(db.Model):
    #     __tablename__ = 'surahs'  # Nom exact de la table dans la base de données
    #     id = db.Column(db.Integer, primary_key=True)
    #     number = db.Column(db.Integer, nullable=False)
    #     name_ar = db.Column(db.String(255), nullable=False)
    #     name_en = db.Column(db.String(255), nullable=False)
    #     name_en_translation = db.Column(db.String(255), nullable=False)
    #     type = db.Column(db.String(255), nullable=False)
    #     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    #
    # users = Surahs.query.all()
    # print(users)





    return render_template('index.html',surahs=myresult)


if __name__ == '__main__':
    app.run()
