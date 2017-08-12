import rules

import discord
from discord.ext import commands


description = '''Random bot i made just now'''
bot = commands.Bot(command_prefix='!', description=description)

def find_rule(text):
    return handle_comment(text, rules.rules, rules.awards, True)


def find_award(text):
    return handle_comment(text, rules.rules, rules.awards, False)


def handle_comment(comment, rules_list, awards_list, rule):
    words = comment.lower().split(" ")
    if rule:
        terms = get_rules_list(rules_list, words)
    else:
        terms = get_rules_list(awards_list, words)

    reply_text = ""

    for term in terms:
        reply_text += term[0] + ":\n" + term[1] + "\n"

    return reply_text


def get_rules_list(rules_list, query_list):
    good_rules = []
    for rule in rules_list:
        is_good = 0
        is_bad = 0
        for query in query_list:
            if (query not in rule[1].lower()) and (query != rule[0].lower()):
                is_bad += 1
            else:
                is_good += 1
        percent = (is_good / (is_good + is_bad))
        if percent >= .75:
            good_rules.append(rule)
    return good_rules


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def rule(ctx, *, search: str):
    rule_em = discord.Embed(title="Here's what I found for '{}'...".format(search), description=find_rule(search), color=0xFFA500)
    rule_em.set_footer(text="{}".format(ctx.message.server.name), icon_url=ctx.message.server.icon_url)
    await bot.say(embed=rule_em)


@bot.command(pass_context=True)
async def award(ctx, *, search : str):
    award_em = discord.Embed(title="Here's what I found for '{}'...".format(search), description=find_award(search), color=0xFFA500)
    award_em.set_footer(text="{}".format(ctx.message.server.name), icon_url=ctx.message.server.icon_url)
    await bot.say(embed=award_em)


bot.run('')

