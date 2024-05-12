from flask import Flask, render_template
# from service.GeminiService import GeminiService
from controller.TranslatorController import translator_controller
from controller.UnitTestsGeneratorController import unit_tests_generator_controller
from controller.TestMassGeneratorController import test_mass_generator_controller
# from controller.FrontEndGeneratorController import frontend_generator_controller

app = Flask(__name__, static_folder='/templates/static')

app.register_blueprint(translator_controller)
app.register_blueprint(unit_tests_generator_controller)
app.register_blueprint(test_mass_generator_controller)
# app.register_blueprint(frontend_generator_controller)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translator')
def translator():
    return render_template('translator.html')

@app.route('/frontend-generator')
def frontend_generator():
    return render_template('frontend_generator.html')
    # Placeholder for frontend generator route
    pass

@app.route('/testing-assistant')
def testing_assistant():
    return render_template('testing_assistant.html')

@app.route('/unit-tests-generator')
def unit_tests_generator():
    return render_template('unit_tests_generator.html')

@app.route('/test_mass_generator')
def test_mass_generator():
    return render_template('test_mass_generator.html')

if __name__ == '__main__':
    app.run(debug=True)
