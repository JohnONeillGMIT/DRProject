from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='',static_folder='.')

employees=[
    {"id":100101, "FirstName":"Adam", "Surname":"Clayton", "Extension":1001},
    {"id":100102, "FirstName":"Larry", "Surname":"Mullen", "Extension":1002},
    {"id":100103, "FirstName":"Paul", "Surname":"Hewson","Extension":1003},
]
nextID =100104



#curl "http://127.0.0.1:5000/employees"
@app.route('/employees')
def getAll():
    return jsonify(employees)

# curl "http://127.0.0.1:5000/employees/100101"
@app.route('/employees/<int:id>')
def findByID(id):
    findEmps = list(filter(lambda t: t['id'] == id, employees))
    if len(findEmps) == 0:
        return jsonify ({}), 204

    return jsonify(findEmps[0])   


#curl-7.67.0-win64-mingw\bin>curl -i -H "Content-Type:application/json" -X POST -d "{\"FirstName\":\"Dave\",\"Surname\":\"Evans\",\"Extension\":\"100104\"}" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
    #other checking
    employee = {
        "id":nextID,
        "FirstName": request.json['FirstName'],
        "Surname": request.json['Surname'],
        "Extension": request.json['Extension'],
    }
    nextID +=1
    employees.append(employee)
    return jsonify(employee)


#curl -i -H "Content-Type:application/json" -X PUT -d "{\"FirstName\":\"Dave\",\"Surname\":\"Evans\",\"Extension\":\"1004\"}" http://127.0.0.1:5000/employees/100101
@app.route('/employees/<int:id>', methods=['PUT'])
def update(id):
    findEmps = list(filter(lambda t: t['id'] == id, employees))
    if len(findEmps) == 0:
       abort(404)
    findEmps = findEmps[0]
    if not request.json:
        abort(400)
    reqJson = request.json


    if 'FirstName' in reqJson:
        findEmps['FirstName']= reqJson ['FirstName']
    if 'Surname' in reqJson:
        findEmps['Surname']= reqJson ['Surname']
    if 'Extension' in reqJson and type(reqJson['Extension']) is not int:
        abort(400)
        findEmps['Extension']= reqJson ['Extension']
    
    return jsonify(findEmps)  




@app.route('/employees/<int:id>', methods=['DELETE'])
def delete(id):
    findEmps = list(filter(lambda t: t['id'] == id, employees))
    if len(findEmps) == 0:
       abort(404)
    employees.remove(findEmps[0])
    return jsonify({"done":True})



if __name__== '__main__':
    app.run(debug= True)