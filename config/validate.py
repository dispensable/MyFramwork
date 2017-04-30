# _*_coding:utf_8 _*_

from schema import Schema, Use, Or, Optional, SchemaUnexpectedTypeError


def validate_param(params):
    """ transefer ['name=value', 'name=value' ...] to a dict """
    if not isinstance(params, list):
        raise SchemaUnexpectedTypeError(list)

    result = {}
    for p in params:
        p.strip()
        p.lstrip()
        name, value = p.split('=')
        result[name] = value
    return result

schema = Schema(
    {
        'bind': str,
        'conf': str,
        'debug': bool,
        'help': bool,
        Optional('param'): Or([], validate_param),
        Optional('plugin'): [str],
        'reload': bool,
        'server': str,
        'version': bool,
        'reloader': str,
        'package.module:app': str
    },
    ignore_extra_keys=True
)

