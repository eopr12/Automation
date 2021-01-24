#!/usr/bin/env python
# coding: utf-8

# In[20]:


from selenium import webdriver
import requests


# In[21]:


# # 크롬 드라이버 경로 지정
# driver = webdriver.Chrome('C:/Users/Becky/chromedriver_win32/chromedriver.exe')

# # Session & header 설정
# session = requests.Session()
# session.headers = {"User-Agent": "Chrome/87.0 (Macintosh; Intel Win 10 10_9_5)\
#          WindowsWebKit 3.80.36 (KHTML, like Gecko) Chrome",
#                    "Accept": "text/html,application/xhtml+xml,application/xml;\
#          q=0.9,imgwebp,*/*;q=0.8"}


# In[22]:


# #specifying login info in advance_1
# public class WebdriverSetup {   
#     public static String chromedriverPath = "C:\\Users\\pburgr\\Desktop\\selenium-tests\\GCH_driver\\chromedriver.exe";

#     // my default profile folder
#     public static String chromeProfilePath = "C:\\Users\\pburgr\\AppData\\Local\\Google\\Chrome\\User Data";    

#     public static WebDriver driver; 
#     public static WebDriver startChromeWithCustomProfile() {
#         System.setProperty("webdriver.chrome.driver", chromedriverPath);
#         ChromeOptions options = new ChromeOptions();

#         // loading Chrome with my existing profile instead of a temporary profile
#         options.addArguments("user-data-dir=" + chromeProfilePath);

#         driver = new ChromeDriver(options);
#         driver.manage().window().maximize();
#         return driver;
#     }
#     public static void shutdownChrome() {
#         driver.close();
#         driver.quit();
#     }
# }


# In[23]:


# #specifying login info in advance_2
# # 크롬 드라이버 경로 지정
# driver = webdriver.Chrome('C:/Users/Becky/chromedriver_win32/chromedriver.exe')

# #extract session _id / _url from driver object 
# url = driver.command_executor._url
# session_id = driver.session_id

# #use these two parameter to connect to your driver
# driver = webdriver.Remote(command_executor=url,desired_capabilities={})
# driver.close()
# driver.session_id = session_id

# #connect to driver again
# driver.get('https://sellercentral.amazon.com/orders-v3/fba/all?page=1&date-range=last-14')


# In[25]:


# specifying login info in advance_3
# launch Chrome with custom flag, and open port for remote debugging
chrome.exe --remote-debugging-port=1111 --user-data-dir="C:\selenum\AutomationProfile"

# Selenium connect to opened browser with below code
System.setProperty("webdriver.chrome.driver", "C:/Users/Becky/chromedriver_win32/chromedriver.exe");
chromeOptions options = new ChromeOptions();
options.setExperimentalOption("debuggerAddress", "127.0.0.1:1111");
WebDriver driver = new ChromeDriver(options);`


# In[10]:


#opening url
driver.execute_script("window.open('https://sellercentral.amazon.com/orders-v3/fba/all?page=1&date-range=last-14');")


# In[11]:


# #login_id_1
# WebElement email=driver.findElement(By.id("ap_email"));
# email.sendKeys("rori.lee@dfirst-inc.com");
# Thread.sleep(1000);


# In[15]:


# #login_id_2
# # email = driver.find_element_by_id("ap_email")
# email = driver.find_element_by_xpath('//*[@id="ap_email"]')
# # WebElement email = driver.findElement(By.id("//*[@id='ap_email']/div"));
# email.sendKeys("rori.lee@dfirst-inc.com");
# Thread.sleep(1000);


# In[16]:


# #login_pw
# WebElement password=driver.findElement(By.id("ap_password"));
# password.sendKeys("m20210101");


# In[17]:


# #login_click button
# WebElement loginButton = driver.findElement(By.xpath("//*[@id='sinInSubmit']/span"));
# loginButton.click();
# Thread.sleep(10000);


# In[13]:


#finding elements
element = webDriver.findElement(By.xpath("//*[@class='cell-body-title']/div")).click()
#driver.find_element_by_id()
#driver.find_element_by_class_name()
#driver.find_element_by_name()
#webDriver.findElement(By.xpath("//a[@href='']")).click();

#clicking elements
element.click();

