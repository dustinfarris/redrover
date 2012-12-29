import os

from django.conf import settings
from django.core import exceptions
from django.utils.importlib import import_module
from django_nose.plugin import DjangoSetUpPlugin, ResultPlugin, TestReorderer
from django_nose.runner import NoseTestSuiteRunner

import nose.core

from plugin import RedRoverFilter


def _get_plugins_from_settings():
  plugins = (list(getattr(settings, 'NOSE_PLUGINS', [])) +
             ['django_nose.plugin.TestReorderer',
              'redrover.plugin.RedRoverFilter'])

  for plug_path in plugins:
    try:
      dot = plug_path.rindex('.')
    except ValueError:
      raise exceptions.ImproperlyConfigured(
        "%s isn't a Nose plugin module" % plug_path)
    p_mod, p_classname = plug_path[:dot], plug_path[dot + 1:]

    try:
      mod = import_module(p_mod)
    except ImportError, e:
      raise exceptions.ImproperlyConfigured(
        'Error importing Nose plugin module %s: "%s"' % (p_mod, e))

    try:
      p_class = getattr(mod, p_classname)
    except AttributeError:
      raise exceptions.ImproperlyConfigured(
        'Nose plugin module "%s" does not define a "%s"' %
        (p_mod, p_classname))

    yield p_class()


class RedRoverRunner(NoseTestSuiteRunner):

  def __init__(self, *args, **kwargs):
    if 'NOSE_REDROVER' not in os.environ:
      os.environ['NOSE_REDROVER'] = '1'
    super(RedRoverRunner, self).__init__(*args, **kwargs)

  def run_suite(self, nose_argv):
    result_plugin = ResultPlugin()
    plugins_to_add = [DjangoSetUpPlugin(self),
                      result_plugin,
                      TestReorderer(),
                      RedRoverFilter()]

    for plugin in _get_plugins_from_settings():
        plugins_to_add.append(plugin)

    nose.core.TestProgram(argv=nose_argv, exit=False,
                          addplugins=plugins_to_add)
    return result_plugin.result
