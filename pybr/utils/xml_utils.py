from xml.sax.saxutils import escape
from .text import remover_acentos


def tag(t: str, *children, **kwargs):
    s = '<' + t
    for k, v in kwargs.items():
        if v is None:
            v = ''
        s += ' %s="%s"' % (k, escape(v))
    if children:
        s += '>'
        s += ''.join(children)
        s += '</' + t + '>'
    else:
        s += '/>'
    return s


def filtrar_texto_xml(texto: str, retira_acentos: bool = False, retira_espacos: bool = False, quebra_linha: str = None) -> str:
    if retira_acentos:
        texto = remover_acentos(texto)

    texto = escape(texto)

    if retira_espacos:
        texto = texto.replace(' ', '')
    if quebra_linha is not None:
        texto = texto.replace('\n', quebra_linha)
    return texto.strip()

