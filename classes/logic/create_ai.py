import json

def create_ai():
    print ('Creating AI...')
    print('Please enter the following details :')
    sex = input('Sex :')
    name = input('Name :')
    height    = input('Height :')
    body_type = input('Body Type :')
    skin_tone = input('Skin Tone : ')
    eye_color = input('Eye Color :')
    hair_color = input('Hair Color :')
    ethnicity = input('Ethnicity :')
    language =input('Language :')
    
    ai_profile = {
            'Sex' : sex,
            'Name' : name,
            'Height' : height,
            'Body Type' : body_type,
            'Skin Tone' : skin_tone,
            'Eye Color': eye_color,
            'Hair Color' : hair_color, 
            'Ethnicity' : ethnicity,
            'Language' : language 
            }

    # Print the ai profile
    print('\nAI profile Created')
    for key, value in ai_profile.items():
        print(f'{key}: {value}')


    # save the user profile to a JSON file
        with open('ai_profile.json', 'w') as json_file:
            json.dump(ai_profile, json_file, indent=4)
            print('\nAI profile has been created to ai_profile.json')

# call the function to create a AI 
create_ai()
