import json 

def create_user():
    print('Creating User...')
    print('Please enter the following details :')
    sex = input('Sex :')
    name = input('Name :')
    height = input('Height :')
    body_type = input('Body Type :')
    skin_tone = input('Skin Tone :')
    eye_color = input('Eye Color :')
    hair_color = input('Hair Color :')
    ethnicity = input('Ethnicity :')
    language= input('Language :')

    user_profile = {
            'sex' : sex,
            'name' : name,
            'height' : height, 
            'Body Type' : body_type,
            'Skin Tone': skin_tone,
            'Eye Color' : eye_color,
            'Hair Color' : hair_color,
            'Ethnicity' : ethnicity,
            'Language' : language,
            }

    print('\nUser profile Created')
    for key, value in user_profile.items():
        print(f'{key}: {value}')

        with open('user_profile.josn', 'w') as json_file:
            json.dump(user_profile, json_file, indent=4)
            print('\nUser profile has been created to user_profile.json')

create_user()
