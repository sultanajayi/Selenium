from resources.login_page_object import LoginPageObject

test = LoginPageObject()


def test_successful_login(test):
    test.launch_page()
    test.valid_credentials()
    test.login_button()

def test_failed_login(test):
    test.launch_page()
    test.invalid_credentials()
    test.login_button()
    test.error_display()

def test_error_message_display(test):
    test.launch_page()
    test.invalid_credentials()
    test.login_button()
    test.error_message('Invalid credentials')