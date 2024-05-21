import json

def modify_ai(file_path, modifier, value):
    with open(file_path,'r') as json_file:
        ai_profile = json.load(json_file)

        print('Ai profile loaded :')
        for key, value in ai_profile.items():
            print(f'{key}:{value}')
    
    if modifier in ai_profile :
       ai_profile[modifier] = value
    else:
        print(f'Key "{modifier}" not found in the AI profile')

    with open('ai_profile.json', 'w') as json_file:
        json.dump(ai_profile, json_file, indent=4)
        print('\n Ai profile has updated with sucess ')

modifier = input('what key you want change :')
value = input('Insert the value :')
file_path = 'ai_profile.json'

ai_profile = modify_ai(file_path, modifier, value)
