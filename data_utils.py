import regex

# /!\ Modified from nlstruct so that lines starting with "-" are split (list items)
BASE_SENTENCE_REGEX = regex.compile("((?:\s*\n)+\s*|(?:(?<=[\w0-9]{2,}\.|[)]\.)\s+))(?=[[:upper:]]|•|[-]|\n)")


# Adapted from nlstruct (Perceval Wajsbürt)
def regex_sentencize(text, reg_split=BASE_SENTENCE_REGEX, balance_chars=()):  # balance_chars=('()', '[]')):
    begin = 0
    for match in reg_split.finditer(text):
        end = match.start()
        if all(text[begin:end].count(chars[0]) <= text[begin:end].count(chars[1]) for chars in balance_chars):
            if begin != end:
                yield text[begin:end].strip(), begin, end
            begin = match.end()
    if begin != len(text):
        sent = text[begin:].strip()
        if len(sent):
            yield text[begin:].strip(), begin, len(text)

        
def regex_sentencize_whitespace_remove(text, reg_split=BASE_SENTENCE_REGEX, balance_chars=()):  # balance_chars=('()', '[]')):
    begin = 0
    text = " ".join(text.split())
    
    for match in reg_split.finditer(text):
        end = match.start()
        if all(text[begin:end].count(chars[0]) <= text[begin:end].count(chars[1]) for chars in balance_chars):
            if begin != end:
                yield text[begin:end].strip(), begin, end
            begin = match.end()
    if begin != len(text):
        sent = text[begin:].strip()
        if len(sent):
            yield text[begin:].strip(), begin, len(text)

        
        
        
