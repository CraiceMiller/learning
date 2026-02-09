from flask import Flask, jsonify,request,Response
from flask_cors import CORS #type: ignore
from mypython.decorators import time #type: ignore
from mypython.files import FileManager #type: ignore
import asyncio

#1. THIS ONLY CREATE THE MAIN APP ALONG WITH THE NEEDED CORS
app = Flask(__name__)
CORS(app)
file = FileManager()
path= r"C:\Users\Usuario Pc\Desktop\programming\data\User Accounts.json"

#THE INFO I WANT TO SEND 
data = dict(
    serie="A",
    id=1,
    name="hersy", 
    age=18,
    no_friends=4, 
    is_Student=True, 
    height=59.25,
    more_Info={
        "country":"Altisora", 
        "languages":["Spanish","English"], 
        "has_Job":False
    }
)


#A LITTLE MORE COMPLEX INFO A WANT TO SEND 
async def main():
    global file 
    global path
    user = await file.read_json(path,False) #this return a dict
    return user


#I GUESS THESE ARE THE LINK (PATH) I CREATE TO GET THE INFO
#//GETTERS
@app.route( "/")
def index(): 
    return "Hello world"

@app.route( "/app/data")
def get_json_data(): 
    return jsonify(data)

@app.route("/app/users")
def get_user():
    users = asyncio.run(main() )
    return jsonify(users)


#SETTERS
@app.route("/api/save_user",methods=['POST'])
def save_user_data()->tuple[Response,int]: 
    try: 
        print("Reciving the data")
        incoming_data:dict = request.get_json(cache=True)

        if incoming_data is None: 
            return jsonify( {"status":"error", 
                             "message": "no JSON received"}), 400
        
        username = incoming_data.get('username' )
        balance = incoming_data.get('balance')

        print(f"The new data was successufly get...")

        global file 
        global path 
        users = asyncio.run(main())
        nw_info = {
            "username":username, 
            "balance":balance
        }

        file.write_json(path,nw_info)


        return jsonify({
            "status":"success",
            "message": f"user {username} recived and processed"

        }),200
    except Exception as e: 
        print( e)
        return jsonify({
            "status": "error",
            "message": f"An error has ocurred {e}"
        }),500

#RUN THE APP TO WORK WITH THIS ENTIRE CODE...
#get_json_data(information)
app.run(debug=True)

