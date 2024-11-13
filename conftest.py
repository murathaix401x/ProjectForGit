from base.base_test import BaseTest
import pytest
import os
import allure
from selenium import webdriver


def get_driver():
    if os.environ["BROWSER"] == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
        options.add_argument("--use-fake-ui-for-mediafiles-stream")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

    elif os.environ["BROWSER"] == "firefox":
        options = webdriver.FirefoxOptions()
        preferences = {
            "download.default_directory": os.path.join(os.getcwd(), "downloads"),
            "safebrowsing.enabled": False,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
        }
        options.add_experimental_option("prefs", preferences)
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--use-fake-ui-for-mediafiles-stream")
        driver = webdriver.Firefox(options=options)

    elif os.environ["BROWSER"] == "safari":
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
    return driver

@pytest.fixture(autouse=True)
def driver(request):
    driver = get_driver()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="Screen on failure",
            attachment_type=allure.attachment_type.PNG
        )

@pytest.fixture()
def add_users(request):
    user_count = request.param
    drivers = []
    for _ in range(user_count):
        driver = get_driver()
        drivers.append(driver)
    yield drivers
    for driver in drivers:
        driver.quit()



# @pytest.fixture(autouse=True, scope="session")
# def setup_environment_properties():
#     properties = {
#         "Stage": os.environ["STAGE"],
#         "Browser": os.environ["BROWSER"]
#     }
#     with open("allure-results/environment_properties", "w") as file:
#         for key, value in properties.items():
#             file.write(f"{key}={value}\n")