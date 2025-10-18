from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from Flaskapp.models import BlogPost, User ,Question
from Flaskapp.forms import PostForm, RegistrationForm, LoginForm
from Flaskapp import db

main=Blueprint('main',__name__)

@main.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

# Post details by specific post_id
@main.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('post.html', post=post)


# Create a new post
@main.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if 'user_id' not in session:
        flash('You need to login first!')
        return redirect(url_for('main.login')) # if the user not loggedin then it redirects to login page

    if form.validate_on_submit():
        new_post = BlogPost(title=form.title.data,content=form.content.data,
            user_id=session['user_id'])
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('main.index'))
    return render_template('create.html', form=form)

# Edit post
@main.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if 'user_id' not in session or post.user_id != session['user_id']:
        flash("You can't edit this post!")
        return redirect(url_for('main.index'))

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.add(title=post.title,content=post.content)
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('main.post', post_id=post.id))
    return render_template('edit.html', form=form,post=post)

# Delete post
@main.route('/delete/<int:post_id>')
def delete(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if 'user_id' not in session or post.user_id != session['user_id']:
        flash("You can't delete this post!")
        return redirect(url_for('main.index'))

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!')
    return redirect(url_for('main.index'))

# to post a question
@main.route('/question',methods=["GET","POST"])
def question():
    questions = Question.query.all()
    if request.method == 'POST':
        content = request.form.get('content', '').strip()
        answer = request.form.get('answer', '').strip()
        if content and answer:
            new_question = Question(content=content, answer=answer)
            db.session.add(new_question)
            db.session.commit()
            flash('Question added successfully!', 'success')
            return redirect(url_for('main.question'))
    return render_template('question.html',questions=questions)

# Register
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

# Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            flash('Logged in successfully!')
            return redirect(url_for('main.index'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

# Logout
@main.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully')
    return redirect(url_for('main.index'))
