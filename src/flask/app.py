from flask import Flask, render_template, request, redirect, url_for
from pypg import helper
import json


app = Flask(__name__)

@app.route('/')
def index():
  tables = helper.read_tables()
  return render_template("index.html", table=[0][0])

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    phone = request.form.get("phone")

    print(f"{name}이 {phone}로 가입")
    print(helper.insert("student", name, phone))

    return render_template("index.html")

@app.route('/select', methods=["GET"])
def select():
  data=[]
    #name = request.form.get('name_to_search') #input 값 갖고오기
  name="고태형"
  data = helper.selecting("student", name)
  print(f"{name} 검색결과 : {data}")

  result = json.dumps(data, ensure_ascii=False)
  print(f"{result}")
  return result



@app.route('/delete', methods=["POST"])
def delete():
    name = request.form["name_to_delete"]

    print(f"{name} 삭제")
    print(helper.delete("student", name))

    return redirect("/")

@app.route('/update', methods=["POST"])
def update():
    name = request.form["name_to_update"]
    phone = request.form["phone_to_update"]

    print(f"{name}, {phone} 수정")
    print(helper.update("student", name, phone))
    return redirect("/")


@app.route("/list-rest")
def students_list_rest():
  result = helper.students_list() #list type -> column 으로 접근
  result = json.dumps(result)
  return result


if __name__ == ("__main__"):
  # docker
  app.run(debug=True, host='0.0.0.0', port=5090)
  # other
  #app.run(debug=True)



