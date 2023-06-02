from src import create_app

# import src.common.exception_handler
from config import Config

app = create_app()

if __name__ == "__main__":
    app.run(port=Config.PORT)
