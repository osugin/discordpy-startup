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
    # 「/じー」と発言したら「こっち見んな！！ぶっ殺すわよ！？」が返る処理
    if message.content == '/じー':
        await message.channel.send('こっち見んな！！ぶっ殺すわよ！？')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/キャルちゃん」と発言したら「なによ！なんか用？」が返る処理
    if message.content == '/キャルちゃん':
        await message.channel.send('なによ！なんか用？')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/ねぇねぇ」と発言したら「触んな！」が返る処理
    if message.content == '/ねぇねぇ':
        await message.channel.send('触んな！')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/つかれた」と発言したら「ゆっくりする？」が返る処理
    if message.content == '/つかれた':
        await message.channel.send('ゆっくりする？')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
