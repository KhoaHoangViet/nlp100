import a_20
import re

def category_name(data):
    list_match = re.findall(r"\[\[(Category:)([^\]]*)\]\]", data, re.DEBUG)

    for match in list_match:
        print(match[1]) # the second element in group


if __name__ == "__main__":
    data = a_20.json_export()
    category_name(data)
