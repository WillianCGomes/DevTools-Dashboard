# Ferramentas de Apoio ao Time DEV - DevTools Dashboard 🛠️

Bem-vindo ao DevTools Dashboard, um painel interativo de ferramentas de desenvolvimento construído com Flask e integrado com a API do Gemini para automatizar e facilitar tarefas de desenvolvimento de software.

## Demonstração 🎥

Assista a uma demonstração do DevTools Dashboard em ação:
[Assistir ao Vídeo](https://youtu.be/ceb4RRllTvk)

## Funcionalidades 🌟

### Tradutor de Código 💬

Transforme o código fonte em explicações detalhadas e compreensíveis, facilitando a compreensão de códigos complexos.

- **Como funciona:** Envie arquivos de código através da interface e receba de volta explicações detalhadas no formato Markdown.
- **Tecnologia utilizada:** Utiliza o modelo `gemini-1.5-pro-latest` para análise e explicação de códigos.

### Assistente de Testes 🧪

Facilita a criação de testes de software com funcionalidades de geração de massa de testes e criação de testes unitários.

- **Gerador de Massa de Testes:**
  - **Funcionalidade:** Gere dados de teste em massa, válidos ou inválidos, para diferentes tipos de campos (Banco, CPF, Email, etc.).
  - **Tecnologia utilizada:** Baseia-se no modelo `gemini-1.5-pro-latest` para gerar dados sob demanda.

- **Gerador de Testes Unitários:**
  - **Funcionalidade:** Receba código fonte e obtenha scripts de teste unitário automáticos.
  - **Tecnologia utilizada:** O mesmo modelo Gemini é utilizado para gerar testes precisos e explicar o uso dos frameworks de testes adequados.

## Configuração do Projeto ⚙️

1. Clone o repositório:
`git clone https://github.com/WillianCGomes/DevTools-Dashboard`

2. Instale as dependências:
- Certifique-se de ter o Python instalado em uma versão superior à 3.10 com pip;
- Abra o terminal na pasta do projeto e instale as dependências:
`pip install -r requirements.txt `
Se preferir, você também pode fazer isso em um ambiente virtual.

3. Renomeie o arquivo .env_exemplo para `.env`

4. Configure a chave de API do Gemini no arquivo `.env`:


## Como Usar 🚀

Execute o servidor Flask localmente:
 `py.exe .\app.py` ou `python.exe .\app.py`
Acesse o painel através do navegador em `localhost:5000` e explore as ferramentas disponíveis no dashboard.

Criado por Willian Carlos Gomes. 
Muito Obrigado!