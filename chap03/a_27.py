import a_20
import re
from pprint import pprint 

def regular_info_export(data):
    result = {}
    
    regular_info_pattern = re.compile(r"^\{\{基礎情報 国$(.*?)^\}\}$", re.MULTILINE + re.DOTALL)
    regular_info = regular_info_pattern.findall(data)
    regular_info = regular_info[0]

    regular_info = re.sub(r"'{2,5}", "", regular_info)

    regular_info = re.sub(r"\[\[([^\|\]]+)\]\]", r"\1", regular_info) # [[記事名]] -> 記事名
    regular_info = re.sub(r"\[\[([^\|\]#]+)\|([^\]]+)\]\]", r"\1", regular_info) # [[記事名|表示文字]] -> 記事名
    regular_info = re.sub(r"\[\[([^\|\]#]+)#([^\]]+)\]\]", r"\1", regular_info) # [[記事名#節名|表示文字]] -> 記事名
    
    detail_pattern = re.compile(r"^\|(.*?)(\s*=\s*)(.*?)$", re.MULTILINE)
    result_detail = detail_pattern.findall(regular_info)

    for detail in result_detail:
        result[detail[0]] = detail[2]
    return result

if __name__ == "__main__":
    data = a_20.json_export()
    pprint(regular_info_export(data))
