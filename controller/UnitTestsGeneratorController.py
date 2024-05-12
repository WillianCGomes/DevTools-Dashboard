from flask import Blueprint, request
from service.GeminiService import GeminiService

unit_tests_generator_controller = Blueprint('unit_tests_generator', __name__, template_folder='templates')

@unit_tests_generator_controller.route('/gerar_testes_unitarios', methods=['POST'])
def generate_unit_tests():
    file = request.files['codeFile']
    if file:
        code = file.read().decode('utf-8')
        gemini_service = GeminiService()
        tests = gemini_service.generate_unit_tests(code)
        return tests
    return 'Erro leitura do arquivo.'

