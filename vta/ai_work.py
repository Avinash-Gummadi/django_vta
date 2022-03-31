from . import normalChat,webScrapping,math_function,dictionary

import math

EXIT_COMMANDS = ['bye','exit','quit','shut down', 'shutdown']
def isContain(txt, lst):
	for word in lst:
		if word in txt:
			return True
	return False

def main(text):
	if 'my name' in text:return 'Avinash'
	if isContain(text, ['time','date']):return normalChat.chat(text)
	if isContain(text, ['morning','evening','noon']) and 'good' in text:return normalChat.chat("good")
	if isContain(text, ['news']):
		msg = "<br><b>Latest news.....</b> <br><br>"

		headlines,headlineLinks = webScrapping.latestNews(2)
		for idx,head in enumerate(headlines):
			msg += f'{idx+1}. {head} <br>'
		return msg
	# print(text)
	#,'log','value of','root of','math',,'binary','hexadecimal','octal','shift','sin','cos','tan','cosec','sec','cot']):
	if isContain(text, ['factorial of ']):
				num = text.split('factorial of')[1]
				num = int(num)
				res = math.factorial(num)
				return res
	if isContain(text, ['log of ']):
				num = text.split('log of')[1]
				num = int(num)
				res = math.log(num)
				return res
	if isContain(text,['+','-','*','/']):
		return eval(text)
	if isContain(text,['plus','minus','multiply','dividedby']):
		return math_function.basicOperations(text)
	if isContain(text,['right shift','left shift']):
		return math_function.bitwiseOperations(text)
	if isContain(text,['sin','cos','tan','cosec','sec','cot']):
		return math_function.trigonometry(text)
	if isContain(text,['bin','hex','oct']):
		return math_function.conversions(text)
	result = normalChat.reply(text)
	if result != "None":
		return result
	else:
		return f"I didn't recognise {text}. If you like to google it <a href='https://www.google.com/search?q={text}' target='_blank'>click here</a>"

def keyboardInput(input_msg):
	user_input = input_msg.lower()
	if user_input!="":
		if isContain(user_input, EXIT_COMMANDS):
			return "Bye, have a nice day."
		else:return main(user_input)
