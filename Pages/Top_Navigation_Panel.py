#Page for top panel locators

class top_panel():
    create_new = "//summary[contains(@aria-label,'Create new…')]"
    new_gist = "//a[contains(.,'New gist')]"
    profile = "//summary[contains(@data-ga-click,'Header, show menu, icon:avatar')]"
    sign_out = "//button[contains(.,'Sign out')]"
    your_gist = "//a[contains(.,'Your gists')]"