# import unittest

import pytest
import os
import sys

sys.path.append(os.getcwd())

from page.page_login import PageLogin


def get_data():
    return [("13800001111", "123456"), ("13800001112", "123457")]


class TestLogin(object):
    def setup_class(self):
        self.page_login_test = PageLogin()

    def teardown_class(self):
        self.page_login_test.driver.quit()

    @pytest.mark.parametrize("phone,pwd", [("13800001111", "123456"), ("13800001112", "123457")])
    # @pytest.mark.parametrize("text", [("123",)])

    # @pytest.mark.parametrize("phone,pwd",[("13800001111", "123456"),("13811111111", "654321")])
    # @pytest.mark.parametrize("phone,pwd",get_data())
    def test_login_phone(self,phone,pwd):
        self.page_login_test.page_login(phone,pwd)

    # def test_login_phone(self,phone="13800001111",pwd="123456"):
    #     self.page_login_test.page_login(phone=phone,pwd=pwd)
