import os
import re

import termstyle
from rednose import RedNose


class RedRoverFilter(RedNose):
  """
  Suppress the last traceback entry since that will always be raised by
  redrover.

  """
  env_opt = 'NOSE_REDROVER'
  env_opt_color = 'NOSE_REDROVER_COLOR'
  score = 199

  def options(self, parser, env=os.environ):
    global REDNOSE_DEBUG
    rednose_on = bool(env.get(self.env_opt, False))
    rednose_color = env.get(self.env_opt_color, 'auto')
    REDNOSE_DEBUG = bool(env.get('REDNOSE_DEBUG', False))

    parser.add_option(
      "--redrover-rednose", action="store_true",
      default=rednose_on, dest="redrover_rednose",
      help="enable colour output (alternatively, set $%s=1)" % (self.env_opt,))
    parser.add_option(
      "--no-redrover-color", action="store_false",
      dest="redrover_rednose",
      help="disable colour output")
    parser.add_option(
      "--force-redrover-color", action="store_const",
      dest='redrover_rednose_color',
      default=rednose_color,
      const='force',
      help="force colour output when not using a TTY " +
        "(alternatively, set $%s=force)" % (self.env_opt_color,))
    parser.add_option(
      "--redrover-immediate", action="store_true",
      default=False,
      help="print errors and failures as they happen, as well as at the end")

  def configure(self, options, conf):
    if options.redrover_rednose:
      self.enabled = True
      termstyle_init = {
        'force': termstyle.enable,
        'off': termstyle.disable
      }.get(options.redrover_rednose_color, termstyle.auto)
      termstyle_init()

      self.immediate = options.immediate
      self.verbose = options.verbosity >= 2

  def _fmt_traceback(self, trace):
    """format a traceback"""
    ret = []
    ret.append(termstyle.default("   Traceback (most recent call last):"))
    current_trace = trace
    while current_trace is not None:
      line = self._file_line(current_trace)
      if line is not None and not re.search(r'redrover/\w+\.pyc?', line):
        ret.append(line)
      current_trace = current_trace.tb_next
    return '\n'.join(ret)
