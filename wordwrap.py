def wordwrap(text, width):
    """
    If string surpasses the character width applies new line
    maintaining words together. Gonna frick up if a single
    word is longer than width

    :param text: a string of text
    :param width: character limit per line
    :type text: str
    :return: another string
    """

    t = ''
    text = text.split()
    length = len(text)
    for i in range(length):
        if len(t + text[i]) > width:
            t = t.rstrip()
            text = t + '\n' + wordwrap(' '.join(text[i:length]), width)
            break
        t += text[i] + ' '

    if isinstance(text, list) is True:
        text = ' '.join(text)

    return text
