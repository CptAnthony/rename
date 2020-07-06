import os
import time

# Ask user for file path.
file_path = input('What is the file path?')
# Ask user for show_name value.
show_name = input('What is the name of the show?')
# Ask user for season value.
season = input('What is the show season (01, 02, etc.)?')

for episode, old_name in enumerate(os.listdir(file_path), 1):
    # Creates episode_string.
    if episode < 10:
        episode_string = 'E0' + str(episode)
    else:
        episode_string = 'E' + str(episode)
    # Extracts last four letters in file name for file_suffix.
    file_suffix = old_name[-4:]
    # Assembles new name string.
    episode_number_full = ('S' + season + episode_string)
    new_name = (show_name + " " + episode_number_full + file_suffix)
    # Renames episode file.
    src = (file_path + old_name)
    dst = (file_path + new_name)
    os.rename(src, dst)
    time.sleep(.3)

    # Write to output file.
    f = open((file_path + 'changelog.txt'), 'a')
    line = old_name + ' was changed to ' + new_name
    f.write(f'{line}\n')
    f.close()
