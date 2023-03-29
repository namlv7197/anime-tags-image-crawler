from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import yaml

class ChromeDriver(webdriver.Chrome):
    def __init__(self,chrome_options,executable_path='chromedriver'):
        super(ChromeDriver,self).__init__(chrome_options=chrome_options,
                                          executable_path=executable_path)
        
    def load_url(self,url,wait=5):
        self.get(url)
        time.sleep(wait)

    def require_login(self,
                      username=None,
                      password=None,
                      css_selector_username="input[type='text']",
                      css_selector_password="input[type='password']",
                      css_selector_submit="input[type='submit']",
                      wait=5):
        
        if username=='' or password=='':
            config=yaml.safe_load(open('./config/config.yaml'))
            username=config['username']
            password=config['password']
            
        self.find_element(By.CSS_SELECTOR, css_selector_username).send_keys(username)
        self.find_element(By.CSS_SELECTOR, css_selector_password).send_keys(password)
        self.find_element(By.CSS_SELECTOR, css_selector_submit).click()
        time.sleep(wait)

    def anime_picture_crawl_from_post_id(self,post_id,lang='en',wait=1):
        self.load_url(f'https://anime-pictures.net/posts/{str(post_id)}?lang={lang}',wait=wait)
        character_tags=[]
        reference_tags=[]
        object_tags=[]
        full_image_url=''
        small_image_url=''
        artist=[]
        try:
            download=self.find_element(By.CSS_SELECTOR,"a[class='download_icon svelte-iczcvx']")
            full_image_url=download.get_attribute('href')
            tags=self.find_element(By.CSS_SELECTOR,"ul[class='tags svelte-bnip2f']")

            char_tags=tags.find_elements(By.XPATH,"//li/a[contains(@class,'svelte-1a4tkgo') and contains(@class,'big_tag') and contains(@class,'character')]")
            for c in char_tags:
                character_tags.append(c.text)
            
            a_tags=tags.find_elements(By.XPATH,"//li/a[contains(@class,'svelte-1a4tkgo') and contains(@class,'artist') and contains(@class,'big_tag')]")
            for i in a_tags:
                artist.append(i.text)

            ref_tags=tags.find_elements(By.XPATH,"//li/a[contains(@class,'svelte-1a4tkgo') and contains(@class,'reference') and contains(@class,'object')]")
            for f in ref_tags:
                reference_tags.append(f.text)

            obj_tags=tags.find_elements(By.XPATH,"//li/a[@class='svelte-1a4tkgo not_my_tag_border']")+tags.find_elements(By.XPATH,"//li/a[@class='svelte-1a4tkgo']")
            for o in obj_tags:
                object_tags.append(o.text)

            small_image_url=self.find_element(By.ID,'big_preview').get_attribute('src')
        except:pass

        return {
            'id':post_id,
            'character_tags':character_tags,
            'reference_tags':reference_tags,
            'object_tags':object_tags,
            'full_image_url':full_image_url,
            'small_image_url':small_image_url,
            'artist':artist
        }
    
class ChromeOption(Options):
    def __init__(self,detach=False,headless=False,maximize_window=False):
        super(ChromeOption,self).__init__()
        
        if detach:
            self.add_experimental_option('detach',detach)

        if headless:
            self.add_argument('headless')
        
        if maximize_window:
            self.add_argument('start-maximized')
        