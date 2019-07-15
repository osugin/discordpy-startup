# インストールした discord.py を読み込む
import discord
import random  # おみくじで使用
import random  # diceで使用
from discord.ext import commands
import asyncio
import wikipedia
import requests
import json
import random

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
    # 「キャルちゃん」で始まるか調べる
    if message.content.startswith("キャルちゃん"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            try:
                user_name = message.author.name
                text = message.content
                print(text)
                print(type(text))

                ################# Don't touch. ################
                kumo_san = '╭◜◝ ͡ ◜◝╮ \n(   •ω•　  ) \n╰◟◞ ͜ ◟◞╯ < '
                ################# Don't touch. ################

                msg =  kumo_san + user_name + 'さん '
                #msg = user_name + 'さん '

                if text == ('キャルちゃん'):
                    msg = 'はい！ご用でしょうか！'
                elif text.find('おは') > -1:
                    msg += 'おはよう！'
                elif text.find('こんにちは') > -1 or text.find('こんちゃ') > -1 or text.find('やあ') > -1 or text.find('おっす') > -1:
                    msg += 'こんにちは！'
                elif text.find('こんばん') > -1 or text.find('ばんわ') > -1:
                    msg += 'こんばんは！'
                elif text.find('おつ') > -1 or text.find('疲') > -1 or text.find('お先') > -1 or text.find('おち') > -1 or text.find('落ち') > -1:
                    msg += 'おつかれ！'
                elif text.find('自己紹介して') > -1:
                    msg = 'はじめまして！みんなのキャルちゃんよ！精一杯頑張るからよろしくね！'
                elif text.find('help') > -1 or text.find('-h') > -1:
                    msg += 'https://discordapp.com/channels/407045885281828877/407050154315874315/558382007433035786'
                elif text.find('って何') > -1:
                    msg += wikipediaSearch(text)
                elif text.find('天気') > -1:
                    msg += getWeatherInformation(text)
                elif text.find('は素数') > -1:
                    msg += primarity_test(text, 50)
                else:
                    msg += 'その言葉は知らなかったから調べたよ。\n' + wikipediaSearch(text)
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, msg)
                return msg
            except Exception as e:
                print(e)
                raise e

# Get Weather Infomation
def getWeatherInformation(text):
    weather_api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    response_string = ''
    city_id = ''
    if text.find('長野') > -1:
        city_id = '200010'
    elif text.find('大阪') > -1:
        city_id = '270000'
    elif text.find('東京') > -1:
        city_id = '130010'
    elif text.find('北海道') > -1 or text.find('札幌') > -1:
        city_id = '016010'
    elif text.find('愛知') > -1 or text.find('名古屋') > -1:
        city_id = '230010'
    elif text.find('佐賀') > -1:
        city_id = '410010'
    else:
        city_id = '130010'
        response_string += '場所が聞き取れなかったので取り敢えず'

    try:
        params = {'city':city_id}
        response = requests.get(weather_api_url,params=params)
        response_dict = json.loads(response.text)
        title = response_dict["title"]
        description = response_dict["description"]["text"]
        response_string += title + "です！\n\n"
        forecasts_array = response_dict["forecasts"]
        forcast_array = []
        for forcast in forecasts_array:
            telop = forcast["telop"]
            telop_icon = ''
            if telop.find('雪') > -1:
                telop_icon = ':showman:'
            elif telop.find('雷') > -1:
                telop_icon = ':thunder_cloud_and_rain:'
            elif telop.find('晴') > -1:
                if telop.find('曇') > -1:
                    telop_icon = ':partly_sunny:'
                elif telop.find('雨') > -1:
                    telop_icon = ':partly_sunny_rain:'
                else:
                    telop_icon = ':sunny:'
            elif telop.find('雨') > -1:
                telop_icon = ':umbrella:'
            elif telop.find('曇') > -1:
                telop_icon = ':cloud:'
            else:
                telop_icon = ':fire:'

            temperature = forcast["temperature"]
            min_temp = temperature["min"]
            max_temp = temperature["max"]
            temp_text = ''
            if min_temp is not None:
                if len(min_temp) > 0:
                    temp_text += '\n最低気温は' + min_temp["celsius"] + "℃"
            if max_temp is not None:
                if len(max_temp) > 0:
                    temp_text += '\n最高気温は' + max_temp["celsius"] + "℃"

            forcast_array.append(forcast["dateLabel"] + ' ' + telop + telop_icon + temp_text)
        if len(forcast_array) > 0:
            response_string += '\n\n'.join(forcast_array)
        response_string += '\n\n' + description
    except Exception as e:
        response_string = '天気検索でエラーです＞＜ :cold_sweat:\n' + e.message + '\n' + str(e)
    return response_string

# Search from Wikipedia
def wikipediaSearch(text):
    response_string = ''
    wikipedia.set_lang('ja')
    index_st = text.find(' ')
    index_ed = text.find('って何')
    search_text = text[index_st:index_ed]
    search_response = wikipedia.search(search_text)
    print(search_response)
    if len(search_response) > 0:
        try:
            wiki_page = wikipedia.page(search_response[0])
        except Exception as e:
            try:
                wiki_page = wikipedia.page(search_response[1])
            except Exception as e:
                response_string = 'お探しの言葉ではエラーを起こしました！:cold_sweat:\n' + e.message + '\n' + str(e)
        response_string = '説明しよう！\n'
        response_string += wiki_page.content[0:200] + '.....\n'
        response_string += wiki_page.url
    else:
        response_string = '今はまだ見つけられないンゴ…でも頑張って見つけられるようになるゾ〜！'

    return response_string

# Miller-Rabin Primality Test
def primarity_test(text, k):
    response_string = ''
    index_st = text.find(' ')
    index_ed = text.find('は素数')
    q = int(text[index_st:index_ed])
    if q == 2:
        response_string = str(q) + 'は素数です！:laughing:'
        return response_string
    if q < 2 or q & 1 == 0:
        response_string = str(q) + 'は素数じゃないです！:rage:'
        return response_string

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q-1)
        t = d
        y = pow(a, t, q)
        while t != q-1 and y != 1 and y != q-1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q-1 and t & 1 == 0:
            response_string = str(q) + 'は素数です！:smile:'
        response_string = str(q) + 'は素数です！:wink:'
    return response_string

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
