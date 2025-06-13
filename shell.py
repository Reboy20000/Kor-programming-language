import Kor


# Track last command status
last_command_success = True

while True:
	# Set arrow color based on last command status

	text = input('Kor' + ' ❯ ')
	
	if text.strip() == "exit": break
	if text.strip() == "-v" or "--v" or "-verison" or "--verison": print("Sling [version 1.0.0]")
	if text.strip() == "help":
		print("""
		Available commands:
		exit - Exit the interpreter
		help - Show this help message
		""")
		last_command_success = True
		continue
	if text.strip() == "copyright":
		print("""
		Copyright (c) 2025 Kor by Reyaansh Sinha.
		All rights reserved.
		""")
		last_command_success = True
		continue
	if text.strip() == "version":
		print("Sling [version 1.0.0]")
		last_command_success = True
		continue
	if text.strip() == "credits":
		print("""
		Credits:
		Reyaansh Sinha
		""")
		last_command_success = True
		continue
	if text.strip() == "": 
		last_command_success = True
		continue
		
	result, error = Kor.run('<stdin>', text)

	if error:
		print(error.as_string())
		last_command_success = False
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
		last_command_success = True
