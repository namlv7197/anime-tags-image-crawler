from src.crawler import ChromeDriver
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient

def prepare(args):
    chrome_options=Options()
    chrome_options.add_experimental_option('detach',True)
    chrome_options.add_argument('headless')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--no-sandbox')

    chrome_driver=ChromeDriver(chrome_options,
                               executable_path='driver')

    chrome_driver.load_url('https://anime-pictures.net/login?lang=en')
    chrome_driver.require_login(username=args.username,password=args.password)

    client=MongoClient(args.uri)
    return chrome_driver,client


def crawl(args):
    chrome_driver,client=prepare(args)
    curr_post_id=list(client[args.db][args.collection].find().sort('post_id',-1).limit(1))
    if curr_post_id==[]:
        curr_post_id=1
    else:
        curr_post_id=curr_post_id[0]['id']

    post_id=max(int(args.post_id),int(curr_post_id))
    while True:
        output=chrome_driver.anime_picture_crawl_from_post_id(post_id)

        client[args.db][args.collection].insert_one(output)
        post_id+=1