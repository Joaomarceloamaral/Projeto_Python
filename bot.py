"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for the Web Bot
from botcity.web import WebBot, Browser  # , By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import BotMaestroSDK  # , BotExecution

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    """main function"""
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    webbot = WebBot()

    # Configure whether or not to run on headless mode
    webbot.headless = False

    # Uncomment to change the default Browser to Firefox
    webbot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    webbot.driver_path = r"drivers\geckodriver.exe"

    # Opens the BotCity website.
    webbot.browse("https://www.botcity.dev")

    # Implement here your logic...
    webbot.wait(3000)

    bot.control_a()
    bot.control_c()

    value = bot.get_clipboard()
    print(value)

    # Wait 3 seconds before closing
    webbot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    webbot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    """not found"""
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
