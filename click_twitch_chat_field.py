import pyautogui
import pygetwindow as gw
import time

def get_browser_window(tab_name):
    window = gw.getWindowsWithTitle(tab_name)

    return window

def click_button_in_browser(browser_window, button_position):
    original_x, original_y = pyautogui.position()
    
    # Get the position and size of the browser window
    browser_x, browser_y, browser_width, browser_height = browser_window[0].left, browser_window[0].top, browser_window[0].width, browser_window[0].height

    # Calculate the absolute position of the button based on the browser window size
    button_x = browser_x + browser_width * button_position[0]
    button_y = browser_y + browser_height * button_position[1]

    # Move the mouse to the button position and click
    pyautogui.moveTo(button_x, button_y, duration=0)
    pyautogui.click()
    
    # Move the mouse back to the original position instantly
    pyautogui.moveTo(original_x, original_y, duration=0)

# Example usage:
if __name__ == "__main__":
    # Specify the tab name of the browser window

    # Set the button position relative to the browser window size (x_ratio, y_ratio)
    button_position = (0.90, 0.93)  # This means the button is located at the center horizontally and 70% down vertically
    
    quintus_tab_name = "Quin69 - Twitch"

    # Find the browser window with the specified tab name
    browser_window = get_browser_window(quintus_tab_name)

    if browser_window:
        # Click the button based on the browser window size and button position
        click_button_in_browser(browser_window, button_position)
    else:
        print(f"Browser window with the tab '{quintus_tab_name}' not found.")
