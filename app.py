from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for blog posts
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    if 0 <= post_id < len(posts):
        return render_template('post.html', post=posts[post_id], post_id=post_id)
    return 'Post not found', 404

@app.route('/new', methods=['POST'])
def new_post():
    title = request.form['title']
    content = request.form['content']
    posts.append({'title': title, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 