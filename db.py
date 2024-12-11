import psycopg2

connection: psycopg2.extensions.connection = None

def connect():
    global connection
    connection = psycopg2.connect(**{
            "dbname" : "kr2_v1",
            "user": "postgres",
            "password": "",
            "host": "localhost",
            "port": 5432
        })
    
def close():
    global connection
    connection.close()

def getRentals():
    global connection
    cur = connection.cursor()
    cur.execute("""
                SELECT 
                    client.lastname || ' ' || client.firstname || ' ' || client.patronymic as client_name,
                    car_model.name as car_name,
                    rental.start_date,
                    rental.days_quantity
                FROM rental
                JOIN car
                    ON rental.car_id = car.id
                JOIN car_model
                    ON car.model_id = car_model.id
                JOIN client
                    ON rental.client_id = client.id;
                """,)
    data = cur.fetchall()
    cur.close()
    return data
    