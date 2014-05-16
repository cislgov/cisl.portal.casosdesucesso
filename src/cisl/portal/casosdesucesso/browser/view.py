# -*- coding: utf-8 -*-

from cisl.portal.casosdesucesso.interfaces import IExample
from five import grok

grok.templatedir('templates')


class HelloWorld (grok.View):
    """Browserview de exemplo Hello World
    """

    grok.context(IExample)
