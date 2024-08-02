from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app and to instantiate the flask function as app 
app = Flask(__name__)

# in-memory database for simplicty 
posts = [{"title": "Post 1", "content": "This is the content of post 1"}, {"title": "Post 2", "content": "This is the content of post 2"}]

# Route to the home page

@app.route('/')
def index():
    return render_template('index.html', posts=posts)



@app.route('/new', methods=['GET', 'POST'])
def new_post():
    # first check if the request method is POST
    if request.method == 'POST':
        # get the title and content from the form 
        title = request.form['title']
        content = request.form['content']
        print("this is my new title", title)
        print("this is my new content", content)
        # create a new post object and put it in our 
        # posts list - -- append the new object 
        posts.append({"title": title, "content": content})
        print("this is my updated posts database", posts)
        # once the object is created redirect to the index page and show us the new post that was created
        return redirect(url_for('index'))
    # if the request method is not POST, then render the new.html template
    return render_template('new_post.html')





if __name__ == '__main__':
    app.run(debug=True)