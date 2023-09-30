from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.secret_key = 'ashik'
users = [{'username': 'user', 'password': 'password'}]
blog_posts = []

@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html', posts=blog_posts, username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and bcrypt.check_password_hash(user['password'], password):
                session['username'] = username
                flash('Logged in successfully', 'success')
                return redirect(url_for('home'))
        flash('Login failed. Check your credentials.')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = {'username': username, 'password': hashed_password}
        users.append(new_user)
        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if 'username' in session:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            new_post = {'title': title, 'content': content, 'author': session['username']}
            blog_posts.append(new_post)
            flash('Blog post added successfully', 'success')
            return redirect(url_for('home'))
        return render_template('add_post.html')
    return redirect(url_for('login'))

@app.route('/edit_post/<int:index>', methods=['GET', 'POST'])
def edit_post(index):
    if 'username' in session:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            blog_posts[index] = {'title': title, 'content': content, 'author': session['username']}
            flash('Blog post edited successfully', 'success')
            return redirect(url_for('home'))
        return render_template('edit_post.html', post=blog_posts[index])
    return redirect(url_for('login'))

@app.route('/delete_post/<int:index>')
def delete_post(index):
    if 'username' in session:
        del blog_posts[index]
        flash('Blog post deleted successfully', 'success')
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/add_comment/<int:index>', methods=['POST'])
def add_comment(index):
    if 'username' in session:
        if request.method == 'POST':
            comment = request.form['comment']
            blog_posts[index].setdefault('comments', []).append({'author': session['username'], 'comment': comment})
            flash('Comment added successfully', 'success')
        return redirect(url_for('home'))
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
