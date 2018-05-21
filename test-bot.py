#test-bot by Deps

#https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_HERE&scope=bot&permissions=66186303
#https://discordapp.com/developers/docs/intro

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
	print("test-bot online")
	print(bot.user.name)
	print(bot.user.id)

@bot.command(pass_context=True)
@commands.has_role('nb')
async def ping(ctx):
	await bot.say("OIII FAM DON'T @ ME")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	embed = discord.Embed(title='{}\'s info'.format(user.name), description='Here\'s what I could find', color=0x00ff00)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=True)
	embed.add_field(name="Highest role", value=user.top_role)
	embed.add_field(name="Date joined", value=user.joined_at)
	embed.set_thumbnail(url=user.avatar_url)
	await bot.say(embed=embed)
	
	
@bot.command(pass_context=True)
@commands.has_role('new role')
async def kick(ctx, user: discord.Member):
	await bot.say("So uncivilised")
	await bot.kick(user)
	
	
@bot.command(pass_context=True)
async def embed(ctx):
	embed = discord.Embed(title='test', description='my name jeff', color=0x00ff00)
	embed.set_footer(text='this is the footer')
	embed.set_author(name='NoisyB')
	embed.add_field(name='This is a field', value='no its not', inline=True)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def helpp(ctz, *args, **kwargs):
	print(args)
	print(kwargs)
	print(len(args))
	if 'name' in args:
		await bot.say('y u saying name for')
	else:
		await bot.say('no name')
		
	await bot.say('the first thing u said was: {}'.format(args[0]))
	
@bot.command(pass_context=True)
async def test(ctx, user: discord.Member = None, *args):
	if user is not None:
		await bot.say(user.name)
	else:
		await bot.say('ello {0}. id = {1}'.format(ctx.message.author, ctx.message.author.id))


bot.run("NDQ2NjYxMTAyNDcwODIzOTM2.Dd8RHw.CIJ3VRO9Re6w4nF82qohes6yw0g")