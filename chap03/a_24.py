import a_20
import re

def media_file_export(data):
    list_match = re.findall(r"\[\[(ファイル:)([^[\||\]]*)\|", data, re.DEBUG)
    
    for match in list_match:
        print("Media file: {}".format(match[1])) # the second element in group


if __name__ == "__main__":
    data = a_20.json_export()
    media_file_export(data)
