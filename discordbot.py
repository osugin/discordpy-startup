# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTk1ODEzMzUxODc1OTM2MjY5.XRx3gA.TwsckxcaLz-94u72JC_CkJO04EI'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
        
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/じー」と発言したら「じ、じろじろ見てんじゃないわよ！！ぶっ殺すわよ！？」が返る処理
    if message.content == '/じー':
        await message.channel.send('じ、じろじろ見てんじゃないわよ！！ぶっ殺すわよ！？')
# 話しかけた人に返信する

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
