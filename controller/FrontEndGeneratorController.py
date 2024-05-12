from flask import Blueprint, request
from service.GeminiService import GeminiService

frontend_generator_controller = Blueprint('frontend_generator', __name__, template_folder='templates')

@frontend_generator_controller.route('/gerar_frontend', methods=['POST'])
def gerar_frontend():
    file = request.files['imageFile']
    if file:
        gemini_service = GeminiService()
        codigo_frontend = gemini_service.generate_frontend(file)
        return codigo_frontend
    return 'Erro leitura do arquivo.'

