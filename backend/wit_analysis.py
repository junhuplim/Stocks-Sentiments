from wit import Wit
from dotenv import load_dotenv
import os

load_dotenv()

WIT_ACCESS_TOKEN = os.getenv("WIT_ACCESS_TOKEN")
client = Wit(WIT_ACCESS_TOKEN)

resp = client.message('dd')
print(resp['intents'][0]['name'])