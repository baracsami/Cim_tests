import logging

# Needed for aetest script
from ats import aetest

# Get your logger for your script
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class TestcaseOne(aetest.Testcase):
    # First test section
    @aetest.test
    def log_output(self):
        """ Sample test section. Only print """
       assert 1 == 0


class TestcaseTwo(aetest.Testcase):
    # Second test section
    @aetest.test
    def log_output(self):
        """ Sample test section. Only print """
        log.info("pass")


class TestcaseFour(aetest.Testcase):
    # Fourth test section
    @aetest.test
    def log_output(self):
        """ Sample test section. Only print """
        log.info("pass")


if __name__ == '__main__':
    aetest.main()
