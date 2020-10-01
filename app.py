import json
from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/devs/<int:id>/', methods=['GET','PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:    
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Entre em contato com o suporte tecnico'    
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)    

    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'Status':'sucesso', 'mensagem': 'Registro Excluido!'})

@app.route('/devs/', methods=['POST','GET'])
def listar_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)
        return jsonify(devs[pos])

    elif request.method == 'GET':
        return jsonify(devs)

if __name__ == "__main__":
    app.run(debug=True)