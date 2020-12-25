import discord
import os
import solver
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	print('-------------------------------------\n')
	await client.change_presence(activity=discord.Activity(name="CTFs and solving ciphers.", type="5"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	msg = message.content

	if solver.isCommand(msg):
		try:
			await message.channel.send(solver.evaluate(msg))
		except:
			await message.channel.send('Can\'t complete command.')


keep_alive()
client.run(os.getenv('TOKEN'))