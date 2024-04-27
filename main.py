import os

os.system("pip install scratchattach")

import scratchattach as scratch3
import time

sessionID = ".eJxVj8FuwyAQRP_F59Y1YAzOrW2OVQ6V2qonC8NiE9uQGqwoqfrvXaRcclu92RnN_BZbhNWrBYpdETfvL_28QZwuxUPRqS2NXdY7Z1BmRFLOWoZSgph0CJPLtnNYJzD3hl7pCXx2ZQY-Oa2SC768CbF8h9N8gy-3Z8wNeKDJKGKI1FZVrKkNr6UUlFjSGt1aA9ruhqF729vrGinbPiz_Sq-DPpw-f_Zqwpg5DM4_uhMmNVXZiJI0vKxlrjgrP2xqyL2PCoE5Ighdcgtcg8_4eYEViz0d4Nx947T7YaOKIz5x0jOtueoroEJSI7BU00pGK8EtBdmLmtSC2uLvHy3kdB4:1rsu8v:8H94ipbRgAMlzRGWzUfneOQCfwA"

session = scratch3.Session(sessionID, username="sunnybluesky")

connection = session.connect_cloud(project_id=996203838)

print("クラウド変数に接続")

A = 0

while True:
  A = (A + 1) % 2
  connection.set_var("last_access", A)
  print(f"クラウド変数をセット {A}")
  time.sleep(0.1)
