from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.phone_page import PhonePage
from pages.contacts_page import ContactsPage
from pages.chats_page.chats_page import ChatsPage
from pages.profile_page.profile_page import ProfilePage
from pages.settings_page import SettingsPage
from libs.data_generator import Generators
from data.credentials import Credentials




class BaseTest:

    def setup_method(self):

        self.generator = Generators()
        self.creds = Credentials()
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.home_tab = lambda driver=self.driver: HomePage(driver)
        self.phone_tab = lambda driver=self.driver: PhonePage(driver)
        self.contacts_tab = lambda driver=self.driver: ContactsPage(driver)
        self.chats_tab = lambda driver=self.driver: ChatsPage(driver)
        self.profile_tab = lambda driver=self.driver: ProfilePage(driver)
        self.settings_tab = lambda driver=self.driver: SettingsPage(driver)








