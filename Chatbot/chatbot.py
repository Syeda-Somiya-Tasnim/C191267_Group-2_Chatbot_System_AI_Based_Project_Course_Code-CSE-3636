
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatBot = ChatBot('ChatBot')

trainer=ChatterBotCorpusTrainer(chatBot)

trainer.train("chatterbot.corpus.english")

print(chatBot.get_response("Hello"))