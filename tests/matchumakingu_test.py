import sys    

sys.path[0] = sys.path[0] + "\\..\\app"
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

from dotenv import load_dotenv
import os

from db.db_manager import db_manager
if os.path.isfile(".env"): load_dotenv()


dbMan = db_manager()


def matchumakingu(elo):
    methodQuery = '''
    SELECT piskvorky.uuid, piskvorky.x, users.elo, piskvorky.gamemode FROM piskvorky
    JOIN users ON piskvorky.x = users.uuid
    WHERE piskvorky.o like '' AND elo <= %s + 100 AND gamemode not like 'private' ORDER BY elo DESC;
    '''
    dbMan.cursor.execute(methodQuery, [elo])
    result = dbMan.cursor.fetchall()
    if len(result) == 0:
        print("Kratos new game ig idk")
    else:
        print("Join")

    print(result)
    dbMan.free()

matchumakingu(400)