# -*- coding: utf-8 -*-

from cisl.portal.casosdesucesso import _
from zope.interface import Interface


class IBrowserLayer(Interface):
    """Layer especifico para este add-on.

    Esta interface e referenciada em browserlayers.xml.

    Views e viewlets registrados para este layer serao exibidos
    apenas quando o produto estiver instalado.
    """


class IExample(Interface):
    """Interface de tipo de conteúdo."""
