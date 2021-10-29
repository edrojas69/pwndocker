from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import validators
import os

TOKEN_BOT = '##' 
__VERSION__="0.1"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hacking!!..')


def help(update, context):
    """Send a message when the command /help is issued."""
    msg_help= """
/help       -   Show this help
/pwn        -   Do the thing EX. /pwn dirsearch https://localhost/
/toolslist  -   List of avaible tools
/wordlist   -   List all the bot wordlist
/version    -   Show bot develop version
    """
    update.message.reply_text(msg_help)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


####################################################################################

list_tools= ['subfinder', 'wfuzz', 'dirsearch', 'nmap', 'sqlmap']
special_tools = ['wfuzz', 'dirsearch','sqlmap']
poc=['id','whoami']

####################################################################################

def validar(update, context):
    tool = context.args[0]
    host = context.args[1]
    try:
        if len(tool) != 0 and len(host) != 0:
            if tool == "nmap":
                if validators.domain(host) or validators.ip_address.ipv4(host):
                    output = dockerComand(tool, host)
                    update.message.reply_text(output)
                else:
                    update.message.reply_text("Error")

            elif tool == "subfinder":
                if validators.domain(host):
                    output = dockerComand(tool, host)
                    update.message.reply_text(output)
                else:
                    update.message.reply_text("Error")

            elif tool in special_tools:
                if validators.url(host):
                    output = dockerComand(tool, host)
                    update.message.reply_text(output)
                
            else:
                update.message.reply_text("Error")
    except:
        pass


def dockerComand(tool, host):
    try:
        
        resp = os.popen('docker run --rm -it pwntools sh -c "'+tool+' '+host+'"').read()
        if len(resp) !=0:
            os.system('docker rm $(docker ps -a -q) --force 2>/dev/null ')    
            return resp
        else:
            os.system('docker rm $(docker ps -a -q) --force 2>/dev/null ')
            return("Error")
    except:
        os.system('docker rm $(docker ps -a -q) --force 2>/dev/null ')
    

def tools_list(update, context):
    msg="""
    Herraminetas disponible\n
    gobuster
    ffuf
    dirsearch
    nmap
    sqlmap
    """
    update.message.reply_text(msg)


def list_wordlist(update, context):
    wordlist="""
    apache-user-enum-1.0.txt
    apache-user-enum-2.0.txt
    directory-list-1.0.txt
    directory-list-2.3-big.txt
    directory-list-2.3-medium.txt
    rockyou.txt.gz
    """
    update.message.reply_text(wordlist)


def version(update, context):
    update.message.reply_text("Version en desarrollo: "+__VERSION__)
    

def main():
    updater = Updater(TOKEN_BOT, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("pwn", validar))
    dp.add_handler(CommandHandler("toolslist", tools_list))
    dp.add_handler(CommandHandler("wordlist", list_wordlist))
    dp.add_handler(CommandHandler("version", version))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
