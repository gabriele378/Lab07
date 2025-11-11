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
    def get_artefatti_filtrati(self, museo= None, epoca= None):
        cnx = ConnessioneDB.get_connection()
        artefatti = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * from ARTEFATTO
                        WHERE (%s IS NULL OR museo = %s)
                        AND (%s IS NULL OR epoca = %s)
                        `"""
            cursor.execute(query,(museo,museo, epoca, epoca))
            for row in cursor:
                artefatti.append(Artefatto(**row))

            cursor.close()
            cnx.close()

        return artefatti

    def get_epoche(self):
        cnx = ConnessioneDB.get_connection()
        epoche = []
        if cnx is not None:
            cursor = cnx.cursor()
            query2 = """SELECT DISTICT epoca from ARTEFATTO"""
            cursor.execute(query2)
            for row in cursor:
                epoche.append(row[3])

            cursor.close()
            cnx.close()

        return epoche



