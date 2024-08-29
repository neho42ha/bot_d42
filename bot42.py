import discord

# Настройка необходимых intents для работы с сообщениями и реакциями
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.messages = True

# Создаем клиента с указанными intents
client = discord.Client(intents=intents)

# Задаем ID канала, из которого пересылаются сообщения
SOURCE_CHANNEL_ID = 1277957800936345675  # Замените на ID вашего исходного канала
# Задаем ID канала, в который пересылаются сообщения
TARGET_CHANNEL_ID = 1277958802716758067  # Замените на ID вашего целевого канала

@client.event
async def on_ready():
    print(f'Бот {client.user} успешно запущен!')

@client.event
async def on_reaction_add(reaction, user):
    # Проверяем, что реакция добавлена в нужный канал и что это эмодзи ❤️
    if reaction.message.channel.id == SOURCE_CHANNEL_ID and str(reaction.emoji) == '❤️':
        target_channel = client.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            # Отправляем сообщение в целевой канал
            await target_channel.send(
                f'Пересланное сообщение от {reaction.message.author}:\n{reaction.message.content}'
            )

client.run('1278603399650086953')