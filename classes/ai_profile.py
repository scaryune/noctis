import json 

def ai_profile():
    # Read the Json file
    with open(file_path, 'r') as json_file:
        ai_profile = json.load(json_file)
        user_profile = json.load(json_file)

    # Print the loaded Ai profile 
    print('Ai profile loaded:')
    for key, val in ai_profile.items():
        print(f'{key}:{val}')

    user_profile.items()
    print('Welcome')





# Prompt the user for input
file_path = 'ai_profile.json'
user_path = 'user_profile.json'

ai_profile()
