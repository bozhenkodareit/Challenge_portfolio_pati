from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_panel_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom')]"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_link_xpath = "//*[contains(@class, 'jss4')]"
    language_listbox_xpath = "//*[contains(@class, 'MuiSelect-nativeInput')]"
    sign_in_button_xpath = "//*[contains(@class, 'MuiTouchRipple-root')]"
    email = 'user01@getnada.com'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
