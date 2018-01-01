import json

REMOVE_EXIT_KEYWORD = True # get rid of the "exit" at the end of the cast
START_IMMEDIATELY = True # make first message/prompt appear immediately

with open('data.json') as data_file:
	    data = json.load(data_file)

if (REMOVE_EXIT_KEYWORD):
	stdout = data["stdout"]
	stdout_trimmed = []
	stdout_trimmed = data["stdout"][(len(stdout)-5):len(stdout)]
	stdout_trimmed = [item[1] for item in stdout_trimmed]
	if (''.join(stdout_trimmed) == "exit\r\n"):
		del data["stdout"][(len(stdout)-5):len(stdout)]
	elif (''.join(stdout_trimmed) == "xit\r\nexit\r\n"):
		del data["stdout"][(len(stdout)-5):len(stdout)]


if (START_IMMEDIATELY):
     data["stdout"][0][0] = 0.000000
     data["stdout"][1][0] = 0.000000

print json.dumps(data)
