from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)

# เปิดไฟล์ index.html ด้วย browser
driver.get("file:///C:/Users/User/Content/demo-selenium/labubu.html")

# รอจนกว่าหน้าเว็บโหลดเสร็จ
driver.implicitly_wait(30)

# รอให้หน้ารอคิวหายไป และหน้าสั่งซื้อปรากฏ
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "queue-page"))
)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "order-form"))
)

# กรอกข้อมูลในฟอร์ม
driver.find_element(By.ID, "name").send_keys("ทดสอบ ระบบ")
driver.find_element(By.ID, "phone").send_keys("0812345678")
driver.find_element(By.ID, "address").send_keys("123 ถนนทดสอบ, เมืองทดสอบ, 12345")
driver.find_element(By.ID, "quantity").send_keys("2")

# เลือกระดับความเผ็ด
spice_level = driver.find_element(By.ID, "spice-level")
spice_level.send_keys("เผ็ดปานกลาง")

# ส่งฟอร์ม
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# รอให้หน้าสรุปปรากฏ
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "summary-page"))
)

# ตรวจสอบข้อมูลในหน้าสรุป
summary = driver.find_element(By.ID, "order-summary").text
print("สรุปการสั่งซื้อ:")
print(summary)

# ตรวจสอบว่าข้อมูลถูกต้อง
assert "ทดสอบ ระบบ" in summary
assert "0812345678" in summary
assert "123 ถนนทดสอบ, เมืองทดสอบ, 12345" in summary
assert "จำนวน: 2" in summary
assert "ระดับความเผ็ด: medium" in summary
assert "ราคารวม: 100 บาท" in summary

print("การทดสอบเสร็จสมบูรณ์")

# ปิด browser
driver.quit()