from flask import Flask, request, jsonify
app = Flask(__name__)

# TODO: Complete this method
# Input: Uploaded image as request body parameter
# Output: List of people in the image
@app.route('/peep', methods=["GET"])
def peep():
    print('Peeping into people')
    return (jsonify(
        {
            'code': 200,
            'people': [
                {
                    'name': 'Name',
                    'email': 'Email',
                    'links': {
                        'facebook': '',
                        'twitter': '',
                        'linkedin': '',
                        'github': ''
                    }
                }
            ]
        }
    ))

# TODO: Complete this method
# Input: Person details as request body parameter
# Output: 200 code if validations pass, else error message
@app.route('/users/new', methods=["POST"])
def register_user():
    # Use the request.args
    print('Register a new user')
    return(jsonify({'code': 200, 'id': 1}))

# TODO: Complete this method
# Input: Person details as request body parameter
# Output: True if validations pass, else error message
@app.route('/users/<int:user_id>', methods=["POST"])
def update_user(user_id):
    # Fetch user from database for this user_id
    # Use the request.args
    print('Updates an existing user')
    return(jsonify({'code': 200}))

# TODO: Complete this method
# Input: Person details as request body parameter
# Output: True if validations pass, else error message
@app.route('/users/<int:user_id>', methods=["GET"])
def fetch_user(user_id):
    # Fetch user from database for this user_id
    print('Fetches an existing user')
    return (jsonify(
        {
            'code': 200,
            'person': {
                'name': 'Name',
                'email': 'Email',
                'links': {
                    'facebook': '',
                    'twitter': '',
                    'linkedin': '',
                    'github': ''
                }
            }
        }
    ))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
