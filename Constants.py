#system constants, simple
TEXT_RESET = "\033[0m"
TEXT_RED = "\033[31m"
TEXT_GREEN = "\033[32m"
TEXT_YELLOW = "\033[33m"
TEXT_BLUE = "\033[34m"
TEXT_BOLD = "\033[1m"
TEXT_DIM = "\033[2m"
TEXT_MAGENTA = "\033[35m"
TEXT_CYAN = "\033[36m"

#system constants, compound
TEXT_BOLD_RED = TEXT_RED + TEXT_BOLD
TEXT_BOLD_BLUE = TEXT_BLUE + TEXT_BOLD

#program constants, large
recurring_printStatement = f"""
{TEXT_BOLD_BLUE}00{TEXT_RESET} : Objects      (b)
0{TEXT_BOLD_BLUE}1{TEXT_RESET} : Scenery      (b)
0{TEXT_BOLD_BLUE}2{TEXT_RESET} : Accessories  (c)
0{TEXT_BOLD_BLUE}3{TEXT_RESET} : Clothing     (c)
0{TEXT_BOLD_BLUE}4{TEXT_RESET} : Faces        (c)
0{TEXT_BOLD_BLUE}5{TEXT_RESET} : Expressions  (c)
0{TEXT_BOLD_BLUE}6{TEXT_RESET} : Posture      (c)
0{TEXT_BOLD_BLUE}7{TEXT_RESET} : Colours      (g)
0{TEXT_BOLD_BLUE}8{TEXT_RESET} : Uni-AS       (g)
0{TEXT_BOLD_BLUE}9{TEXT_RESET} : NV           (g)

{TEXT_BOLD_BLUE}1{TEXT_RESET}0 : 2 Objects    (b)
{TEXT_BOLD_BLUE}2{TEXT_RESET}0 : 3 Objects    (b)
start with '{TEXT_BOLD_RED}/{TEXT_RESET}' for R images

face: {TEXT_BOLD_BLUE}#{TEXT_RESET} {TEXT_BOLD_BLUE}E{TEXT_RESET}yes {TEXT_BOLD_BLUE}H{TEXT_RESET}air {TEXT_BOLD_BLUE}C{TEXT_RESET}olour {TEXT_BOLD_BLUE}S{TEXT_RESET}hape
posture wrt: {TEXT_BOLD_BLUE}#{TEXT_RESET} {TEXT_BOLD_BLUE}C{TEXT_RESET}amera {TEXT_BOLD_BLUE}H{TEXT_RESET}uman {TEXT_BOLD_BLUE}N{TEXT_RESET}ature    {TEXT_DIM}(Human-Camera Human-Human Human-Object/Scenery){TEXT_RESET}

{TEXT_BOLD_BLUE}30{TEXT_RESET} : Recheck
{TEXT_BOLD_BLUE}31{TEXT_RESET} : NonAS
{TEXT_BOLD_BLUE}32{TEXT_RESET} : Delete
{TEXT_BOLD_RED}33{TEXT_RESET} : Favourites
"""

