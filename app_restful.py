import json
from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

devs = [
    {
        'id': 0,   
        'nome': 'Douglas',
        'habilidades':[
            'Python', 
            'Flask',
            'Hadoop',
            'TensorFlow'
        ]
    },
    
    {
        'id': 1,
        'nome': 'Carlos',
        'habilidades':[
            'Javascript',
            'NodeJs',
            'React',
            'React Native'
        ]
    } 
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:    
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Entre em contato com o suporte tecnico'    
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'Status':'sucesso', 'mensagem': 'Registro Excluido!'}

class Listar_Desenvolvesores(Resource):
    def get(self):
        return devs
    
    def post(self):
        dados = json.loads(request.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)
        return devs[pos]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Listar_Desenvolvesores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == "__main__":
    app.run(debug=True)