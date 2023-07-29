import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import Increment
from github import Github
import os
import subprocess
versiyon=1
#Firebase Initialization
#cred = credentials.Certificate("path/to/serviceAccountKey.json")
#firebase_admin.initialize_app(cred)
#db = firestore.client()
#doc_ref = db.collection(u'bot').document(u'version')

# Github Initialization
g = Github("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")
repo = g.get_repo("https://github.com/Acelya-Launcher/bot.git")
# Get current version from Firestore
#current_version = doc_ref.get().to_dict()['current_version']

# Check if current version is up to date
if True:
    # Download and run new version
    assets = repo.get_latest_release().get_assets()
    for asset in assets:
        if asset.name == "bot.py":
            url = asset.browser_download_url
            subprocess.Popen(["curl", "-o", "bot_new.py", url])
            break
    os.replace("bot_new.py", "bot.py")

# Your bot's main code here
