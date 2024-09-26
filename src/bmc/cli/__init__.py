# SPDX-FileCopyrightText: 2024-present Dave Williams <dave@dave.io>
#
# SPDX-License-Identifier: MIT
import click

from bmc.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="bmc")
def bmc():
    click.echo("Hello world!")
