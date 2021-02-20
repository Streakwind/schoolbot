from discord.ext import commands
import discord
import traceback

class Admin (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def cog_check(self, ctx):
        return await commands.is_owner().predicate(ctx)
    @commands.command()
    async def reload(self, ctx, extension):
        """Reload an extension"""
        try:
            self.bot.reload_extension(extension)  # the extension arg
            await ctx.send (f"{extension} succesfully reloaded.")
        except Exception as e:
            # this next line formats the traceback and sends it
            error = "".join(traceback.format_exception(type(e), e, e.__traceback__, 1))
            return await ctx.send(f"Oh noes! The extension failed to reload! Here's the traceback:\n{error}")
    @commands.command()
    async def changeactidle(self, ctx):
        """Changed the status to idle."""
        await self.bot.change_presence(status=discord.Status.idle)
        await ctx.send ("Success!")
        
    @commands.command()
    async def changeactdnd(self, ctx):
        """Changed the status to DND."""
        await self.bot.change_presence(status=discord.Status.do_not_disturb)
        await ctx.send ("Success!")
        
    @commands.command()
    async def changeactoff(self, ctx):
        """Changed the status to invisible."""
        await self.bot.change_presence(status=discord.Status.invisible)
        await ctx.send ("Success!")
    
    @commands.command()
    async def resetact(self, ctx):
        """Reset the status."""
        await self.bot.change_presence(status=discord.Status.online)
        await ctx.send ("Success!")
    @commands.command()
    async def setplay(self, ctx, *, thing):
        """Set's a play status"""
        await self.bot.change_presence(activity = discord.Game(thing))
        await ctx.send ("Success!")
    @commands.command()
    async def setwatch(self, ctx, *, thing):
        """Set's a watch status"""
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=thing))
        await ctx.send ("Success!")
    @commands.command()
    async def setlisten(self, ctx, *, thing):
        """Set's a listen status"""
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=thing))
        await ctx.send ("Success!")
   # @commands.command()
   # @commands.is_owner()
   # async def changeactplay(self, ctx, status, game):
    #    """Lets the bot play a game."""
   #     await self.bot.change_presence(status=discord.Status.{status} activity={game})
   #     await ctx.send ("Success!")

def setup(bot):
    bot.add_cog(Admin(bot))