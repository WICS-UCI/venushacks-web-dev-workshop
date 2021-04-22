# Python Library Imports

#Flask App
from flask import Flask, request, render_template, redirect

# Creating Flask App object
app = Flask(__name__, template_folder="templates")

expenses = []

# Each method in the Flask app is tied to a url, which is wriiten using '@app.route()'
@app.route('/')
def root():
    # Default an HTML page
    return render_template('index.html')

@app.route('/add-page')
def add_page():
    return render_template('add.html')

@app.route('/view-page')
def view_page():
    return render_template('view.html', category="all")

@app.route('/view-cat', methods=['POST'])
def change_category():
    category = request.form['cat']
    return redirect('/view/' + category)
    
# Regular GET method (doesn't receive information, sends back information)
@app.route('/view/<category>')
def view(category):
    if category == 'all':
        data= expenses
    else:
        data =  [i for i in expenses if i['category'] == category]
    return render_template('view.html', category=category, data=data)

# POST method (receives information, sends back information)
@app.route('/add', methods=['POST'])
def add_item():
    item = {'item': request.form['item'], 'amount': request.form['amount'], 'category': request.form['category']}
    expenses.append(item)
    return redirect('view/all')

# Runs Flask App
if __name__ == "__main__":
    app.run()