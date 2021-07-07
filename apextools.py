#!/usr/bin/env python
"""
Entry point of the CLI for Apex-Tools
"""
import soap.wsdl2apex
import soap.gentests
import click

@click.group('soap')
def cli():
    pass

@cli.command()
@click.option('-p', '--paths', 'paths', multiple=True)
def fix_classes(paths):
    print(paths)
    soap.wsdl2apex.fix_classes(paths)

@cli.command()
@click.option('-c', '--class', 'cls')
@click.option('-o', '--output', 'out')
def gen_tests(cls, out):
    soap.gentests.generate_tests(cls, out)

if __name__ == '__main__':
    cli()
