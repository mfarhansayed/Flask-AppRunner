from flask import request, jsonify
from app import app, db
from app.models import Person

@app.route('/api/person', methods=['POST'])
def add_person():
    data = request.get_json()
    new_person = Person(name=data['name'], email=data['email'], role=data['role'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
