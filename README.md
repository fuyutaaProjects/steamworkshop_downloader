# steamworkshop_downloader
 A tool to download mods/addons on the steamworkshop with only its name.

 1. Add the steamcmd.
 The steamcmd is not included in the repository, you'll need to download it and add it to the root of this repository.
 (It's where the main.py file is located.)

 2. Type in your addons names in the addons.txt file
 
 3. Run main.py (requires multiple libraries and it doesn't download itself!)
 
 4. Give the game's name when being asked for it.
 
 Simple as that!

 BEWARE: This is V1, without values checks and stuff, so if you input a value wrongly, it just crashes without warning.


REQUIREMENTS:
- bs4 (BeautifulSoup)
- subprocess (Popen)
- requests
-  os
