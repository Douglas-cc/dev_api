from flask_restful import Resource

lista_habilidades = ['C','Python', 'Java', 'R', 'Javascript']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades