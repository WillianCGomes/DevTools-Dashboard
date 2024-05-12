from flask import Blueprint, request
from service.GeminiService import GeminiService

translator_controller = Blueprint('translator', __name__, template_folder='templates')

@translator_controller.route('/traduz_codigo', methods=['POST'])
def translate_code():
    file = request.files['codeFile']
    if file:
        code = file.read().decode('utf-8')
        gemini_service = GeminiService()
        explanation = gemini_service.translate_code(code)
        return explanation
    return 'Erro leitura do arquivo.'

