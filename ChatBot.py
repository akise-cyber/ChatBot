!pip install chatterbot
!pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Jamilton')
bot = ChatBot(
    'Jamilton',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
    
conversa = ListTrainer(bot)
conversa.train([
   'Oi',
   'Olá',
   'Qual seu nome?',
   'Jamilton',
   'Prazer',
   'O prazer é todo meu',
   'Estou com um problema',
   'Em que posso ajudar?',
   'Quantos anos você tem?',
   'Tenho 1 dia de existência',
   'Tenho que ir',
   'Tudo bem, volte sempre',
   'KKKK',
   'Ri não safado',
])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.portuguese')

while True:
  resposta = bot.get_response(input("Usuário: "))
  if float(resposta.confidence) > 0.5:
      print("Jamilton: ", resposta)
  else:
      print("Desculpe, eu não entendi!")
