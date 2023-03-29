from src.crawler import ChromeDriver,ChromeOption
import argparse
from src.utils import crawl

def args_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--post_id",
                        type=str,
                        default=-1,
                        help="""parse the specific post id to crawl""")

    parser.add_argument("--detach",
                        type=bool,
                        default=True,
                        help="""This argument means that after the tests have finished running, the browser window will remain open and visible to the user. By default, when a Selenium test script finishes running, the browser window will be closed automatically"""
                        )
    
    parser.add_argument("--headless",
                       type=bool,
                       default=True,
                       help="""This argument means that Chrome driver will run in a mode that displays a graphical user interface (GUI). By default, when a Selenium test script finishes running, there will be no visible browser window.""",
                       )
    
    parser.add_argument("--maximize_window",
                        type=bool,
                        default=False,
                        help="""This argument means that Chrome driver will start the Chrome browser with its window maximized, so that it takes up the entire screen. By default, the window will be not maximum"""
                        )

    parser.add_argument("--executable_path",
                        type=str,
                        default='chromedriver',
                        help="""This argument means that the directory contains chromedriver file"""
                        )
    
    parser.add_argument("--require_login",
                        type=bool,
                        default=True,
                        help="""This argument means that website needs user to login to render its content"""
                        )
    
    parser.add_argument("--username",
                        type=str,
                        default='',
                        help="""This argument means that providing username if require_login is True""")
    
    parser.add_argument("--password",
                        type=str,
                        default='',
                        help="""This argument means that providing password if require_login is True""")
    
    return parser.parse_args()

def main(args):
    crawl(args)


if __name__=='__main__':
    args=args_parser()
    main(args)

