import os
import encode
import telebot
import ok as pl
BOT_TOKEN = "abc"

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    text="""What type of data do you intend to deal with
Text
number"""
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, datatyp)
def datatyp(message):
    if(message.text=='number'):
        text="""encode  or  decode"""
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, encodeordecodenum)
    elif(message.text=='text'):
        text="""encode  or  decode"""
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, encodeordecodestr)
    
    else:
        text="invalid option"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, datatyp)
    
def encodeordecodenum(message):
    if(message.text=='encode'):
        text="Enter Data"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,abc )
    elif(message.text=='decode'):
        text="Enter Data"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,abcd )
    else:
        text="Choose valid option"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, encodeordecodenum)
def abc(message):
    a=encode.driver(int(message.text),"encrypt")
    text=a
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    text="press 1 to continue and 2 to exit"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, ex)
def abcd(message):
    a=encode.driver(int(message.text),"decrypt")
    text=a
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    text="press 1 to continue and 2 to exit"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, ex)

def encodeordecodestr(message):
    if(message.text=='encode'):
        text="Enter Data"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg,stra )
        
    elif(message.text=='decode'):
        text="Enter Data"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, strab)
    else:
        text="Choose valid option"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, encodeordecodestr)
def stra(message):
    a=pl.playfair(message.text)
    text=a
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    text="press 1 to continue and 2 to exit"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, ex)
def strab(message):
    a=pl.playfair(message.text,False)
    text=a
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    text="press 1 to continue and 2 to exit"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, ex)
def ex(message):
    if (message.text=="1"):
        text="""What type of data do you intend to deal with
Text
number"""
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, datatyp)
    else:
        exit



bot.infinity_polling()