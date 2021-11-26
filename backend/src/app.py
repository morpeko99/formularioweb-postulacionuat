from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail, Message
from datetime import datetime
import json

app = Flask(__name__)
#Se cargan los datos del archivo configdb

data = open('./configdb.json')
configdb = json.load(data)

nameUser = configdb["nameMySQLUser"]
passwordUser = configdb["passwordMySQLUser"]
nameDb = configdb["nameMySQLDb"]

# configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+nameUser+':'+passwordUser+'@localhost/'+nameDb

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configuración email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'clinicaficticia123@gmail.com'
app.config['MAIL_PASSWORD'] = 'prueba123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), nullable=False)
    apellidoPaterno = db.Column(db.String(70), nullable=False)
    apellidoMaterno = db.Column(db.String(70), nullable=False)
    rut = db.Column(db.String(70), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    medico = db.Column(db.String(70), nullable=False)
    fechaHora = db.Column(db.DateTime(), nullable=False)
    correo = db.Column(db.String(70), unique=True, nullable=False)

    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, rut, edad, medico, fechaHora, correo):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.rut = rut
        self.edad = edad
        self.medico = medico
        self.fechaHora = fechaHora
        self.correo = correo

db.create_all()  # se leen todas las clases y se crean las tablas


class ClientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellidoPaterno', 'apellidoMaterno',
                  'rut', 'edad', 'medico', 'fechaHora', 'correo')


client_schema = ClientSchema()  # para un cliente
clients_schema = ClientSchema(many=True)  # para multiples clientes


# routes
@app.route('/clients', methods=['POST'])
def create_client():
    """se agrega un cliente a la base de datos"""
    try:
        nombre = request.json['nombre'].lower()
        apellidoPaterno = request.json['apellidoPaterno'].lower()
        apellidoMaterno = request.json['apellidoMaterno'].lower()
        rut = request.json['rut']
        edad = int(request.json['edad'])
        fechaHora = datetime.strptime(
            (request.json['fecha']+' '+request.json['hora']), '%Y-%m-%d %H:%M')
        medico = request.json['medico'].lower()
        correo = request.json['correo'].lower()

        send_email(correo, nombre, apellidoPaterno, apellidoMaterno, request.json['fecha'], request.json['hora'], medico )

        new_client = Client(nombre, apellidoPaterno,
                            apellidoMaterno, rut, edad, medico, fechaHora, correo)
        db.session.add(new_client)
        db.session.commit()

        return client_schema.jsonify(new_client)
    except:
        abort(404, description="No se pudo crear la consulta.")


@app.route('/clients', methods=['GET'])
def get_clients():
    """se solicitan todos los clientes de la base de datos"""

    all_clients = Client.query.all()
    result = clients_schema.dump(all_clients)
    return jsonify(result)


@app.route('/clients/<id>', methods=['GET'])
def get_client(id):
    """se solicita un cliente"""
    client = Client.query.get(id)
    return client_schema.jsonify(client)


@app.route('/clients/<id>', methods=['DELETE'])
def delete_client(id):
    """Borra un cliente"""

    client = Client.query.get(id)
    db.session.delete(client)
    db.session.commit()

    return client_schema.jsonify(client)


def send_email(clientMail, nombre, apellidoPaterno, apellidoMaterno, fecha, hora, medico ):
    try:
        msg = Message('Unidad de Asistencia Técnica - Reserva de consulta', sender='clinicaficticia123@gmail.com',
                    recipients=[clientMail])
        fechaList = fecha.split("-")
        body = "Estimado "+nombre+" "+apellidoPaterno+" "+apellidoMaterno+"\n\n"+"Se ha confirmado su agenda para el día "+fechaList[2]+" del "+fechaList[1]+" del año "+fechaList[0]+", a las "+hora+", con el médico "+medico+".\n\n Atte.\n La Unidad de Asistencia Técnica"
        msg.body = body
        mail.send(msg)
        return True
    except:
        return False



if __name__ == "__main__":
    app.run(debug=True)
