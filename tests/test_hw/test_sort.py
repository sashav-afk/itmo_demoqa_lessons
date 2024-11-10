from pages.web_tables import WebTables

def test_sort(browser):
    web_tables = WebTables(browser)
    web_tables.visit()

    web_tables.heads_sort.click()