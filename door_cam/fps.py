import time

class FPS_Reporter:
    report_interval = 0     # Disable by default
    report_function = print
    report_format = "{loop_name}: {fps:.2f} FPS"

    def __init__(self, loop_name = "loop"):
        self.loop_name = loop_name

        # Initialise the stats
        self._report_ts = time.time()
        self._loops = 0

    def report(self):
        # Reporting (only if report_interval > 0)
        if self.report_interval <= 0:
            return

        ts_current = time.time()
        ts_diff = ts_current - self._report_ts
        if ts_diff > self.report_interval:
            fps = self._loops/ts_diff
            self.report_function(self.report_format.format(fps=fps, loop_name=self.loop_name))
            self._loops = 0
            self._report_ts = ts_current

        self._loops += 1
