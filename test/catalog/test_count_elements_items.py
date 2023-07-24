from selenium.webdriver.common.by import By

def test_stickers_check_in_catalog(app):
    app.open_home_page()

    all_stickers = 0

    items = app.catalog.find_all_items_from_catalog()
    for item in items:
            sticker = item.find_elements(By.XPATH, ".//div[starts-with(@class,'sticker')]")
            assert len(sticker) == 1, "Количество стикеров у товара больше 1"

            all_stickers = all_stickers + len(sticker)

    assert app.catalog.count_all_items_in_catalog() == all_stickers, "Количество карточек не совпадает с количеством стикеров"