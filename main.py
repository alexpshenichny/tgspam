from pyrogram import Client

api_id = int(input("API_ID:\n"))

api_hash = input("API_HASH:\n")

n = input("User:\n")

t = int(input("Threads:\n"))

with Client("my_account", api_id, api_hash) as app:
 i = 1
 while i <= t:
  app.send_message(n, "SPAM")
  i = i + 1
