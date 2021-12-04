pip install dostoevsky
!python -m dostoevsky download fasttext-social-network-model
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

messages = [
    'козел! ненавижу тебя',
    'Ты первоклассный специалист! умничка',
    'Арина - лучший капитан команды и друг',
    'да пошел ты к черту'
]

results = model.predict(messages, k=2)

for message, sentiment in zip(messages, results):
    print(message, '->', sentiment)