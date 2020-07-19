from selenium import webdriver
import argparse


def main():
    driver = webdriver.Remote(command_executor=args.url, desired_capabilities={})
    driver.close()  # this prevents the dummy browser
    driver.session_id = args.id


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url")
    parser.add_argument("-i", "--id")
    args = parser.parse_args()
    main()
