# 上海大学每日两报补报

## 环境

Python 3, Selenium

## 用法

拒 绝 输 入 ， 直 接 改 码

```python
## ID and Password
self.driver.find_element(By.ID, "username").send_keys("20120000")
self.driver.find_element(By.ID, "password").click()
self.driver.find_element(By.ID, "password").send_keys("123456")
self.driver.find_element(By.ID, "submit").click()
```

## 待解决问题

由于元素查找方式（查找含“未填报”文本元素），只能在晚报时间使用