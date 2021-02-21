from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, banreason=None):
      """Bans a specified user from the guild"""
      await member.ban(reason=banreason)
      await ctx.send(f"{member} has been banned by {ctx.author}. Reason: {banreason}")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, kickreason=None):
      """Kicks a specified user from the guild"""
      await member.kick(reason=kickreason)
      await ctx.send(f"{member} has been kicked by {ctx.author}. Reason: {kickreason}")

def setup(bot):
    bot.add_cog(Moderation(bot))