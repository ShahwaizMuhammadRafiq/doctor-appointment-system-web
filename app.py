#we will use flask and imports its feature to get html and css interface 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# we will use list because they are mutable(can be change) to store user data,we can also use dictionary
appointments = []
#app route is used to connect css and html
@app.route('/')
def home():
    return render_template('home.html')

#
@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        appointments.append({'name': name, 'date': date, 'time': time})
        return redirect(url_for('book_appointment'))

    return render_template('appointment.html', appointments=appointments)

#we will imagine some appointments to edit
appointments = [...]

@app.route('/edit_appointment/<int:index>', methods=['GET', 'POST'])
def edit_appointment(index):
    if 0 <= index < len(appointments):
        if request.method == 'POST':
            #use for edit and update the data in the list thats why we will use index
            appointments[index] = {
                'name': request.form['name'],
                'date': request.form['date'],
                'time': request.form['time']
            }
            # than we will return to appointment page after the return
            return redirect(url_for('appointments'))

        # template to render the edit appointment html appointment page
        return render_template('edit_appointment.html', appointment=appointments[index], index=index)

    # if ined is out of range it will go to appointment page again
    return redirect(url_for('appointments'))

@app.route('/remove_appointment/<int:index>')
def remove_appointment(index):
    del appointments[index]
    return redirect(url_for('book_appointment'))

@app.route('/about')
def about():
    return render_template('about.html')
#this is a feature of flask  it will give us debug and check  errors and if main is a script that runs on main program
if __name__ == '__main__':
    app.run(debug=True)
