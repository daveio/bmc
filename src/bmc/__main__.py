# SPDX-FileCopyrightText: 2024-present Dave Williams <dave@dave.io>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from bmc.cli import bmc

    sys.exit(bmc())
