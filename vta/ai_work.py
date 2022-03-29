from . import normalChat
EXIT_COMMANDS = ['bye','exit','quit','shut down', 'shutdown']
def isContain(txt, lst):
	for word in lst:
		if word in txt:
			return True
	return False

def main(text):
	if 'my name' in text:return 'Avinash'
	if isContain(text, ['time','date']):return normalChat.chat(text)

def keyboardInput(input_msg):
	user_input = input_msg.lower()
	if user_input!="":
		if isContain(user_input, EXIT_COMMANDS):
			return "Bye, have a nice day."
		else:return main(user_input)
