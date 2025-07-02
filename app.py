from flask import Flask, render_template, abort, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Sample in-memory posts
dummy_posts = [
    {"id": 1, "title": "Welcome to My Blog", "content": "This is the first post on my new blog!"},
    {"id": 2, "title": "Another Post", "content": "Here is another interesting post."}
]

def get_next_id():
    return max((p['id'] for p in dummy_posts), default=0) + 1

@app.route('/')
def index():
    return render_template('index.html', posts=dummy_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((p for p in dummy_posts if p["id"] == post_id), None)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('add_post'))
        dummy_posts.append({
            'id': get_next_id(),
            'title': title,
            'content': content
        })
        flash('Post added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_edit.html', action='Add', post={})

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = next((p for p in dummy_posts if p["id"] == post_id), None)
    if not post:
        abort(404)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('edit_post', post_id=post_id))
        post['title'] = title
        post['content'] = content
        flash('Post updated successfully!', 'success')
        return redirect(url_for('post', post_id=post_id))
    return render_template('add_edit.html', action='Edit', post=post)

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    global dummy_posts
    dummy_posts = [p for p in dummy_posts if p['id'] != post_id]
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 