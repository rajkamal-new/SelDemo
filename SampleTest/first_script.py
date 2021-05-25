import time

from selenium.webdriver import Chrome

# 1. open the browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = Chrome()

# 2. maximize the browser
driver.maximize_window()

# 3. Go to the url
driver.get("https://stage-dataplatform.tekioncloud.xyz/map/login")

# 4. verify the page is correct
driver.find_element_by_id("USERNAME").send_keys("nkumar@tekion.com")
driver.find_element_by_id("PASSWORD").send_keys("Engineer_01")
driver.find_element_by_tag_name("button").click()

wait = WebDriverWait(driver, 15)
print(len(wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.rt-tbody>div.rt-tr-group")))))
driver.find_element(By.CSS_SELECTOR, "button.ant-btn-icon:not(#TABLE_ITEMS_REFRESH)").click()
driver.find_element(By.CSS_SELECTOR, "div[role='combobox']").click()
time.sleep(5)
# 5. close browser
driver.close()