from flask import Flask, json

employees = [{"id": 1, "name": "Name 1"}, {"id": 2, "name": "Name 2"}]

api = Flask(__name__)

@api.route('/employees', methods=['GET'])
def get_employees():
  return json.dumps(employees)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=5000, debug=True)
