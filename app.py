from app import create_app
from settings import port


if __name__ == '__main__':
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=port
    )
