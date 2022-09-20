from lib2to3.refactor import get_all_fix_names
from bs4 import BeautifulSoup
import requests
from subprocess import Popen, PIPE

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


def main():
    print("--------------------------------------------------------------")
    print("The mods names must be placed in the txt mods.txt, located under the same directory of main.py")
    print("If you are not sure about the formatting, there is a sample formatted file called mods_example_file.txt to show you how the file must look like.")
    print("One mod per line.")
    print("--------------------------------------------------------------")
    game_name = input("Please enter the game's name.\n")
    game_workshop_id = get_game_workshop_id(game_name)
    addons_txt = open("addons.txt", "r")
    addons_txt_lines = addons_txt.readlines()
    for addon_name in addons_txt_lines:
        addon_id = get_addon_id(addon_name)
        print(addon_id)
        addon_download_command = "workshop_download_item " + game_workshop_id + " " + addon_id
        print(addon_download_command) 

        # OPEN STEAMCMD.EXE IN CMD
        steamcmd_subprocess = Popen(r".\steamcmd\steamcmd.exe", stdin=PIPE)
        steamcmd_subprocess.communicate("login anonymous")
        steamcmd_subprocess.communicate(addon_download_command)


        # TYPE: login anonymous

        # PASS COMMANDS TO STEAMCMD


main()

