import discord
import config
import rules as r

from discord.ext import commands
import random

description = '''Random bot i made just now'''
bot = commands.Bot(command_prefix='/', description=description)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')





@bot.command()
async def (*, rule : str):
    def handle_comment(comment, rules_list, awards_list):
	words = comment.body.lower().split(" ")
	terms = []
	if (words[0].lower() == "!award"):
		terms = get_rules_list(awards_list, words[1:])
	elif (words[0].lower() == "!rule"):
		terms = get_rules_list(rules_list, words[1:])
	else:
		return False
	reply_text = ""
	for term in terms:
		reply_text += term[0] + ":\n" + term[1] + "\n"
	if(reply_text != ""):
		reply_text+= "&nbsp;&nbsp;\n\n^^Bot ^^by ^^Ethan ^^Schaffer. ^^Check ^^out ^^the ^^[GitHub](https://github.com/ethan-schaffer/reddit-bot) ^^or ^^send ^^me ^^a ^^PM!"
		print("Going to comment:")
		print(reply_text)
        return reply_text
	
    def get_rules_list(rules_list, query_list):
	    good_rules = []
	    for rule in rules_list:
		    is_good = 0
		    is_bad = 0
		for query in query_list:
			if (query not in rule[1].lower()) and (query != rule[0].lower()):
				is_bad+=1
			else:
				is_good+=1
		percent = ( is_good / (is_good+is_bad) )
		if percent >= .75:
			good_rules.append(rule)
	return good_rules

    await bot.say(handle_comment(rule, rules.rules, rules.awards)
                  










bot.run(config.token)
