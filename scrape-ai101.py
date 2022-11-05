from playwright.sync_api import sync_playwright

def save_curriculum(url: str, filename: str, waitfortab: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        #class="c-tabs__accordion-tab"
        #c-tabs__accordion-tab
        week0 = page.locator('css=#' + waitfortab).wait_for()
        tabs = page.locator('css=.c-tabs__accordion-tab')
        for i in range(tabs.count()):
            weekitab = tabs.nth(i)
            weekitab.click()
        page.pdf(path=filename)
        browser.close()


save_curriculum('https://www.agisafetyfundamentals.com/ai-alignment-curriculum', 'alignment101.pdf', 'tab-week-0')
save_curriculum('https://www.agisafetyfundamentals.com/alignment-201-curriculum', 'alignment201.pdf', 'tab-blog-post-title-one-7mj4n')
save_curriculum('https://www.agisafetyfundamentals.com/ai-governance-curriculum', 'aigovernance.pdf', 'tab-week-0')
