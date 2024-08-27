from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/swagger"  # URL para acessar o Swagger UI
API_URL = "/static/swagger.json"  # Caminho para o arquivo swagger.json

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={
        "app_name": "API de Alunos",
        "requestInterceptor": lambda request: request.url.replace("localhost:5000", "https://generationapi.onrender.com")
    }
)
