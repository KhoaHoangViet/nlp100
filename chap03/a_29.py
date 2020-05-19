import re
import requests
from pprint import pprint
import a_28
import a_20

def get_flag_url(result_dict):    
    filename = result_dict["国旗画像"]
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop" : "url",
        "titles": f"File:{filename}"
    }

    R = S.get(url=URL, params=PARAMS)
    result = R.text
    match = re.search(r'"url":"(.+?)"', result)
    return match.group(1)

if __name__ == "__main__":
    data = a_20.json_export()
    result_dict = a_28.remove_markups(data)
    pprint(get_flag_url(result_dict))