import json

def modify_ai(file_path, modifier, value):
    # Read the JSON file
    with open(file_path, 'r') as json_file:
        ai_profile = json.load(json_file)

    # Print the loaded AI profile
    print('AI profile loaded:')
    for key, val in ai_profile.items():
        print(f'{key}: {val}')
    
    # Modify the value of the specified key
    if modifier in ai_profile:
        ai_profile[modifier] = value
    else:
        print(f'Key "{modifier}" not found in the AI profile')
        return
    
    # Write the modified AI profile back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(ai_profile, json_file, indent=4)
        print('\nAI profile has been updated successfully')

    # Print the modified AI profile
    print('\nModified AI Profile:')
    for key, val in ai_profile.items():
        print(f'{key}: {val}')

# Prompt the user for input
modifier = input('What key do you want to change: ')
value = input('Insert the value: ')
file_path = 'ai_profile.json'

# Call the function to modify the AI profile
modify_ai(file_path, modifier, value)
