from flask_swagger_ui import get_swaggerui_blueprint
import os

SWAGGER_URL = "/swagger"  # URL para acessar o Swagger UI
API_URL = "/static/swagger.json"  # Caminho para o arquivo swagger.json

# Verifica se a aplicação está rodando no ambiente de produção no Render
if os.getenv("RENDER"):
    API_URL = "https://generationapi.onrender.com/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL, 
    config={
        "app_name": "API de Alunos",
        "validatorUrl": None  # Evita mensagens de erro relacionadas ao validador
    }
)
