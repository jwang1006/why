import requests

amazonURL = requests.get("https://z9y1z07tr8.execute-api.us-east-2.amazonaws.com")
amazonURL.raise_for_status()



