# -*- coding: utf-8 -*-
u"""Instalation files for django-brazil-fields."""

from setuptools import setup
from setuptools.command.test import test as test_command
from brazil_fields import __version__


class TestCommand(test_command):
    user_options = []

    def initialize_options(self):
        u"""Initialize the test options."""
        test_command.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        u"""Finalize the test options."""
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        u"""Run tests."""
        from django.conf import settings
        settings.configure(
            DATABASES={'default': {'NAME': ':memory:', 'ENGINE': 'django.db.backends.sqlite3'}},
            INSTALLED_APPS=('brazil_fields',)
        )
        from django.core.management import call_command
        import django

        if django.VERSION[:2] >= (1, 7):
            django.setup()
        call_command('test', 'brazil_fields')


setup(
    name='django-brazil-fields',
    packages=['brazil_fields'],
    version=__version__,
    description='Biblioteca com os campos para os tipos de dados usados no Brasil.',
    long_description='Biblioteca com os campos para os tipos de dados usados no Brasil.',
    author='Gestão Livre',
    author_email='contato@gestaolivre.org',
    url='https://github.com/gestaolivre/django-brazil-fields',
    download_url='https://github.com/gestaolivre/django-brazil-fields/releases',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    keywords='django fields brazil types receita federal',
    install_requires=['Django >= 1.8', 'brazil-types'],
    tests_require=['Django >= 1.8', 'brazil-types'],
    cmdclass={'test': TestCommand},
)
