import sys    
import json
sys.path[0] = sys.path[0] + "\\..\\app"
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)

from dotenv import load_dotenv
import os

from db.db_manager import db_manager
if os.path.isfile(".env"): load_dotenv()

dbMan = db_manager()
methodQuery = "UPDATE users SET \"gameHistory\" = %s::jsonb || \"gameHistory\" WHERE uuid LIKE %s"
dbMan.cursor.execute(methodQuery, [json.dumps({"title": "ar", "opid": "er"}), "0104c848-f6ba-4668-b810-af1aa16dc616"])
dbMan.conn.commit()
dbMan.free()