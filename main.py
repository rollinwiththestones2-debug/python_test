from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import data
import helpers
from pages.urban_routes_page import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.set_from(data.ADDRESS_FROM)
        page.set_to(data.ADDRESS_TO)

        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        page = UrbanRoutesPage(self.driver)
        page.click_call_taxi_button()
        page.select_supportive_tariff()

    def test_fill_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.set_phone_number(data.PHONE_NUMBER)
        page.click_next_button()

    def test_fill_card(self):
        page = UrbanRoutesPage(self.driver)
        page.click_payment_method_button()
        page.click_add_card_button()
        page.set_card_number(data.CARD_NUMBER)
        page.set_card_code(data.CARD_CODE)
        page.click_link_button()
        page.close_payment()

    def test_comment_for_driver(self):
        page = UrbanRoutesPage(self.driver)
        page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        page = UrbanRoutesPage(self.driver)
        page.toggle_blanket()

    def test_order_2_ice_creams(self):
        page = UrbanRoutesPage(self.driver)
        for _ in range(2):
            page.add_ice_cream()

    def test_car_search_model_appears(self):
        page = UrbanRoutesPage(self.driver)
        page.click_order_button()
