from .version import __version__ as version

foamMonHeader = """
8 8888888888       ,o888888o.           .8.                   ,8.       ,8.                   ,8.       ,8.           ,o888888o.     b.             8
8 8888          . 8888     `88.        .888.                 ,888.     ,888.                 ,888.     ,888.       . 8888     `88.   888o.          8
8 8888         ,8 8888       `8b      :88888.               .`8888.   .`8888.               .`8888.   .`8888.     ,8 8888       `8b  Y88888o.       8
8 8888         88 8888        `8b    . `88888.             ,8.`8888. ,8.`8888.             ,8.`8888. ,8.`8888.    88 8888        `8b .`Y888888o.    8
8 888888888888 88 8888         88   .8. `88888.           ,8'8.`8888,8^8.`8888.           ,8'8.`8888,8^8.`8888.   88 8888         88 8o. `Y888888o. 8
8 8888         88 8888         88  .8`8. `88888.         ,8' `8.`8888' `8.`8888.         ,8' `8.`8888' `8.`8888.  88 8888         88 8`Y8o. `Y88888o8
8 8888         88 8888        ,8P .8' `8. `88888.       ,8'   `8.`88'   `8.`8888.       ,8'   `8.`88'   `8.`8888. 88 8888        ,8P 8   `Y8o. `Y8888
8 8888         `8 8888       ,8P .8'   `8. `88888.     ,8'     `8.`'     `8.`8888.     ,8'     `8.`'     `8.`8888.`8 8888       ,8P  8      `Y8o. `Y8
8 8888          ` 8888     ,88' .888888888. `88888.   ,8'       `8        `8.`8888.   ,8'       `8        `8.`8888.` 8888     ,88'   8         `Y8o.`
8 8888             `8888888P'  .8'       `8. `88888. ,8'         `         `8.`8888. ,8'         `         `8.`8888.  `8888888P'     8            `Yo
                                                                                          by Gregor Olenik, go@hpsim.de, hpsim.de, Version: {}
""".format(version)
