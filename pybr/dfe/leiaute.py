import sys
import re
from decimal import Decimal
from typing import List, Dict, Union
from lxml import etree


class Campo:
    ref = None
    tipo: str = None
    ocorrencias: tuple = None
    tam: tuple = None
    ele: str = None
    campo: str = None
    pai: str = None
    default = None
    descricao = None
    obs: str = None
    nivel: int = None
    regex: str = None
    dominio: str = None
    formato: str = None
    _is_list = False
    _min = _max = 0
    _required = False

    def __init__(
            self, ref=None, tipo: str=None, ocorrencias: Union[tuple, int]=None, tam=None, ele: str=None,
            campo: str=None, pai: str=None, default=None, descricao=None, nivel=None, regex=None, obs=None,
            dominio=None, formato=None,
    ):
        if ref is not None:
            self.ref = ref
        if tipo is not None:
            self.tipo = tipo
        if ocorrencias is not None:
            self.ocorrencias = ocorrencias
        if tam is not None:
            self.tam = tam
        if ele is not None:
            self.ele = ele
        if campo is not None:
            self.campo = campo
        if pai is not None:
            self.pai = pai
        if default is not None:
            self.default = default
        if descricao is not None:
            self.descricao = descricao
        if nivel is not None:
            self.nivel = nivel
        if regex is not None:
            self.regex = regex
        if obs is not None:
            self.obs = obs
        if dominio is not None:
            self.dominio = dominio
        if formato is not None:
            self.formato = formato

        min_v = max_v = None
        if isinstance(self.ocorrencias, tuple):
            min_v, max_v = self.ocorrencias
            if max_v == 'N' or max_v == 'n' or max_v == -1:
                max_v = sys.maxsize
        elif self.ocorrencias == 1:
            min_v = max_v = 1
        self._min = min_v
        self._max = max_v
        if self._min:
            self._required = True

    def __set_name__(self, owner, name):
        if not self.campo:
            self.campo = name
        if not owner._fields:
            owner._fields = {}
        owner._fields[self.campo] = self

    def _get_prep_value(self, value):
        return value

    def _render(self, parent: etree.Element, value):
        raise NotImplementedError

    def _validate(self, value, raise_error=True):
        errors = []

        # Validar pelas ocorrências
        if self._required and not value and value != 0:
            errors.append('(%s) - A tag "%s" é obrigatória.' % (self.ref, self.campo))
        elif self._min != self._max:
            min_v, max_v = self._min, self._max
            if value is None:
                value = []
            elif not isinstance(value, list):
                value = [value]
            count = len(value)
            if count > max_v or count < min_v:
                errors.append('(%s) - A tag "%s" deve ser informada entre %s e %s vezes.' % (self.ref, self.campo, min_v, max_v))

        elif isinstance(self.ocorrencias, int):
            required = True
            if not value:
                errors.append('(%s) - A tag "%s" é obrigatória.' % (self.ref, self.campo))

        # Validar pelo tamanho
        if isinstance(self.tam, tuple) and not errors:
            if value is None:
                value = ''
            else:
                value = str(value)
            min_v, max_v = self.tam
            count = len(value)
            if count > max_v or count < min_v:
                errors.append('(%s) - Valor informado inválido para a tag "%s", é necessário informar entre %s e %s caracteres' % (self.ref, self.campo, min_v, max_v))

        # Validar pelo tipo
        if self.tipo == 'N':
            pass

        return errors

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._values.get(self.campo)

    def __set__(self, instance, value):
        instance._values[self.campo] = self._get_prep_value(value)


class Atributo(Campo):
    ele = 'A'

    def _render(self, parent: etree.Element, value):
        if isinstance(value, float):
            value = '%.2f' % value
        parent.attrib[self.campo] = value

    def _get_prep_value(self, value):
        if self.tam == '1-2v2':
            return float(value)
        return value


class Elemento(Campo):
    _fields: Dict = None
    ele = 'E'

    def _render(self, parent: etree.Element, value=None):
        el = etree.Element(self.campo)
        if value is not None:
            if self.tipo == 'N':
                if isinstance(self.tam, tuple) and self.tam[1] < self.tam[0]:
                    value = ('%%.%df' % self.tam[1]) % value
                elif isinstance(self.tam, int):
                    value = int(value)
                if self.formato:
                    value = self.formato % value
            elif self.tipo == 'D':
                if self.formato:
                    value = value.strftime(self.formato)
                elif self.tam == 10:
                    value = value.strftime('%Y-%m-%d')
            value = str(value).strip()
            if self.tipo == 'CDATA':
                value = etree.CDATA(value)
            el.text = value
        has_value = bool(value)
        if self._fields:
            for field in self._fields.values():
                if field._is_list:
                    vals = getattr(self, field.campo, None)
                    if vals:
                        for val in vals:
                            val._render(el)
                else:
                    val = self._values.get(field.campo)
                    if isinstance(val, Grupo):
                        val._render(el)
                    elif (val is not None or (isinstance(val, list) and val)) and field.campo in self._values:
                        field._render(el, val)
            has_value = bool(len(el))
        if parent is not None and has_value:
            parent.append(el)
        return el

    def _get_prep_value(self, value):
        if value is not None:
            if isinstance(value, str) and self.regex:
                value = ''.join(re.findall(self.regex, value))
            if self.tipo == 'N':
                if isinstance(self.tam, tuple):
                    return Decimal(value)
                return int(value)
        return value

    def _read_attrs(self, node):
        for k in node.attrib:
            if k in self._fields:
                setattr(self, k, node.attrib[k])

    def _read_xml(self, node: etree.Element, parent: Atributo):
        if parent is not None and node.text:
            val = self._get_prep_value(node.text)
            setattr(parent, self.campo, val)
        self._read_attrs(node)


