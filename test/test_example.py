import pytest
from selenium import webdriver

def test_login_in_admin_panel(app):
    username="admin"
    password='admin'
    app.session.login_in_admin_panel(username=username, password=password)


#http://localhost/litecart/public_html/admin/
def test_login_in_catalog(app):
    username="rusakovalera@gmail.com"
    password='secret'
    app.open_home_page()
    app.session.login_in_catalog(username=username, password=password)
