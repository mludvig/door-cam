import time

class FPS:
    def __init__(self, report_interval = 60, report_format = "{fps:.2f} frames/second", report_func = print):
        self.report_interval = report_interval
        self.report_format = report_format
        self.report_func = report_func

        # Initialise the stats
        self._timestamp = time.time()
        self._loops = 0

    def tick(self):
        ts_diff = time.time() - self._timestamp
        if ts_diff > self.report_interval:
            fps = self._loops/ts_diff
            self.report_func(self.report_format.format(fps=fps))
            self._loops = 0
            self._timestamp = time.time()
        else:
            self._loops += 1
