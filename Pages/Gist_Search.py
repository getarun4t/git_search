#Locators for search functionality is saved here

class Search_Page():
    search_textbox = "//input[@class='form-control input-sm js-site-search-focus header-search-input']"
    search_textbox_logged = "//input[contains(@class,'form-control input-sm js-site-search-focus header-search-input js-navigation-enable js-quicksearch-field')]"
    
class Search_Results():
    secret_gist = 'Secret'
    public_gist = 'getarun4t'
    
class Sign_in():
    si_button = "//a[@data-ga-click='Header, sign in']"