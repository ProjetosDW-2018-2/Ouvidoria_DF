DEBUG=True
USER_RELOADER=True
SECRET_KEY = 'db_ouvidoria'
SQLALCHEMY_TRACK_MODIFICATIONS = True

#banco dados configurações
#se conecta com a base operacional
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://alunoufrpe2:ufrpedwbi@www.db4free.net/ouvidoria_df?charset=utf8mb4'

#se conecta com a base do DW
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://alunoufrpe3:ufrpedwbi@www.db4free.net/ouv_dw?charset=utf8mb4'