class TipoGrupo(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        new_cls._fields = {}
        new_cls.campo = name
        __attrs__ = attrs.get('__attrs__')
        if __attrs__:
            if 'campo' in __attrs__:
                new_cls.campo = __attrs__['campo']
            for k, v in __attrs__.items():
                setattr(new_cls, k, v)

        for k, v in attrs.items():
            if isinstance(v, Campo):
                new_cls._fields[v.campo or k] = v
            elif isinstance(v, TipoGrupo):
                v = v()
                new_cls._fields[v.campo or k] = v
                setattr(new_cls, k, v)

        return new_cls


class Grupo(Elemento, metaclass=TipoGrupo):
    xmlns = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.default is None:
            if self._min is not None:
                if self._max > 1:
                    self._is_list = True
                    self.default = ColecaoElemento(self)
                if self._min is None or self._max == 1:
                    self.default = self.__class__
        self._values = {}
        if not self.campo:
            nm = self.__class__.__name__
            self.campo = nm[0].lower() + nm[1:]
        self._children: List[Elemento] = []
        if not self.ocorrencias or self._max == 1:
            # iniciar uma nova instancia
            for field in self._fields.values():
                default = field.default
                if callable(default):
                    default = default()
                setattr(self, field.campo, default)

    # def append(self, item):
    #     self._children.append(item)
    #     return item

    def _load(self, obj, parent=None):
        """Carregar dados do documento a partir de um dict"""
        for k, v in obj.items():
            if v is None:
                continue
            if k == 'CPFCNPJ' or k == 'CNPJCPF':
                if len(v) == 11:
                    k = 'CPF'
                elif len(v) == 14:
                    k = 'CNPJ'
            field = self._fields.get(k)
            if field is not None:
                if isinstance(field, Grupo):
                    val = self._values[field.campo]
                    if isinstance(v, list):
                        for obj in v:
                            val.add()._load(obj)
                    else:
                        val._load(v)
                else:
                    self._values[k] = field._get_prep_value(v)

    def __len__(self):
        return len(self._children)

    def _render(self, parent: etree.Element, value=None):
        node = super()._render(parent, value)
        if self.xmlns:
            node.attrib['xmlns'] = self.xmlns
        return node

    def _to_xml(self, parent: etree.Element=None) -> etree.Element:
        if self._children:
            for child in self._children:
                child._render(parent)
        else:
            return self._render(parent)

    def prepare(self, dfe):
        pass

    def find_field(self, name):
        for f in self._fields.values():
            if f.campo == name:
                return f

    def _read_xml(self, node: etree.Element, parent=None):
        if parent is not None:
            val = parent._values.get(self.campo)
            if self._is_list:
                val.add()._read_xml(node)
            elif val is not None:
                val._read_xml(node)
        else:
            self._read_attrs(node)
            for child in node:
                tag = child.tag.split('}', 1)[-1]
                if tag in self._fields:
                    self._fields[tag]._read_xml(child, self)

    def _validate(self, value=None, raise_error=False):
        errors = {}
        if isinstance(value, list):
            return super()._validate(value)
        elif value is None:
            for f in self._fields.values():
                error = f._validate(self._values.get(f.campo))
                if error:
                    errors[f.campo] = error
        return errors

    def __call__(self, *args, **kwargs):
        return self.__class__(ocorrencias=1)  # forçar o número de ocorrencias para 1

    def __iter__(self):
        for k, v in self._values.items():
            if v is None:
                continue
            if isinstance(v, Grupo):
                v = dict(v)
            elif isinstance(v, ColecaoElemento):
                v = [dict(obj) for obj in v]
            yield k, v

    def __getitem__(self, item):
        return self._values[item]


class ID(Atributo):
    pass


class CPFCNPJ(Elemento):
    pass


class Documento(Grupo):
    pass


class Xml(Elemento):
    _xml: str = None

    def _read_xml(self, node: etree.Element, parent: Atributo):
        self._xml = etree.tostring(node)
        parent._values[self.campo] = self._xml

    def _render(self, parent: etree.Element, value=None):
        parent.append(etree.fromstring(value))


class Signature(Xml):
    campo = 'Signature'


class ColecaoElemento(list):
    def __init__(self, tag):
        super().__init__()
        self.tag = tag

    def add(self):
        item = self.tag()
        self.append(item)
        return item


# Aliases

def G(**kwargs):
    return type('DFe', (Grupo,), {'__attrs__': kwargs})


A = Atributo
E = Elemento
CG = G
CE = Elemento


def CampoCNPJ(**kwargs):
    return Elemento(formato='%014d', **kwargs)


def CampoCPF(**kwargs):
    return Elemento(formato='%011d', **kwargs)
