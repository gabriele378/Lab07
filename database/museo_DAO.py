from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO

    cnx = ConnessioneDB.get_connection()
    musei = []
    if cnx is not None:
        cursor = cnx.cursor()
        query = """SELECT DISTINCT nome from MUSEO"""
        cursor.execute(query)
        for row in cursor:
            musei.append(row)

        cursor.close()
        cnx.close()

    else:
        print("Impossibile connettersi")

