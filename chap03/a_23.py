import a_20
import re

def section_export(data):
    list_match = re.findall(r"(=+)([一-龠]+|[ぁ-ゖ]+|[ァ-ヶ]+)(=+)", data, re.DEBUG)
    
    for match in list_match:
        print("level: {}, name: {}".format(len(match[0]), match[1])) # the second element in group


if __name__ == "__main__":
    data = a_20.json_export()
    section_export(data)
