# steamworkshop_downloader
 A tool to download addons on the steamworkshop by giving only their names.
 It's like WorkshopDL (another GitHub repo) but lighter, without GUI, simplified.
 Instead of giving addon's link and workshop's link, you only have to type the addons in the addons.txt file, and give the game's name when the script asks you (once)

STEPS:
 1. Add the steamcmd.
 The steamcmd is not included in the repository, you'll need to download it and add it to the root of this repository.
 (It's where the main.py file is located.)

 2. Type in your addons names in the addons.txt file
 
 3. Run main.py (requires multiple libraries and it doesn't download itself!)
 
 4. Give the game's name when being asked for it.
 
 Simple as that!

 **BEWARE: This is V1, without values checks and stuff, so if you input a value wrongly, it just crashes without warning.**


REQUIREMENTS:
- bs4 (BeautifulSoup)
- requests
- subprocess (Popen) (Built-in python)
-  os (Built-in python)

If you don't know how to download the required libs or start the main.py with python3:
- Open a cmd
- type in the following commands:
```
pip install beautifulsoup4
pip install requests
```

To start the main.py file:
```
python3 main.py
```
(Requires being under the same directory of the project)
