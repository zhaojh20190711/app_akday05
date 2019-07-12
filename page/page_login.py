import page
from base.base import BaseLogin


class PageLogin(BaseLogin):
    def page_input_phone(self, phone):
        self.base_input(page.page_phone, phone)

    def page_input_pwd(self, pwd):
        self.base_input(page.page_pwd, pwd)

    def page_click_login_btn(self):
        self.base_click(page.page_login_btn)

    # def page_login(self,phone,pwd):
    def page_login(self, phone, pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

#
# PageLogin().page_login()
