import sys
from unittest import TestCase

from redrover.plugin import RedRoverFilter


class FmtTracebackTest(TestCase):

  @classmethod
  def setUpClass(cls):
    cls.red_rover_filter = RedRoverFilter()

  def test_format_remove(self):
    """It should remove any instance of 'redrover/case.py'."""
    try:
      assert 'redrover/case.py' in '***'
    except:
      pass
    tb = sys.exc_info()[2]
    formatted_traceback = self.red_rover_filter._fmt_traceback(tb)
    self.assertNotIn('redrover/case.py', formatted_traceback)

  def test_format_preserve(self):
    """It should keep everything else."""
    try:
      assert 'blueberry/case.py' in '***'
    except:
      pass
    tb = sys.exc_info()[2]
    formatted_traceback = self.red_rover_filter._fmt_traceback(tb)
    self.assertIn('blueberry/case.py', formatted_traceback)
