# インストールした discord.py を読み込む
import discord
import random  # おみくじで使用
import re       # 正規表現に必要（残り体力に使用）
from discord.ext import tasks
from datetime import datetime
from discord.ext import commands

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTk1ODEzMzUxODc1OTM2MjY5.XRx3gA.TwsckxcaLz-94u72JC_CkJO04EI'

CHANNEL_T   = 595598763377033227
# user情報リスト
memberid      = []            # クラメンのＩＤを取得するリスト
membername    = []            # クラメンの名前を取得するリスト
usercount     = 0             # クラメンの人数
totsucount    = []            # 凸数リスト
totsunow      = []            # 今凸っているか
simulated     = []            # 今模擬戦中か
taskill       = []            # タスキル回数
bosyu_list    = []            # 凸募集用
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
        q = await message.channel.send("凸宣言はあった方がいいですか？")
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

# メンバーのリストを取得して表示

if message.content == '!update':
        usercount       = 0
        memberid        = []            # クラメンのＩＤリストを初期化する
        membername      = []            # クラメンの名前リストを初期化する
        totsucount      = []            # 凸数リストを初期化する
        totsunow        = []            # 凸状況リストを初期化する
        simulated       = []            # 模擬戦リストを初期化する
        taskill         = []            # タスキルリストを初期化する
       
        for member in message.guild.members:    # user情報を全員チェックする
            
                    membername.append(member.name)
                    memberid.append(member.id)
                    totsucount.append(0)
                    totsunow.append(0)
                    simulated.append(0)
                    taskill.append(0)
                    usercount += 1                  # user数をカウントアップする
                    i=0

 if message.content == "凸":
        # 開始報告した人を名前リストから探し、凸数を更新する
        for i in range(usercount):                      # i=0からi=29まで30回繰り返す処理を実行する
            if memberid[i] == message.author.id:        # 報告者とidが一致したら
                if totsunow[i] == 0:
                    if totsucount[i] >= 3:
                        await message.channel.send(f"{message.author}さん、あなたの凸はもう終わりました。")
                    else:
                        channel = client.get_channel(CHANNEL_T)
                        await channel.send(f"{message.author}さんが " + str(totsucount[i]+1) + "凸開始します。" )
                        totsunow[i] = 1

if message.content == "!凸残り":  # 凸残ってる人だけ表示する場合
        tmessage1 = "1凸残りは\n"
        tmessage2 = "2凸残りは\n"
        tmessage3 = "3凸残りは\n"
        tcount1 = 0
        tcount2 = 0
        tcount3 = 0
        for i in range(usercount):                      # i=0からi=29まで30回繰り返す処理を実行する
            if totsucount[i] == 2:                      # 凸回数2回なら残り1凸
                tmessage1 += membername[i] + "さん\n"
                tcount1 += 1
            elif totsucount[i] == 1:                    # 凸回数1回なら残り2凸
                tmessage2 += membername[i] + "さん\n"
                tcount2 += 1
            elif totsucount[i] == 0:                    # 凸回数0回なら残り3凸
                tmessage3 += membername[i] + "さん\n"
                tcount3 += 1
        tmessage = [tmessage1, tmessage2, tmessage3]
        tcountA = tcount1 + tcount2 + tcount3           #残り人数をカウントアップする
        tcountB = tcount1 + tcount2*2 + tcount3*3       #残り凸数合計をカウントアップする
        tmessage = tmessage1 + tmessage2 + tmessage3
        channel = client.get_channel(CHANNEL_S)
        await channel.send( '---[現在の残り凸状況]---' )
        await channel.send( f'{tmessage}以上 残り{str(tcountA)}人、残り凸数合計{str(tcountB)}よ。' )

    if message.content.startswith("!凸募集@"):
        recruitment = int(message.content[5:])
        text = "あと{}人 募集中\n"
        revmsg = text.format(recruitment)
        #friend_list 押した人のList
        frelist = []
        msg = await message.channel.send(revmsg)
        await msg.add_reaction('\u21a9')
        await msg.add_reaction('\u23eb')
        while len(frelist) < int(message.content[5:]):
            reaction = await client.wait_for("reaction_add")
            bot_reaction = reaction[0]
            bot_member = reaction[1]
            if bot_member != msg.author:
                if bot_reaction.emoji == '\u21a9':
                    if bot_member.name in frelist:
                        frelist.remove(bot_member.name)
                        recruitment += 1
                        await msg.edit(content=text.format(recruitment) + '\n'.join(frelist))
                elif bot_reaction.emoji == '\u23eb':
                    if bot_member.name in frelist:
                        pass
                    else:
                        frelist.append(bot_member.name)
                        recruitment -= 1
                        await msg.edit(content=text.format(recruitment) + '\n'.join(frelist))
                elif bot_reaction.emoji == '✖':
                    await msg.edit(content='募集終了\n'+ '\n'.join(frelist))
                    break
                await msg.remove_reaction(bot_reaction.emoji, bot_member)
        else:
            await msg.edit(content='募集終了\n'+ '\n'.join(frelist))


# クラバトについてのコード
    CHANNEL_ID = 596583155578961935
    boss1 = "ワイバーン"
    boss2 = "ライライ"
    boss3 = "？？？"
    boss4 = "？？？"
    boss5 = "オルレオン"
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
        await channel.send(f"<@&{roles1}> オルレオン") 


    if message.content == "3凸終了":

        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"本日の{message.author.name}さんの凸は終了です、お疲れ様でした")

    elif message.content == "!ダイレクトメッセージ":
        # ダイレクトメッセージ送信
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんにダイレクトメッセージ") 

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
