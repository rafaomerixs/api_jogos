from flask import Blueprint, request  
from controllers.jogos_controllers import get_jogos, create_jogos, update_jogo, get_jogos_by_id 

# Define um Blueprint para as rotas de "Carro"
jogos_routes = Blueprint('jogos_routes', __name__)  

# Rota para listar todos os carros (GET)
@jogos_routes.route('/jogos', methods=['GET'])
def jogos_get():
    return get_jogos()

# Rota para buscar um carro pelo ID (GET)
@jogos_routes.route('/Jogos/<int:carro_id>', methods=['GET'])
def jogos_get_by_id(jogos_id):
    return get_jogos_by_id(jogos_id)

# Rota para criar um novo carro (POST)
@jogos_routes.route('/Jogos', methods=['POST'])
def jogos_post():
    return create_jogos(request.json)

@jogos_routes.route('/Jogo/<int:jogo_id>', methods=['PUT'])
def jogos_put(jogo_id):
    # Obtém os dados atualizados do jogo enviados no corpo da requisição (formato JSON)
    jogo_data = request.json
    # Chama a função 'update_jogo' para atualizar as informações do jogo no banco de dados
    return update_jogo(jogo_id, jogo_data)
