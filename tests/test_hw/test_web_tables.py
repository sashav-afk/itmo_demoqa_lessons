from pages.web_tables import WebTables

def test_web_tables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.btn_add.click()
    web_tables.first_name.send_keys('Михаил')
    web_tables.last_name.send_keys('Зубенко')
    web_tables.user_email.send_keys('lala@mail.ru')
    web_tables.age.send_keys('30')
    web_tables.salary.send_keys('15000')
    web_tables.department.send_keys('department')
    web_tables.btn_submit.click()
    web_tables.btns_edit_record.click()
    web_tables.first_name.send_keys('Михайло')
    web_tables.btns_delite.click()