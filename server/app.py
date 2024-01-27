from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
<<<<<<< HEAD
from datetime import datetime, timezone
from bson.objectid import ObjectId

=======
import speech_recognition as sr
import subprocess
from werkzeug.utils import secure_filename
>>>>>>> 6b74619 (Add audio saving ability)

app = Flask(__name__)
CORS(app)

CONNECTION_STRING = "mongodb+srv://uoft:oPqKe1qnlgxLVJQF@cluster0.fjluu9a.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)

<<<<<<< HEAD
dbname = client['contacts']
contacts = dbname["contacts"]
=======
db = client.flask_db
contacts = db.contacts
r = sr.Recognizer() # audio recognizer
>>>>>>> 6b74619 (Add audio saving ability)

# Test route
@app.route('/test', methods=['GET'])
def my_profile():
    return jsonify({"name": "Jessica"})

@app.route('/add_contact', methods=['POST'])
def create_contact():
    data = request.get_json()
    app.logger.info(data)

    contacts.insert_one(data)
    # check for invalid input

    response = {'message': 'Contact added successfully'}
    return jsonify(response), 201


# Index and filter contacts
@app.route('/', methods=['GET'])
def list_contacts():
    data = request.get_json()

    # add to database

    response = {'message': 'Contact added successfully'}
    return jsonify(response), 201


# Show contact by ID
@app.route('/contact', methods=['GET'])
def show_contact():
    contact_id = request.args.get('id')

    if not (contact_id and len(contact_id) > 0):
        return jsonify({'error': 'Invalid contact ID'}), 400

    # retrieve from database
    contact = ['Sophie', 'Xie', ['Blacklisted'], 'Company', 'Toronto', 'sophie@gmail.com',
               '1234567890', 'notes notes notes', '02-02-2020']

    if contact:
        keys = ['first_name', 'last_name', 'labels', 'company', 'location',
                'email', 'phone_number', 'notes', 'last_contacted']
        data = dict(zip(keys, contact))
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Contact not found'}), 404


@app.route('/update_contact', methods=['PUT'])
def update_contact():
    data = request.get_json()

    contact_id = data['id']

    if not (contact_id and len(contact_id) > 0):
        return jsonify({'error': 'Invalid contact ID'}), 400

    # edit database
    contact = ['Sophie', 'Xie', ['Potential Customer'], 'Company', 'Toronto', 'sophie@gmail.com',
               '1234567890', 'notes notes notes', '02-02-2020']

    if contact:
        keys = ['first_name', 'last_name', 'labels', 'company', 'location',
                'email', 'phone_number', 'notes', 'last_contacted']
        data = dict(zip(keys, contact))
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Contact not found'}), 404
    
# @app.route('/update_contact/add_meeting', methods=['PUT'])
# def add_meeting():
#     data = request.get_json()
#     app.logger.info(data)

#     # fix
#     try:
#         filter = {'_id': data['_id']}
#         newdata = { "$set": { "lastContacted" : datetime.datetime.now(tz=datetime.timezone.utc) } }
#         contacts.update_one(filter, newdata)
#         response = {'message': 'Last meeting time updated'}
#         return jsonify(response), 200
#     except Exception as e:
#         response = {'message': e}
#         return jsonify(response), 400 


@app.route('/delete', methods=['DELETE'])
def delete_contact():
    data = request.get_json()
    contact_id = data['_id']

    if not (contact_id and len(contact_id) > 0):
        return jsonify({'error': 'Invalid contact ID'}), 400

<<<<<<< HEAD
    try:
        result = contacts.delete_one({'_id': ObjectId(contact_id)})
        if result.deleted_count == 1:
            return jsonify({'message': 'Deleted contact'}), 200
        else:
            return jsonify({'message': 'Contact not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
=======
    # remove from database
    success = True

    if success:
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Contact not found'}), 404
    
@app.route('/listen', methods=["POST"])
def listen():
    print('here')
    try:
        audio_file = request.files['audio']
        # Save the audio file to a specific location
        audio_file.save('./audio.wav')
        return jsonify({'success': 'saved'})
    except Exception as e:
        return jsonify({'error': f'Failed to save audio: {str(e)}'}), 500
>>>>>>> 6b74619 (Add audio saving ability)
