from flask import Blueprint, request
from service.GeminiService import GeminiService

test_mass_generator_controller = Blueprint('test_mass_generator', __name__, template_folder='templates')

@test_mass_generator_controller.route('/gerar_massa_de_testes', methods=['POST'])
def generate_mass():
    quantity = request.form.get('quantity')
    validData = request.form.get('validData')
    item = request.form.get('item')

    print(f"{quantity}, {validData}, {item}")

    gemini_service = GeminiService()
    response = gemini_service.generate_mass_tests(quantity, validData, item)
    return response


