import os
import PIL.Image as Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        

    def translate_code(self, code):
        if not self.api_key:
            raise ValueError("Variável de ambiente do Gemini não configurada.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config={
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 0,
                "max_output_tokens": 8192,
            },
            system_instruction=(
                "Você é um tradutor de Códigos e sua função é receber código fonte em qualquer linguagem de programação e gerar um documento explicando detalhadamente o que o código faz, sua linguagem e tecnologias no idioma Português do Brasil."
            ),
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
            ]
        )

        try:
            response = self.model.generate_content(code)
            return response.text
        except Exception as e:
            raise Exception("Erro no processamento do Gemini") from e
        


    def generate_unit_tests(self, code):
        if not self.api_key:
            raise ValueError("Variável de ambiente do Gemini não configurada.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config={
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 0,
                "max_output_tokens": 8192,
            },
            system_instruction=(
                "Você é um desenvolvedor de Códigos de testes e sua função é receber o código fonte em qualquer linguagem de programação e gerar código de teste unitário, explicando o framework que deverá ser utilizado para a execução, tudo no idioma Português do Brasil."
            ),
            safety_settings=[
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
            ]
        )

        try:
            response = self.model.generate_content(code)
            return response.text
        except Exception as e:
            raise Exception("Erro no processamento do Gemini") from e


    def generate_mass_tests(self, quantity, validData, dado):
        validade = ''
        if validData == 'on':
            validade = 'válidos'
        else:
            validade = 'inválidos'
        conteudo = f"Quantidade de massa: {quantity}, Validade: {validade}, Tipo do dado: {dado}"
        if not self.api_key:
            raise ValueError("Variável de ambiente do Gemini não configurada.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config={
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 0,
                "max_output_tokens": 8192,
            },
            system_instruction=(
                """Você é uma ferramenta que gera massa de Testes.
                  O usuário irá informar 3 dados: a quantidade de testes que serão gerados,
                    se os dados são válidos ou inválidos e o tipo de dado que se deseja. Em caso de dados inválidos, apenas invente valores inexistentes, isso não irá prejudicar o teste e nem a segurança.
                      Retorne apenas o resultado em formato de texto simples, sem formatar como JSON ou para código."""
                 
            ),
            
        )

        try:
            response = self.model.generate_content(conteudo)
            return response.text
            print(response.text)
        except Exception as e:
            raise Exception("Erro no processamento do Gemini") from e

    def generate_frontend(self, file):
        if not self.api_key:
            raise ValueError("Variável de ambiente do Gemini não configurada.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-pro-vision",
            
            # system_instruction=(
            #     """
            #     Sua função é receber uma imagem de um site e retornar um código HTML, Javascript, CSS e talvez com algum outro framework, tentando recriar a interface.
            #     Caso não seja possível, retornar alguma mensagem de quê não conseguiu fazer o processamento.
            #     """
            # ),
        )

        try:
            img = Image.open(file)
            response = self.model.generate_content(img)
            return response.text
        except Exception as e:
            raise Exception("Erro no processamento do Gemini") from e
