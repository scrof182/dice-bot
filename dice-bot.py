import random
import discord
from discord.ext.commands import Bot
import re
from creds import TOKEN


BOT_PREFIX = ("`")
client = Bot(command_prefix=BOT_PREFIX)

def roll_dice(faces):
	value = random.randint(1, faces)
	return(value)

def single_die(face_1):
	new_reply = str(roll_dice(int(face_1)))
	return new_reply

def single_die_p_mod(face_1, sign_1, mod_1):
	roll_1 = int(single_die(face_1))
	if sign_1 == "-":
		both = roll_1 - mod_1
	else:
		both = roll_1 + mod_1
	new_reply = str(roll_1) +  sign_1 + str(mod_1) + " = " + str(both)
	return new_reply

def multi_die(multi_die_tester):
	count = int(multi_die_tester.group(1))
	faces = int(multi_die_tester.group(2))
	dice = []
	for i in range(0, int(count)):
		new_int = (roll_dice(int(faces)))
		dice.append(new_int)
	newstring = "["
	total = 0
	for i in range(0, len(dice)):
		newstring = newstring + str(dice[i]) + " + "
		total = total + dice[i]
	newstring = newstring.rstrip(" + ")
	newstring = newstring + "] = "
	new_reply = newstring + str(total)
	return new_reply 

def advantage(advantage_tester):
	count = int(advantage_tester.group(1))
	faces = int(advantage_tester.group(2))
	type_of = str(advantage_tester.group(3))
	kept = int(advantage_tester.group(4))
	dice = []
	for i in range(0, int(count)):
		new_int = (roll_dice(int(faces)))
		dice.append(new_int)
	newstring = "Rolled: " + str(dice) + "  Kept: ["
	if type_of == "k":
		dice.sort(reverse=True)
		high_dice = dice[:kept]
		for i in range(0, len(high_dice)):
			newstring = newstring + str(high_dice[i]) + " + "
		newstring = newstring.rstrip(" + ")
		new_reply = newstring + "]"
	else:
		dice.sort()
		low_dice = dice[:kept]
		for i in range(0, len(low_dice)):
			newstring = newstring + str(low_dice[i]) + " + "
		newstring = newstring.rstrip(" + ")
		new_reply = newstring + "]"
	return new_reply

def multi_die_p_mod(multi_die_p_mod_tester):
	count = int(multi_die_p_mod_tester.group(1))
	faces = int(multi_die_p_mod_tester.group(2))
	sign = str(multi_die_p_mod_tester.group(3))
	mod = int(multi_die_p_mod_tester.group(4))
	dice = []
	for i in range(0, int(count)):
		new_int = (roll_dice(int(faces)))
		dice.append(new_int)
	newstring = "["
	total = 0
	for i in range(0, len(dice)):
		newstring = newstring + str(dice[i]) + " + "
		total = total + dice[i]
	if sign == "+":
		mod_total = total + mod
		newstring = newstring.rstrip(" + ")
		newstring = newstring + "] + "
		newstring = newstring + str(mod)
		newstring = newstring + " = "
		new_reply = newstring + str(mod_total)
	else:
		mod_total = total - mod
		newstring = newstring.rstrip(" + ")
		newstring = newstring + "] - "
		newstring = newstring + str(mod)
		newstring = newstring + " = "
		new_reply = newstring + str(mod_total)
	return new_reply 

