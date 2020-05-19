import a_20
import re

def category_export(data):
    # list_match = re.findall(r"\[\[Category:.*?\]\]", data, re.DEBUG) # *? for non-greedy
    list_match = re.findall(r"\[\[Category:[^\]]*\]\]", data, re.DEBUG) #[^\[] for all characters except ]

    for match in list_match:
        print(match)


if __name__ == "__main__":
    data = a_20.json_export()
    category_export(data)
