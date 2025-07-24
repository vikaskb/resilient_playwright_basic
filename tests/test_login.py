from playwright.sync_api import sync_playwright
import json

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        with open("selectors.json") as f:
            selectors = json.load(f)

        page.goto("https://example.com/login")
        page.fill(selectors["username"], "testuser")
        page.fill(selectors["password"], "password123")
        page.click(selectors["submit"])
        assert "Dashboard" in page.content()
        browser.close()
