from pages.base_page import BasePage


class Dashboard(BasePage):
    header_text_xpath = "//*[contains(@class, 'MuiTypography-root MuiTypography-h6 MuiTypography-noWrap')]"
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]"
    main_page_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]"
    players_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[1]"
    lang_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]"
    lang_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[1]"
    signout_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]"
    signout_icon_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[1]"
    add_player_link_xpath = "//a[contains(@href, '/players/add')]"
    dev_team_contact_link_xpath = "//a[contains(@href, 'https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6')]"

    pass

