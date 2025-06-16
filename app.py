from flask import Flask, render_template,url_for,redirect,render_template, request,flash
import sqlite3
app = Flask(__name__)
app.secret_key = 'bharat_portfolio'
def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact',methods =['POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        message = request.form['message']
        conn = get_connection()
        query = 'insert into contact(email,name, message) values(?,?,?)'
        cursor = conn.cursor()
        cursor.execute(query,(email,name, message))
        conn.commit()
        conn.close()
        flash("Message sent successfully!", "success")
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)