folderAdressList = {

    #default
    '99' : r"D:\Ashen Silver\More\The Great Library",
    '99R' : r"D:\Ashen Silver\More\The Great Library R9",
    #default extended
    '30' : r"D:\Ashen Silver\More\ReCheck",
    '30R' : r"D:\Ashen Silver\More\ReCheck R",
    '31' : r"D:\Ashen Silver\More\NonAS",
    '31R' : r"D:\Ashen Silver\More\NonAS R9",
    '32' : r"D:\Ashen Silver\More\Del",
    '32R' : r"D:\Ashen Silver\More\Del",
    '33' : r"D:\Ashen Silver\More\Favourites",
    '33R' : r"D:\Ashen Silver\More\Favourites R9",

    #non r
    '00' : r"D:\Ashen Silver\1 b Objects",
    '01' : r"D:\Ashen Silver\1 b Scenery",
    '02' : r"D:\Ashen Silver\1 c Accessories",
    '03' : r"D:\Ashen Silver\1 c Clothing",
    '04' : r"D:\Ashen Silver\1 c Faces",
    '05' : r"D:\Ashen Silver\1 c Expressions",
    '06' : r"D:\Ashen Silver\1 c Posture",
    '07' : r"D:\Ashen Silver\1 g Colours",
    '08' : r"D:\Ashen Silver\1 g UniAS",
    '09' : r"D:\Ashen Silver\1 g NV",

    '10' : r"D:\Ashen Silver\2 b Objects",
    '11' : r"D:\Ashen Silver\2 b Scenery",
    '12' : r"D:\Ashen Silver\2 c Accessories",
    '13' : r"D:\Ashen Silver\2 c Clothing",
    '14' : r"D:\Ashen Silver\2 c Faces",
    '15' : r"D:\Ashen Silver\2 c Expressions",
    '16' : r"D:\Ashen Silver\2 c Posture",
    '17' : r"D:\Ashen Silver\2 g Colours",
    '18' : r"D:\Ashen Silver\2 g UniAS",
    '19' : r"D:\Ashen Silver\2 g NV",

    '20' : r"D:\Ashen Silver\3 b Objects",
    '21' : r"D:\Ashen Silver\3 b Scenery",
    '22' : r"D:\Ashen Silver\3 c Accessories",
    '23' : r"D:\Ashen Silver\3 c Clothing",
    '24' : r"D:\Ashen Silver\3 c Faces",
    '25' : r"D:\Ashen Silver\3 c Expressions",
    '26' : r"D:\Ashen Silver\3 c Posture",
    '27' : r"D:\Ashen Silver\3 g Colours",
    '28' : r"D:\Ashen Silver\3 g UniAS",
    '29' : r"D:\Ashen Silver\3 g NV",

    #r
    '00R' : r"D:\Ashen Silver\R9\1 b Objects",
    '01R' : r"D:\Ashen Silver\R9\1 b Scenery",
    '02R' : r"D:\Ashen Silver\R9\1 c Accessories",
    '03R' : r"D:\Ashen Silver\R9\1 c Clothing",
    '04R' : r"D:\Ashen Silver\R9\1 c Faces",
    '05R' : r"D:\Ashen Silver\R9\1 c Expressions",
    '06R' : r"D:\Ashen Silver\R9\1 c Posture",
    '07R' : r"D:\Ashen Silver\R9\1 g Colours",
    '08R' : r"D:\Ashen Silver\R9\1 g UniAS",
    '09R' : r"D:\Ashen Silver\R9\1 g NV",

    '10R' : r"D:\Ashen Silver\R9\2 b Objects",
    '11R' : r"D:\Ashen Silver\R9\2 b Scenery",
    '12R' : r"D:\Ashen Silver\R9\2 c Accessories",
    '13R' : r"D:\Ashen Silver\R9\2 c Clothing",
    '14R' : r"D:\Ashen Silver\R9\2 c Faces",
    '15R' : r"D:\Ashen Silver\R9\2 c Expressions",
    '16R' : r"D:\Ashen Silver\R9\2 c Posture",
    '17R' : r"D:\Ashen Silver\R9\2 g Colours",
    '18R' : r"D:\Ashen Silver\R9\2 g UniAS",
    '19R' : r"D:\Ashen Silver\R9\2 g NV",

    '20R' : r"D:\Ashen Silver\R9\3 b Objects",
    '21R' : r"D:\Ashen Silver\R9\3 b Scenery",
    '22R' : r"D:\Ashen Silver\R9\3 c Accessories",
    '23R' : r"D:\Ashen Silver\R9\3 c Clothing",
    '24R' : r"D:\Ashen Silver\R9\3 c Faces",
    '25R' : r"D:\Ashen Silver\R9\3 c Expressions",
    '26R' : r"D:\Ashen Silver\R9\3 c Posture",
    '27R' : r"D:\Ashen Silver\R9\3 g Colours",
    '28R' : r"D:\Ashen Silver\R9\3 g UniAS",
    '29R' : r"D:\Ashen Silver\R9\3 g NV"

}
