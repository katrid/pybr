import unicodedata


def remover_acentos(s):
    return unicodedata.normalize('NFD', s).encode('ascii', 'ignore')
