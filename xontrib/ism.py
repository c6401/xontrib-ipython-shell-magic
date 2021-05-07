import re
import subprocess

from IPython.utils.text import SList


__all__ = (
    'ism_out',
    'ism_run',
)

expression_str = r'\!([^\(\[].*)'
expression = re.compile(expression_str)
assignment = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*' + expression_str)

def ism_out(command):
    print(subprocess.run(command, capture_output=True, shell=True, text=True).stdout)

def ism_run(command):
    return SList(subprocess.run(f'''{command}''', capture_output=True, shell=True, text=True).stdout.splitlines())

@events.on_transform_command
def ipypreproc(cmd, **kw):
    if matched := expression.match(cmd):
        cmd, = matched.groups()
        return f"ism_out(f'''{cmd}''')"
    elif matched := assignment.match(cmd):
        var, cmd = matched.groups()
        return f"{var} = ism_run(f'''{cmd}''')\n"
    else:
        return cmd
