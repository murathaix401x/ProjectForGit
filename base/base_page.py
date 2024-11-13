import allure
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.support import expected_conditions as EC
from  helpers.ui_helper import UIHelper


class BasePage(UIHelper, metaclass=MetaLocator):

    _HOME_TAB_LOCATOR = "//a[@aria-label='Home']"
    _PHONE_TAB_LOCATOR = "//a[@aria-label='Phone']"
    _CONTACTS_TAB_LOCATOR = "//a[@aria-label='Contacts']"
    _CHATS_TAB_LOCATOR = "//a[@aria-label='Messages']"
    _PROFILE_TAB_LOCATOR = "//a[@aria-label='Profile']"
    _SETTINGS_TAB_LOCATOR = "//a[@aria-label='Settings']"
    _SETTINGS_POPUP_LOCATOR = "//section[@role='dialog']"
    _AUDIO_TAB_LOCATOR = "//button[contains(@class, 'SettingsModal_tab')][1]"
    _VIDEO_TAB_LOCATOR = "//button[contains(@class, 'SettingsModal_tab')][2]"
    _CLOSE_SETTINGS_POPUP_BUTTON = "//button[contains(@class, 'Close')]"
    _LOGOUT_TAB_LOCATOR = "//button[contains(@class, 'logout')]"


    _PERSONAS_SELECTOR = "//div[contains(@class, 'PersonasSelector')]"
    _SELECTED_PERSONAS_NAME = "//p[contains(@class, 'PersonasSelector_name')]"
    _SELECTED_PERSONAS_NUMBER = "//div[contains(@class, 'PersonasSelector')]//div[contains(@class, 'PhoneWithFlag')]"







    @allure.step("Switch to second window")
    def switch_to_second_window(self):
        window_1 = self.driver.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        all_windows = self.driver.window_handles
        window_2 = [window for window in all_windows if window != window_1][0]
        self.driver.switch_to.window(window_2)

    @allure.step("Switch to main window")
    def switch_to_main_window(self):
        all_windows = self.driver.window_handles
        window_1 = all_windows[0]
        self.driver.switch_to.window(window_1)

    @allure.step("Open Home tab")
    def go_to_home_tab(self):
        self.find(self._HOME_TAB_LOCATOR).click()

    @allure.step("Open Phone tab")
    def go_to_phone_tab(self):
        self.find(self._PHONE_TAB_LOCATOR).click()

    @allure.step("Open Contacts tab")
    def go_to_contacts_tab(self):
        self.find(self._CONTACTS_TAB_LOCATOR).click()

    @allure.step("Open Chats tab")
    def go_to_chats_tab(self):
        self.find(self._CHATS_TAB_LOCATOR).click()

    @allure.step("Open Profile tab")
    def go_to_profile_tab(self):
        self.find(self._PROFILE_TAB_LOCATOR).click()

    @allure.step("Open Settings popup")
    def open_settings_popup(self):
        self.find(self._SETTINGS_TAB_LOCATOR).click()
        self.find(self._SETTINGS_POPUP_LOCATOR)

    @allure.step("Open Video tab")
    def open_video_tab(self):
        self.find(self._VIDEO_TAB_LOCATOR).click()

    @allure.step("Open Audio tab")
    def open_audio_tab(self):
        self.find(self._AUDIO_TAB_LOCATOR).click()

    @allure.step("Open Audio tab")
    def close_settings_popup(self):
        self.find(self._CLOSE_SETTINGS_POPUP_BUTTON).click()

    @allure.step("Logout")
    def logout(self):
        self.find(self._LOGOUT_TAB_LOCATOR).click()