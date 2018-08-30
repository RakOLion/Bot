import discord
import random
from urllib3 import PoolManager
from urllib3.exceptions import HTTPError
client = discord.Client()
P = PoolManager(100)
@client.event
async def on_message(message):
	global P
	if message.author ==client.user:
		return
	if message.content.startswith('Hello'):
		msg = 'Hi'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('no u'):
		msg = 'no u'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('Hi'):
		msg = 'Mhm'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('Hey'):
		msg = 'What do you want'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('kys'):
		msg = 'no u'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('@RakO#9124'):
		msg = 'What'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('online'):
		url=message.content[7:]
		try:
			r=P.request('GET', url)
			if r.status==200:
				await client.send_message(message.channel, "Online")
			else:
				await client.send_message(message.channel, "Status Code %d"%r.status)
		except(ConnectionError,HTTPError) as e:
			await client.send_message(message.channel, e)
	if message.content.startswith('command'):
			if message.author.id =='309143499008245760':
				msg = 'Yes, Overseer'.format(message)
				await client.send_message(message.channel, msg)
			else:
				msg = 'I dont serve you..'.format(message)
				await client.send_message(message.channel, msg)	
	if message.content.startswith('ask'):
			r=random.choice(['Sure','I dont see why not', 'Whatever you wish', 'It's your decision'])

	
	
	

client.run('NDgxOTg0MDcwNTk1NjQxMzY0.Dl-SPg.kpwgVtc_eblAc1ST6xp7yyLLkVM')
