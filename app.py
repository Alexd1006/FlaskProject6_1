from flask import Flask, render_template, request

app = Flask(__name__)

# Хранение всех анкет в памяти
all_users = []

@app.route('/', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        user_data = {
            'name': request.form.get('name'),
            'city': request.form.get('city'),
            'hobby': request.form.get('hobby'),
            'age': request.form.get('age')
        }
        all_users.append(user_data)
    return render_template('form.html', all_users=all_users)

if __name__ == '__main__':
    app.run(debug=True)
