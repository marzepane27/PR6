class Config:

    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:ygenbXELPjFcAdfMKwzQwfXmPGDJIAqu@junction.proxy.rlwy.net:19910/RailwayDB'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  


    JWT_SECRET_KEY = 'your-secret-key'  
    JWT_ACCESS_TOKEN_EXPIRES = 30  

    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
