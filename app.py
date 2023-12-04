from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)
ultima_qtd_passageiros = 0

# MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'brabozo',
}

@app.route('/api/log/<int:qtd_passageiros>', methods=['GET'])
def save_to_database(qtd_passageiros):
    try:
        print("Recebido: " + str(qtd_passageiros))
        
        global ultima_qtd_passageiros
        ultima_qtd_passageiros = qtd_passageiros

        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert the variable into the database
        cursor.execute("INSERT INTO logs (id_onibus, qtd_passageiros, dt) VALUES (1, {}, now())".format(qtd_passageiros))

        # Commit changes and close the connection
        connection.commit()
        cursor.close()

        return ""

    except Exception as e:
        return str(e)
    
@app.route('/', methods=['GET'])
def list_entries():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Fetch entries from the database
        cursor.execute("SELECT * FROM logs")
        entries = cursor.fetchall()

        # Close the connection
        cursor.close()

        global ultima_qtd_passageiros

        return render_template('list_entries.html', entries=entries, ultima=ultima_qtd_passageiros)

    except Exception as e:
        return str(e)

@app.route('/site', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug=False, port= '8080')
