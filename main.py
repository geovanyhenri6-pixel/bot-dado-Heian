import random 
import discord 
import os

intents = discord.Intents.default() 
intents.message_content = True 

client = discord.Client(intents=intents) 

# acertos especiais-------------------------------------------
#-------------------------------------------------------------

acerto_crit = ["🌟 O destino claramente está ao seu lado.",
            "⚡ Tudo acontece exatamente como você esperava.",
            "👑 Uma execução impecável.",
            "🍀 Sorte e habilidade caminharam juntas dessa vez.",
            "🌌 Parece até que o universo conspirou a favor.",
            "✨ Um resultado melhor do que o imaginado.",
            "🕊️ Nenhum obstáculo foi capaz de impedir você.",
            "🔥 Isso provavelmente vai virar história depois.",
            "🎯 Precisão absoluta. Nada saiu errado.",
            "🏆 Um momento raro de perfeição.",
            "☄️ Algo praticamente impossível acaba de acontecer.",
            "🌠 Nem os mais experientes acreditariam nisso.",
            "👑 Seu nome mereceria entrar para a história.",
            "⚡ O acaso atingiu seu auge absoluto.",
            "🌌 Por um instante, tudo pareceu alinhado.",
            "🐉 Até a sorte ficou impressionada.",
            "✨ Você ultrapassou todos os limites esperados.",
            "🔥 Um acontecimento digno de lendas.",
            "🎭 A realidade simplesmente decidiu favorecer você.",
            "🌟 Existem milagres… e existe isso."]

acerto_otm = ["✨ As chances claramente estavam ao seu favor.",
            "🌟 Um resultado acima do esperado.",
            "⚡ Tudo parece fluir perfeitamente.",
            "🍀 A sorte resolveu colaborar dessa vez.",
            "🎯 Você chegou muito perto da perfeição.",
            "🔥 Um resultado impressionante.",
            "🌌 O destino parece sorrir para você.",
            "🕊️ Poucas coisas poderiam ter dado tão certo.",
            "👑 Uma performance digna de destaque.",
            "📈 Melhor do que a maioria conseguiria."]

erro_feio = ["🌧️ As coisas definitivamente poderiam ter saído melhor.",
            "💨 A sorte passou longe dessa vez.",
            "⚠️ Um resultado abaixo do esperado.",
            "🫠 Algo claramente deu errado no caminho.",
            "📉 Não foi exatamente um grande momento.",
            "😵 O destino não colaborou muito.",
            "🪨 Você encontrou dificuldade onde menos esperava.",
            "🤏 Quase deu certo… quase.",
            "🌫️ O resultado ficou longe do ideal.",
            "🎭 Nem sempre os dados são gentis."]

erro_crit = ["💀 O pior cenário possível acabou de acontecer.",
            "🌧️ Nem a sorte quis ajudar dessa vez.",
            "🤡 Isso definitivamente não saiu como planejado.",
            "🪨 Você tropeçou no próprio destino.",
            "💨 Tudo deu errado ao mesmo tempo.",
            "🫠 Talvez seja melhor fingir que isso nunca aconteceu.",
            "🕳️ A situação conseguiu piorar de alguma forma.",
            "😵 O universo claramente tinha outros planos.",
            "📉 Um resultado dolorosamente desastroso."]

#---------------------------------------------------------------
#---------------------------------------------------------------

@client.event 
async def on_ready(): print("Dados Prontos!") 

@client.event 
async def on_message(message): 
    
    if message.author == client.user:
        return 
    
    if message.content.lower().startswith("r"):

        partes = message.content.split()
        comando = partes[0]
        lado = comando[1:]

        if lado.isdigit():
            lado = int(lado)
            rdado = random.randint(1, lado)
        #dados---------------------------------------------------
        #--------------------------------------------------------
        if lado > 2 and rdado == lado:
            await message.reply(f"Dado do(a) {message.author.display_name} '{" ".join(partes[1:])}' -> {rdado}\n\n{random.choice(acerto_crit)}")

        elif lado > 2 and rdado == 1:
            await message.reply(f"Dado do(a) {message.author.display_name} '{" ".join(partes[1:])}' -> {rdado}\n\n{random.choice(erro_crit)}")

        elif lado > 2 and rdado >= lado * 0.80:
            await message.reply(f"Dado do(a) {message.author.display_name} '{" ".join(partes[1:])}' -> {rdado}\n\n{random.choice(acerto_otm)}")

        elif lado > 2 and rdado <= lado * 0.20:
            await message.reply(f"Dado do(a) {message.author.display_name} '{" ".join(partes[1:])}' -> {rdado}\n\n{random.choice(erro_feio)}")

        else:
            await message.reply(f"Dado do(a) {message.author.display_name} '{" ".join(partes[1:])}' -> {rdado}")

        #--------------------------------------------------------
        #--------------------------------------------------------

token = os.getenv("DISCORD_TOKEN")
client.run(token)