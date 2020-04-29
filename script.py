from selenium import webdriver

# Place driver in CWD (this setup uses Firefox)
# At this you can change web browser, 
# but install browser and download driver first
browser = webdriver.Firefox('.')

# Example for Chrome
#browser = webdriver.Chrome('.')

# Maximize window just for fun
browser.maximize_window()

def load_page(url=None):
    global browser
    # Add https part to url if needed
    if not 'http://' in url or not 'https://' in url: url = 'https://' + url        
    browser.get(url)
    print("Loaded page", url)

# Example function to refresh currently focused tab
def perform_refresh():
    global browser
    browser.refresh()
    print("Refreshed page")

#TODO make automation here
load_page('google.com')
perform_refresh()

# Close automated browser window
browser.close()