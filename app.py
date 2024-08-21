from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity
budget_data = []

@app.route('/')
def index():
    return render_template('index.html', budget_data=budget_data)

@app.route('/add', methods=['POST'])
def add_entry():
    description = request.form.get('description')
    amount = float(request.form.get('amount'))
    budget_data.append({'description': description, 'amount': amount})
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_entry(index):
    if 0 <= index < len(budget_data):
        budget_data.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

