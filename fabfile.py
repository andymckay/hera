"""
Creating standalone Django apps is a PITA because you're not in a project, so
you don't have a settings.py file. I can never remember to define
DJANGO_SETTINGS_MODULE, so I run these commands which get the right env
automatically.
"""
import functools
import os

from fabric.api import local, env

ROOT = os.path.abspath(os.path.dirname(__file__))

os.environ['PYTHONPATH'] = os.pathsep.join([ROOT,
                                            os.path.join(ROOT, 'examples')])

env.hosts = ['localhost']

local = functools.partial(local, capture=False)

def test(pdb=False):
    local('nosetests')
