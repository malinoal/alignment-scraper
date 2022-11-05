from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://www.agisafetyfundamentals.com/ai-alignment-curriculum')
    for i in range(9):
        #id="tab-week-i"
        weekitab = page.locator("css=#tab-week-" + str(i))
        weekitab.click()
        #tabpanel-week-i
        weekicontent = page.locator("css=#tabpanel-week-" + str(i))
        weekicontent.click()
    #tab-further-alignment-resources
    #tabpanel-further-alignment-resources
    furthercontenttab = page.locator("css=#tab-further-alignment-resources")
    furthercontenttab.click()
    furthercontentcontent = page.locator("css=#tabpanel-further-alignment-resources")
    furthercontentcontent.click()
    page.pdf(path=f'alignment101.pdf')
    browser.close()
