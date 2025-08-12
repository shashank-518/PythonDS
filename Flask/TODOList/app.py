from flask import Flask,jsonify,request

app = Flask(__name__)

items = [
    {"id":1 , "name":"item1" , "descrption": "This is Item1"},
    {"id":2 , "name":"item2" , "descrption": "This is Item2"},
    ]

@app.route("/")
def main():
    return "Hello World"

@app.route("/items" , methods=["GET"])
def items():
    return jsonify(items)

@app.route("/items/<int:id>" , methods=["GET"])
def get_items(id):
    item = next((item for item in items if item["id"] == id),None)
    if item is None:
        return jsonify({"error": "Item is not found"})
    return jsonify(item)

@app.route("/items" , methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Item not found"})
    new_item ={
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json["name"],
        "description" : request.json.get("description","")
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:id>",methods=["PUT"])
def update_item(id):
    item = next((item for item in items if item["id"] == id),None)
    if item is None:
        return jsonify({"error": "Item is not found"})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

@app.route("/items/<int:id>",methods=["DELETE"])
def delete_item(id):
    global items
    items = [item for item in items if item["id"] != id]
    return jsonify({"result":"Deleted successfully"})




if __name__ == "__main__":
    app.run(debug=True)