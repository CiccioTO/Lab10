from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    def __init__(self):
        pass

    @staticmethod
    def read_hubs():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select * 
                   from hub h"""
        cursor.execute(query)
        for row in cursor:
            result.append(Hub(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_spedizioni():  # Riceve la idMap degli Object
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT s1.id_hub_origine, s1.id_hub_destinazione, sum(s1.valore_merce ) as guadagno, COUNT(*) AS conteggio
                    FROM spedizione s1
                    GROUP BY s1.id_hub_origine, s1.id_hub_destinazione;
                                                                        """
        cursor.execute(query)

        for row in cursor:

            result.append(Spedizione(row["id_hub_origine"],row["id_hub_destinazione"],row['guadagno'],row['conteggio']))  # costruisce una Connessione

        cursor.close()
        conn.close()
        return result  # lista di oggetti di tipo Connessione
