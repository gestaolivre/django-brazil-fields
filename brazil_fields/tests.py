# -*- coding: utf-8 -*-
u"""Testes unitários."""

from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase

from brazil_types.types import CNPJ
from brazil_types.types import CPF

from .fields import CNPJField
from .fields import CPFField


class CNPJModel(models.Model):
    u"""Modelo usado para testes."""

    cnpj = CNPJField()
    null_cnpj = CNPJField(null=True)
    default_cnpj = CNPJField(default=CNPJ('58414462000135'))


class CPFModel(models.Model):
    u"""Modelo usado para testes."""

    cpf = CPFField()
    null_cpf = CPFField(null=True)
    default_cpf = CPFField(default=CPF('42326244737'))


class CNPJFieldTest(TestCase):
    u"""CNPJ Tests."""

    cnpj_model = CNPJModel

    def test_cnpj_field_create(self):
        u"""Teste de persistência do CNPJ."""
        cnpj_obj = CNPJ('36635377000164')

        obj = self.cnpj_model.objects.create(cnpj=cnpj_obj)
        new_obj = self.cnpj_model.objects.get(id=obj.id)

        self.assertEqual(new_obj.cnpj, cnpj_obj)

    def test_cnpj_field_null_create(self):
        u"""Teste de persistência do CNPJ."""
        cnpj_obj = CNPJ('88056061000111')

        obj = self.cnpj_model.objects.create(cnpj=cnpj_obj)
        new_obj = self.cnpj_model.objects.get(id=obj.id)

        self.assertIsNone(new_obj.null_cnpj)

    def test_cnpj_field_default_create(self):
        u"""Teste de persistência do CNPJ."""
        cnpj_obj = CNPJ('24508921000128')

        obj = self.cnpj_model.objects.create(cnpj=cnpj_obj)
        new_obj = self.cnpj_model.objects.get(id=obj.id)

        self.assertEqual(new_obj.default_cnpj, CNPJ('58414462000135'))

    def test_cnpj_field_invalid_cnpj(self):
        u"""Teste de persistência do CNPJ."""
        cnpj_obj = CNPJ('99908921000128')

        with self.assertRaises(ValidationError):
            self.cnpj_model.objects.create(cnpj=cnpj_obj)

    def test_cnpj_field_query(self):
        u"""Teste de persistência do CNPJ."""
        cnpj_obj = CNPJ('24508921000128')

        self.cnpj_model.objects.create(cnpj=cnpj_obj)
        new_obj = self.cnpj_model.objects.filter(cnpj=cnpj_obj).first()

        self.assertEqual(new_obj.cnpj, cnpj_obj)

    def test_cnpj_field_query_by_raiz(self):
        u"""Teste de persistência do CNPJ."""
        cnpj_obj = CNPJ('05255236000192')

        self.cnpj_model.objects.create(cnpj=cnpj_obj)
        new_obj = self.cnpj_model.objects.filter(cnpj__startswith=cnpj_obj.raiz).first()

        self.assertEqual(new_obj.cnpj, cnpj_obj)


class CPFFieldTest(TestCase):
    u"""Testes do CPFField."""

    cpf_model = CPFModel

    def test_cpf_field_create(self):
        u"""Teste de persistência do CPF."""
        cpf_obj = CPF('06936625657')

        obj = self.cpf_model.objects.create(cpf=cpf_obj)
        new_obj = self.cpf_model.objects.get(id=obj.id)

        self.assertEqual(new_obj.cpf, cpf_obj)

    def test_cpf_field_null_create(self):
        u"""Teste de persistência do CPF."""
        cpf_obj = CPF('61140532731')

        obj = self.cpf_model.objects.create(cpf=cpf_obj)
        new_obj = self.cpf_model.objects.get(id=obj.id)

        self.assertIsNone(new_obj.null_cpf)

    def test_cpf_field_default_create(self):
        u"""Teste de persistência do CPF."""
        cpf_obj = CPF('40140874178')

        obj = self.cpf_model.objects.create(cpf=cpf_obj)
        new_obj = self.cpf_model.objects.get(id=obj.id)

        self.assertEqual(new_obj.default_cpf, CPF('42326244737'))

    def test_cpf_field_invalid_cpf(self):
        u"""Teste de persistência do CPF."""
        cpf_obj = CPF('99944882835')

        with self.assertRaises(ValidationError):
            self.cpf_model.objects.create(cpf=cpf_obj)

    def test_cpf_field_query(self):
        u"""Teste de persistência do CPF."""
        cpf_obj = CPF('88710388516')

        self.cpf_model.objects.create(cpf=cpf_obj)
        new_obj = self.cpf_model.objects.filter(cpf=cpf_obj).first()

        self.assertEqual(new_obj.cpf, cpf_obj)
