import re
import subprocess

from IPython.utils.text import SList


__all__ = (
    'ish_out',
    'ish_run',
)

expression_str = r'\!([^\(\[].*)'
expression = re.compile(expression_str)
assignment = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*' + expression_str)

def ish_out(command):
    print(subprocess.run(command, capture_output=True, shell=True, text=True).stdout)

def ish_run(command):
    return SList(subprocess.run(f'''{command}''', capture_output=True, shell=True, text=True).stdout.splitlines())

@events.on_transform_command
def ipypreproc(cmd, **kw):
    if matched := expression.match(cmd):
        cmd, = matched.groups()
        return (
            f"try: ish_out(f''' {cmd} ''')\n"
            f"except NameError: ish_out(''' {cmd} ''')\n"
        )
    elif matched := assignment.match(cmd):
        var, cmd = matched.groups()
        return (
            f"try: {var} = ish_run(f''' {cmd} ''')\n"
            f"except NameError: {var} = ish_run(''' {cmd} ''')\n"
        )
    else:
        return cmd
