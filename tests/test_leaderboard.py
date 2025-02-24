import sys    

sys.path[0] = sys.path[0] + "\\..\\app"
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

from dotenv import load_dotenv
import os

from db.db_manager import db_manager
if os.path.isfile(".env"): load_dotenv()


dbMan = db_manager()
how = input("ORDER BY: ")
methodQuery = f"SELECT * FROM users ORDER BY {how} DESC LIMIT 20"
dbMan.cursor.execute(methodQuery)
result = dbMan.cursor.fetchall()

for x in result:
    print(f"{x["username"]}, elo: {x["elo"]} W/D/L: {x["wins"]}/{x["draws"]}/{x["losses"]}")

dbMan.free()