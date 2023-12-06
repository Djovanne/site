from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)
ultima_qtd_passageiros = 0

# MySQL configuration
db_config = {
    'host': '143.198.186.226',
    #'user': 'root',
    'user': 'brabozodb',
    'password': 'a3cb636e07a424c1d8d2507a5a9ade1e38d78aa1eed40a3a',
    'database': 'brabozo',
}

def on_startup():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT QTD_PASSAGEIROS FROM LOGS WHERE ID = (SELECT MAX(ID) FROM LOGS)")

    qtd_passageiros = cursor.fetchall()[0][0]
    qtd_passageiros = float(qtd_passageiros)
    
    cursor.close()

    global ultima_qtd_passageiros
    ultima_qtd_passageiros = qtd_passageiros
    print('on_startup concluido. qtd_passageiros: {}'.format(ultima_qtd_passageiros))

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
        cursor.execute("INSERT INTO LOGS (id_onibus, qtd_passageiros, dt) VALUES (1, {}, now())".format(qtd_passageiros))

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
        cursor.execute("SELECT * FROM LOGS")
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

@app.route('/expectativas', methods=['GET'])
def expectativas():

    global ultima_qtd_passageiros
    area_sala = 30
    massa_onibus_kg = 16000
    massa_passageiro_kg = 65
    velocidade_media_onibus_kh = 35

    densidade_media = ultima_qtd_passageiros / area_sala
    velocidade_media = (velocidade_media_onibus_kh * massa_onibus_kg) / (massa_onibus_kg + (ultima_qtd_passageiros * massa_passageiro_kg))
    
    densidade_media = f"{densidade_media:.3f}"
    velocidade_media =  f"{velocidade_media:.3f}"

    return render_template('expectativas.html', 
                           densidade_media=densidade_media, velocidade_media=velocidade_media)


if __name__ == '__main__':
    on_startup()
    #app.run(host = '143.198.186.226', debug=False, port= '8080')
    app.run(host = 'localhost', debug=False, port= '8080')
