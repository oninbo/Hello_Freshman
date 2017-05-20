import logging

bot_logger = logging.getLogger("bot")
fh = logging.FileHandler('bot.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
bot_logger.addHandler(fh)
bot_logger.addHandler(ch)