# -*- coding: utf-8 -*-
u"""Campos do Django para o Brasil."""

from brazil_types.types import CNPJ
from brazil_types.types import CPF
from django.core.exceptions import ValidationError
from django.db import models


class CNPJField(models.Field):
    u"""Field para armazenar um CNPJ."""

    description = "CNPJ"

    def __init__(self, *args, **kwargs):
        u"""Inicializa os valores padrões."""
        kwargs['max_length'] = 14
        super(CNPJField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        u"""Retorna o tipo de dado do Django usado nesta classe."""
        return 'CharField'

    def from_db_value(self, value, expression, connection, context):
        u"""Converte o tipo do banco em uma instância de CNPJ."""
        if value is None or value == '':
            return None
        return CNPJ(value)

    def get_prep_value(self, value):
        u"""Converte o tipo do banco em uma instância de CNPJ."""
        if value is None or value == '':
            return None
        if not isinstance(value, CNPJ):
            value = CNPJ(value)
        if not value.valid:
            raise ValidationError('Invalid CNPJ: {0:f}'.format(value))
        return value.format('r')

    def to_python(self, value):
        u"""Converte value para uma instância de CNPJ."""
        if value is None:
            return value

        if isinstance(value, CNPJ):
            return value

        return CNPJ(value)


class CPFField(models.Field):
    u"""Field para armazenar um CPF."""

    description = "CPF"

    def __init__(self, *args, **kwargs):
        u"""Inicializa os valores padrões."""
        kwargs['max_length'] = 11
        super(CPFField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        u"""Retorna o tipo de dado do Django usado nesta classe."""
        return 'CharField'

    def from_db_value(self, value, expression, connection, context):
        u"""Converte o tipo do banco em uma instância de CPF."""
        if value is None or value == '':
            return None
        return CPF(value)

    def get_prep_value(self, value):
        u"""Converte o tipo do banco em uma instância de CPF."""
        if value is None or value == '':
            return None
        if not isinstance(value, CPF):
            value = CPF(value)
        if not value.valid:
            raise ValidationError('Invalid CPF: {0:f}'.format(value))
        return value.format('r')

    def to_python(self, value):
        u"""Converte value para uma instância de CNPJ."""
        if value is None:
            return value

        if isinstance(value, CPF):
            return value

        return CPF(value)
