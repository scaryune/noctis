import json

def read_ai_profile(file_path):
    # Open the Json file for reading
    with open(file_path, 'r') as json_file:
        # Load the contents of the file into a dictionary 
        ai_profile = json.load(json_file)

        # Print the Ai profile
        print('Ai profile loaded :')
        for key, value in ai_profile.items():
            print(f'{key}:{value}')
    
    return ai_profile

# Specify the path to the json file
    
file_path = 'ai_profile.json'

# Call the function to read the uer profile
ai_profile = read_ai_profile(file_path)

