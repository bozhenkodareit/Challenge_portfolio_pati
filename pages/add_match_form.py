from pages.base_page import BasePage


class Dashboard(BasePage):
    header_text_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h6 MuiTypography-noWrap')]"
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]"
    main_page_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]"
    players_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[1]"
    current_player_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]"
    current_player_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[1]"
    matches_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]"
    matches_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[1]"
    reports_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[3]/div[2]"
    reports_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[3]/div[1]"
    lang_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]/div[2]"
    lang_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]/div[1]"
    signout_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]/div[2]"
    signout_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]/div[1]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]"
    pass

