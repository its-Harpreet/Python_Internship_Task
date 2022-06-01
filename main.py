from click import command
import discord
import os

client=discord.Client()

TOKEN="OTgwNzczOTIyODYzNzE0MzA0.GISjVX.E5z4Qov74u5QRCAFFo70AHYb3WUo_FQ4QkMbFM"
greeting_words=["Hello", "Hi","Hey","Hola","hello","hi",'hey','hola',"HELLO","HI","HEY","HOLA"]
words=["Enquiry","Register","Registration","Installment","enquiry","register","registration","installment"]
greet="Hello!! Welcome to DigiPodium\nHow can we help you?"
help_words=["Help","help","HELP"]
commands=['$help','$hello','$installment','$register','$enquiry']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
       .format(client))
  # await bot.add_cog(Greetings(bot))

@client.event
async def on_message(message):
  if message.author==client.user:
    return 
  
  msg=message.content
    
  if msg.startswith('$help') or any(word in  msg for word in help_words) :
    await message.channel.send("Here is the list of some useful commands that might help you\n$register : Gives you the REGISTRATION form link\n$installment : Gives you the FEE INSTALLMENT form link\n$enquiry : Gives you the ENQUIRY form link ")
    
  elif msg.startswith('$hello') or any(word in  msg for word in greeting_words):
    await message.channel.send(greet)

  elif  msg.startswith('$installment'):
      await message.channel.send('Installment Form Link: https://forms.gle/BXu8AnjTfFJKnzrs5')

  elif msg.startswith('$register'):
          await message.channel.send('Registration Form Link: https://forms.gle/CFb3ByMRJW6ii9u97')
    
  elif msg.startswith('$enquiry'):
          await message.channel.send('Enquiry Form Link: https://forms.gle/ekYGfbYBY6Sufkxj9')

  elif  any(word in  msg for word in ["installment","Installment","INSTALLMENT"]):
      await message.channel.send("If you are looking for Installment Form Link use: $installment")
    
  elif  any(word in  msg for word in ["register","Register","REGISTRATION","REGISTER","Registration","registration"]):
      await message.channel.send("If you are looking for Registration Form Link use: $register")

  elif  any(word in  msg for word in ["enquiry","ENQUIRY","Enquiry"]):
      await message.channel.send("If you are looking for Enquiry Form Link use: $enquiry")

  
  
  
  
client.run(TOKEN)




# class Greetings(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self._last_member = None

#     @commands.Cog.listener()
#     async def on_member_join(self, member):
#         channel = member.guild.system_channel
#         if channel is not None:
#             await channel.send(f'Welcome {member.mention}.')

#     @commands.command()
#     async def hello(self, ctx, *, member: discord.Member = None):
#         """Says hello"""
#         member = member or ctx.author
#         if self._last_member is None or self._last_member.id != member.id:
#             await ctx.send(f'Hello {member.name}~')
#         else:
#             await ctx.send(f'Hello {member.name}... This feels familiar.')
#         self._last_member = member




