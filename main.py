import os
from flask import Flask, request, render_template, jsonify

# Support for gomix's 'front-end' and 'back-end' UI. template_folder='templates' ,
app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='public'  # Name of directory for static files
)

# Set the app secret key from the secret environment variables.
# app.secret = os.environ.get('SECRET')

# Dream database. Store dreams in memory for now.
KEYWORDS = ['Python. Python, everywhere.']
WEBSITES = ['Python. Python, everywhere.']

# @app.after_request
# def apply_kr_hello(response):
#     """Adds some headers to all responses."""

#     # Made by Kenneth Reitz.
#     if 'MADE_BY' in os.environ:
#         response.headers["X-Was-Here"] = os.environ.get('MADE_BY')

#     # Powered by Flask.
#     response.headers["X-Powered-By"] = os.environ.get('POWERED_BY')
#     return response


@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')


@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    """Simple API endpoint for dreams. 
    In memory, ephemeral, like real dreams.
    """

    # Add a dream to the in-memory database, if given.
    if 'keyword' in request.args:
        KEYWORDS.append(request.args['keyword'])

    # Return the list of remembered dreams.
    return jsonify(KEYWORDS)


# @app.route('/websites', methods=['GET', 'POST'])
# def websites():
#     """Simple API endpoint for dreams.
#     In memory, ephemeral, like real dreams.
#     """

#     # Add a website to the in-memory database, if given.
#     if 'website' in request.args:
#         WEBSITES.append(request.args['website'])

#     # Return the list of remembered websites.
#     return jsonify(WEBSITES)

if __name__ == '__main__':
    # app.run()
    app.debug = True
    app.run('0.0.0.0', 8080)
