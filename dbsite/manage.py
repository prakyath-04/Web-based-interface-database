#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import cx_Oracle
import sys
import os

try:
    if sys.platform.startswith("darwin"):
        lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
                               "instantclient_19_8")
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    elif sys.platform.startswith("win32"):
        lib_dir=r"C:\oracle\instantclient_19_9"
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Whoops!")
    print(err);
    sys.exit(1);

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
