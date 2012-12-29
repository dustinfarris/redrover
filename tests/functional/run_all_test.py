import os
import shlex, subprocess

from django.test import TestCase


class RunAllTest(TestCase):

  @classmethod
  def setUpClass(cls):
    cls.command = ("python {example_dir}/manage.py test " +
               "--where={example_dir}").format(
                 example_dir=os.environ['EXAMPLE_DIR'])
    args = shlex.split(cls.command)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cls.out, cls.err = p.communicate()

  def test_output(self):
    """Tests should run and return proper output to stdout/stderr."""

    self.assertIn(self.command, self.err)
