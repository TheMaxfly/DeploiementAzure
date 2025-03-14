import pyodbc

try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=flavignysqlserver.database.windows.net;DATABASE=Django_prediction;UID=adminusba;PWD=usba2025RBX;Encrypt=yes;TrustServerCertificate=no')
    print('Connexion réussie à la base de données')
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print("Version de SQL Server:", row[0])
    conn.close()
except Exception as e:
    print(f'Erreur de connexion: {str(e)}')