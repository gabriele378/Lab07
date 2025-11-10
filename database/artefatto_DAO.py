from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    cnx = ConnessioneDB.get_connection()
    artefatti = []
    if cnx is not None:
        cursor = cnx.cursor()
        query = """SELECT * from ARTEFATTO
                    WHERE epoca = COALESCE(%s, epoca)
                    and museo = COALESCE(%s, museo)`"""
        cursor.execute(query)
        for row in cursor:
            artefatti.append(row)

        cursor.close()
        cnx.close()

    else:
        print("Impossibile connettersi")

    cnx = ConnessioneDB.get_connection()
    epoche = []
    if cnx is not None:
        cursor = cnx.cursor()
        query2 = """SELECT DISTICT epoca from ARTEFATTO"""
        cursor.execute(query2)
        for row in cursor:
            artefatti.append(row)

        cursor.close()
        cnx.close()

    else:
        print("Impossibile connettersi")