def advantage_mod(advantage_mod_tester):
	count = int(advantage_mod_tester.group(1))
	faces = int(advantage_mod_tester.group(2))
	type_of = str(advantage_mod_tester.group(3))
	kept = int(advantage_mod_tester.group(4))
	sign = str(advantage_mod_tester.group(5))
	mod = int(advantage_mod_tester.group(6))
	dice = []
	for i in range(0, int(count)):
		new_int = (roll_dice(int(faces)))
		dice.append(new_int)
	newstring = "Rolled: " + str(dice) + "  Kept: ["
	if type_of == "k":
		dice.sort(reverse=True)
		high_dice = dice[:kept]
		print(str(high_dice))
		for i in range(0, len(high_dice)):
			newstring = newstring + str(high_dice[i]) + " + "
		newstring = newstring.rstrip(" + ")
		newstring = newstring + "]"
		modded = []
		if sign == "-":
			for i in range(0, len(high_dice)):
				new_number = int(high_dice[i]) - mod
				modded.append(new_number)
			new_reply = newstring + "    With modifier:   " + str(modded)
		else: 
			for i in range(0, len(high_dice)):
				new_number = int(high_dice[i]) + mod
				modded.append(new_number)
			new_reply = newstring + "    With modifier:   " + str(modded)
	else:
		dice.sort()
		low_dice = dice[:kept]
		for i in range(0, len(low_dice)):
			newstring = newstring + str(low_dice[i]) + " + "
		newstring = newstring.rstrip(" + ")
		newstring = newstring + "]"
		modded = []
		if sign == "-":
			for i in range(0, len(low_dice)):
				new_number = int(low_dice[i]) - mod
				modded.append(new_number)
			new_reply = newstring + "    With modifier:   " + str(modded)
		else: 
			for i in range(0, len(low_dice)):
				new_number = int(low_dice[i]) + mod
				modded.append(new_number)
			new_reply = newstring + "    With modifier:   " + str(modded)
	return new_reply


@client.command(aliases=['r'])
async def roll(ctx, arg):
	#Single Die
	single_die_re = ("^d(\d+)$")
	single_die_parser = re.compile(single_die_re)
	single_die_tester = single_die_parser.match(arg)
	#Single Die + modifier
	single_die_p_mod_re = ("^d(\d+)(\+|\-)(\d+)$")
	single_die_p_mod_parser = re.compile(single_die_p_mod_re)
	single_die_p_mod_tester = single_die_p_mod_parser.match(arg)
	#Multiple die
	multi_die_re = ("^(\d+)d(\d+)$")
	multi_die_parser = re.compile(multi_die_re)
	multi_die_tester = multi_die_parser.match(arg)
	#Multiple die + modifer
	multi_die_p_mod_re = ("^(\d+)d(\d+)(\+|\-)(\d+)$")
	multi_die_p_mod_parser = re.compile(multi_die_p_mod_re)
	multi_die_p_mod_tester = multi_die_p_mod_parser.match(arg)
	# Advantage and Disadvantage
	advantage_re = ("^(\d+)d(\d+)(k|l|kl)(\d+)$")
	advantage_parser = re.compile(advantage_re)
	advantage_tester = advantage_parser.match(arg)
	# Advantage and Disadvantage with mods
	advantage_mod_re = ("^(\d+)d(\d+)(k|l|kl)(\d+)(\+|\-)(\d+)$")
	advantage_mod_parser = re.compile(advantage_mod_re)
	advantage_mod_tester = advantage_mod_parser.match(arg)

	if single_die_tester is not None:
		face_1 = int(single_die_tester.group(1))
		new_reply = single_die(face_1)

	elif single_die_p_mod_tester is not None:
		face_1 = int(single_die_p_mod_tester.group(1))
		sign_1 = str(single_die_p_mod_tester.group(2))
		mod_1 = int(single_die_p_mod_tester.group(3))
		new_reply = single_die_p_mod(face_1, sign_1, mod_1)

	elif multi_die_tester is not None:
		new_reply = multi_die(multi_die_tester)

	elif multi_die_p_mod_tester is not None:
		new_reply = multi_die_p_mod(multi_die_p_mod_tester)

	elif advantage_tester is not None:
		new_reply = advantage(advantage_tester)

	elif advantage_mod_tester is not None:
		new_reply = advantage_mod(advantage_mod_tester)

	else:
		new_reply = "You have exceeded operational parameters, please try again"

	await ctx.send(f'{ctx.author.mention} ' + new_reply)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
