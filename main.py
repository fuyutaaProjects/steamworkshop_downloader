from bs4 import BeautifulSoup
import requests
from subprocess import Popen
import os

# By fuyutaa

# I tried to subprocess a cmd and do inputs in, but it wasn't possible because I could not type a new cd 
# command whiel the previous didn't ended, and opening the steamcmd was a command, so it could not type new commands and got stuck that way.
# If you know how I can pass my commands to the steamcmd without using +runscript, please learn me. I NEED this knowledge ^^


def get_url(search):
    url = 'https://www.google.com/search' # search engine used. Can be changed.

    headers = {
        'Accept' : '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }

    parameters = {'q': search} # parameters required by the search engine

    content = requests.get(url, headers = headers, params = parameters).text # getting the page with requests
    soup = BeautifulSoup(content, 'html.parser') # parsing the html content

    search = soup.find(id = 'search')
    first_link = search.find('a') # retrieves all info on the first link, including HTML tags on the page

    return first_link['href'] # retrives the URL by accessing the value contained in the tag "href".


def get_game_workshop_id(game_name):
    game_workshop_page = get_url(game_name) # gets the URL of the workshop page. Example: https://store.steampowered.com/app/294100/RimWorld/
    splitted_url = game_workshop_page.split("/") # Returns the URL splitted: ['https:', '', 'store.steampowered.com', 'app', '294100', 'RimWorld', '']
    return splitted_url[4] # gets the workshop id located at index 4 when url is splitted

def get_addon_id(addon_name):
    game_workshop_page = get_url(addon_name) # gets the URL of the addon on the workshop page
    splitted_url = game_workshop_page.split("id=") # Returns the URL splitted by the id= in the link (example link: https://steamcommunity.com/workshop/filedetails/?id=1386412863)
    return splitted_url[1] # gets the addon id located at index 1 (url is splitted in two)


def __main__():
    # the steamcmd_commands file is given to the steamcmd.exe subprocess and contains commands to pass.
    # We're firstly removing (if there was) the previous file to prevent conflict with the new commands file.
    os.remove("steamcmd_commands.txt")

    print("--------------------------------------------------------------")
    print("The mods names must be placed in the txt mods.txt, located under the same directory of main.py")
    print("If you are not sure about the formatting, there is a sample formatted file called mods_example_file.txt to show you how the file must look like.")
    print("One mod per line.")
    print("--------------------------------------------------------------")

    game_name = input("Please enter the game's name.\n")
    game_workshop_id = get_game_workshop_id(game_name) # Getting the workshop ID of the game (the steamcmd needs addon id + workshop id to download an addon)

    steamcmd_commands = open("steamcmd_commands.txt", "w") # creates new a new file containing commands for steamcmd
    addons_txt = open("addons.txt", "r")
    addons_txt_lines = addons_txt.readlines()

    steamcmd_commands.write("login anonymous\n") # logins to the steam network to download addons. Some addons require login with permissions, most don't (you can use anonymous)

    for addon_name in addons_txt_lines:
        addon_id = get_addon_id(addon_name) # getting the addon id (the steamcmd needs addon id + workshop id to download an addon)
        addon_download_command = "workshop_download_item " + game_workshop_id + " " + addon_id
        steamcmd_commands.write("{}\n".format(addon_download_command)) # writes in the txt file the addons download commands one by one.

    steamcmd_commands.write("quit\n") # exiting properly the steamcmd

    Popen("cmd /k cd steamcmd & steamcmd.exe +runscript ../steamcmd_commands.txt") 
    # Start cmd as child program, and then opens the steamcmd, giving the commands with +runscript [file.txt]


__main__()

