from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.action = ActionChains(self.driver)

    def handle_dev_password(self):
        try:
            password_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
            )
            password_input.send_keys("1111")

            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()

            print("Dev пароль введён")

        except:
            # если экрана нет — просто идем дальше
            pass

    # --- ВСПОМОГАТЕЛЬНОЕ ---

    def _resolve(self, target):
        """Принимает locator или WebElement"""
        if isinstance(target, tuple):
            return self.wait.until(EC.visibility_of_element_located(target))
        return target

    # --- БАЗОВЫЕ ДЕЙСТВИЯ ---

    def refresh_q(self):
        self.driver.refresh()

    def click(self, target):
        element = self._resolve(target)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def type(self, target, text):
        element = self._resolve(target)
        element.clear()
        element.send_keys(text)

    def get_text(self, target):
        element = self._resolve(target)
        return element.text

    # --- ACTIONS ---

    def move_to_element(self, target):
        element = self._resolve(target)
        self.action.move_to_element(element).perform()

    # --- ПРОВЕРКИ ---

    def is_visible(self, target):
        try:
            self._resolve(target)
            return True
        except:
            return False