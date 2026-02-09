from flask import Flask, jsonify, request, Response
from flask_cors import CORS #type: ignore
from studentsBackEnd import get_current_data,add_data, students_id  #type: ignore 

app = Flask(__name__) 
URL = "/api/data"
CORS(app)

@app.get(URL)
def sendData()->Response:
    return jsonify(get_current_data())

@app.get("/api/ids")
def getIds():
     return jsonify(students_id())

@app.post(URL)
def getData()->tuple[Response,int] : 
    response = request.get_json(force=True, silent = True,cache=True)
    

    if response is None: 
            return jsonify( {"status":"error", 
                             "message": "no JSON received"}), 400


    result:dict= add_data(response)
    if (not result["ok"]): 
        return jsonify(result), 550

    return jsonify(result), 200



"""
capitulo tres. separador, practica directa . 

escanear todos los docuemntos firmados por mi jefe...


presentarse el dia miercoles y jueves...

miercoles traer todas las hojas firmadas en un folder rosado carta con caratula,escrito informe de practica.
jundto con  la portada imprimiida. y la introducion ...


dia miercoles con el color rosado a las 8:00 hrs, camisa celeste ...

el dia jueves a las 7:00 hrs, camisa rosada...


uso de vocabulario tecnico ...                                                                                                                             



"""




if __name__ == "__main__":
    app.run(debug=True)