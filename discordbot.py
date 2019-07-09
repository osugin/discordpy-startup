# インストールした discord.py を読み込む
import discord
import random  # おみくじで使用
import random  # diceで使用

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTk1ODEzMzUxODc1OTM2MjY5.XRx3gA.TwsckxcaLz-94u72JC_CkJO04EI'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 新規メンバー参加時のイベントハンドラ
@client.event
async def on_member_join(member):
    guild = member.guild # サーバー
    sysch = guild.system_channel # 参加メッセージを表示するチャンネル
    if sysch: # チャンネルが設定されてなかったら何もしない
        text = f'{member.mention} よく来たわね！ゆっくりして行くといいわ！'
        await sysch.send(text)


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!neko」と発言したら「にゃーん」が返る処理
    if message.content == '!neko':
        await message.channel.send('にゃーん')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!じー」と発言したら「こっち見んな！！ぶっ殺すわよ！？」が返る処理
    if message.content == '!じー':
        await message.channel.send('こっち見んな！！ぶっ殺すわよ！？')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!キャルちゃん」と発言したら「なによ！なんか用？」が返る処理
    if message.content == '!キャルちゃん':
        await message.channel.send('なによ！なんか用？')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!ねぇねぇ」と発言したら「触んな！」が返る処理
    if message.content == '!ねぇねぇ':
        await message.channel.send('触んな！')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「!つかれた」と発言したら「ゆっくりする？」が返る処理
    if message.content == '!つかれた':
        await message.channel.send('ゆっくりする？')

    if message.content == "!眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.name} 仕方ないわね！寝ていいわよ？おやすみ！")  # f文字列（フォーマット済み文字列リテラル）

    elif message.content == "!投票":
        # リアクションアイコンを付けたい
        q = await message.channel.send("あなたは右利きですか？")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "!おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)

    # 「!おつかれ」で始まるか調べる
    if message.content.startswith("!おつかれ"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おつかれさま！" + message.author.name + "今日もよくがんばったわね！ゆっくり休むのよ！！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

# 「!おはよう」で始まるか調べる
    if message.content.startswith("!おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはよう！" + message.author.name + "今日も頑張って！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)



# クラバトについてのコード
    CHANNEL_ID = 596583155578961935
    boss1 = "ワイバーン"
    boss2 = "ライライ"
    boss3 = "？？？"
    boss4 = "？？？"
    boss5 = "？？？"
    roles1 = 596582248757592077


    if message.content == "/1st":
        
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"<@&{roles1}> ワイバーン")
        
    if message.content == "/2nd":
        
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"<@&{roles1}> ライライ")    

    if message.content == "/3rd":
        
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"<@&{roles1}> ？？？") 
        
    if message.content == "/4th":
        
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"<@&{roles1}> ？？？") 
        
    if message.content == "/5th":
        
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"<@&{roles1}> ？？？") 


    if message.content == "3凸終了":

        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"本日の{message.author.name}さんの凸は終了です、お疲れ様でした")

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ") 

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
