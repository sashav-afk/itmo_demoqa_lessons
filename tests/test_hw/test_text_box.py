from pages.text_box import TextBox


def test_textbox(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.name.send_keys('Зубенко Михаил Пертович')
    text_box_page.address.send_keys('мафиозник')
    text_box_page.submit.click()
    assert text_box_page.element_1.exist()
    assert text_box_page.element_2.exist()