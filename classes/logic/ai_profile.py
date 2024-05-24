import json 

def ai_profile():
    # Read the Json file
    with open(file_path, 'r') as json_file:
        ai_profile = json.load(json_file)


    # Print the loaded Ai profile 
    print('Ai profile loaded:')
    for key, val in ai_profile.items():
        print(f'{key}:{val}')
    
    with open(user_path, 'r') as json_file_user:
        user_profile = json.load(json_file_user)
    
    for key, val in user_profile.items():
        if key == name:
            print('................................')
            print('Welcome ' + val)



# Prompt the user for input
file_path = 'ai_profile.json'
user_path = 'user_profile.json'
name = 'name'
ai_profile()
