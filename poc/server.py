from flask import Flask, render_template, request, redirect, url_for, jsonify
from data import sequences_data
from method import *
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would typically check the credentials
        username = request.form['username']
        password = request.form['password']
        if checkLogin(username,password):
            return redirect(url_for('main'))
        else:
            return redirect(url_for('main'))
        # For now, we'll just redirect to home if a username and password are provided

    else:
        return redirect(url_for('main'))


    

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/tool')
def tool():
    selected_class = request.form.get('classSelect', list(sequences_data.keys())[0])
    sequences = sequences_data[selected_class]
    return render_template('tool.html', sequences_data=sequences_data)

@app.route('/get_sequences', methods=['GET', 'POST'])
def get_sequences():
    print("get_sequences route was called")
    class_name = request.form.get('class_name')
    sequences = sequences_data.get(class_name, [])
    return jsonify(sequences)

@app.route('/update_status', methods=['POST'])
def update_status():
    sequence_title = request.form['sequence_title']
    class_name = request.form['class_name']
    action = request.form['action']

    if action == 'join' or action == 'start':
        status = 'In Progress'
        userStatus = 'In'
    elif action == 'end':
        status = 'Finished'
        userStatus = 'Out'
    sequences_data[class_name] = [seq if seq['title'] != sequence_title else {'title': seq['title'], 'status': status,'summary':seq['summary'] ,'userStatus': userStatus} for seq in sequences_data[class_name]]
    return redirect(url_for('tool'))


if __name__ == '__main__':
    app.run(debug=True)
