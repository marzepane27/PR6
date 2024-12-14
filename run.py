from app import create_app  
from app.extensions import get_db_connection  

app = create_app()


with app.app_context():
    pass

if __name__ == '__main__':
    app.run(debug=True)
