from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html', page_title='Home', content="Welcome to Our Hotel!")

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html', page_title='About', content="Learn about Our Hotel")

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact', content="Contact Us")

# Route for the services page
@app.route('/services')
def services():
    return render_template('services.html', page_title='Services', content="Our Services")

if __name__ == '__main__':
    app.run(debug=True)
