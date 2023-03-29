from src.crawler import ChromeDriver,ChromeOption
from pymongo import MongoClient

def prepare(args):
    chrome_options=ChromeOption(detach=args.detach,
                                headless=args.headless,
                                maximize_window=args.maximize_window)

    chrome_driver=ChromeDriver(chrome_options,
                               executable_path=args.executable_path)
    if args.require_login:
        chrome_driver.load_url('https://anime-pictures.net/login?lang=en')
        chrome_driver.require_login(username=args.username,password=args.password)
    
    # client=MongoClient('mongodb://test-api-ai:Hahalolo%402022@10.10.11.100:27017/?authSource=test-api-ai')
    return chrome_driver#,client


def crawl(args):
    chrome_driver=prepare(args)
    if args.post_id==-1:
        post_id=int(open('id.txt','r').read())
    else:
        post_id=int(args.post_id)
    while True:
        output=chrome_driver.anime_picture_crawl_from_post_id(post_id)
        print(output)
        # client['test-api-ai']['images'].insert_one(output)
        post_id+=1
        with open('id.txt','w') as f:
            f.write(str(post_id))
        if post_id>=100000:
            break


