import re
"""
04. 元素記号Permalink
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also 
Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 
9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）
を作成せよ．
"""

def permalink(str):
    words = list(map(lambda x: re.sub(r"\W+", "", x), str.split(" ")))
    first_char_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19] 
    result = {}
    for idx, word in enumerate(words):
        if idx+1 in first_char_positions:
            extracted_word = word[0]
        else:
            extracted_word = word[:2]
        result[extracted_word] = idx+1
    return result


if __name__ == "__main__":
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    print(permalink(str))