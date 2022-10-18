def textOmit(text, maxLength):
    split_text = text[:maxLength]
    omit_text = split_text + "..."
    return omit_text

def textCountChecker(text, countMax):
    if len(text) <= countMax: return text
    return textOmit(text, countMax)

def textIndention(text , lineHeight):
    split_text = [text[x:x+lineHeight] for x in range(0, len(text), lineHeight)]
    mergeText = "\n".join(split_text)
    return mergeText

