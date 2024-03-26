import inspect
import logging
import os
from datetime import date, datetime

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = None


class Baseclass:
    def __init__(self):
        self.driver = driver

    def pytest_addoption(parser):
        parser.addoption(
            "--browser_name", action="store", default="chrome"
        )

    @staticmethod
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        if logger.hasHandlers():
            logger.handlers.clear()
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                item._capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def wait_till_element_is_present(self, locator, timeout=10):
        flag = False
        log = self.get_logger(self)
        try:
            log.info(f"Waiting {timeout} seconds for element {list(locator.values())[0]} presence")
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((list(locator.keys())[0], list(locator.values())[0])))
            log.info(f"Element found")
            flag = True
        except Exception as e:
            log.error(
                f"Element {list(locator.values())[0]} not found after waiting {timeout} seconds")
        return flag

    """    def attach_screenshot_in_report(self):
            driver = logging.FileHandler.selenium_driver
            current_date_time = str(f'({(date.today().strftime("%d %b"))} {(datetime.now().strftime("%H_%M_%S"))})')
            screenshot_path = os.path.join(os.path.abspath(__file__ + '/../../'),
                                           f"Failed_Screenshots/{current_date_time}.png")
            driver.get_screenshot_as_file(screenshot_path)
            allure.attach.file(source=screenshot_path, attachment_type=allure.attachment_type.PNG, name="Screenshot")"""

    # def _capture_screenshot(self, name):
    # driver.get_screenshot_as_file(name)
