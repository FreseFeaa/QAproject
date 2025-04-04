import os
from datetime import datetime
import pytest
from jira import JIRA
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from kt3.logg import logger

load_dotenv(override=True)

API_TOKEN = os.getenv("API_TOKEN_SIGMA")
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
bag_screenshot = "failTest.png"
# xfailOK = "xfailOK.png"

def pytest_addoption(parser):
    parser.addoption("--languages",action="store",default="ru",help="Выберите язык")
    parser.addoption("--jira",action="store_true", help="Включить интеграцию с jira")

@pytest.fixture(scope="session")
def jira_client(request):
    logger.info("\n"+"_"*180+"\n")
    if request.config.getoption("jira"):
        jira = JIRA( server=JIRA_SERVER, basic_auth=(JIRA_USERNAME,API_TOKEN))
        return jira

@pytest.fixture
def browser(request):
    language = request.config.getoption("languages")
    options =Options()
    options.add_experimental_option("prefs",{"intl.accept_languages":language})
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1200,1200)
    yield browser
    print("\n quit browser")
    browser.quit()

@pytest.hookimpl(hookwrapper=True) # декоратор - при фазах теста 
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    logger.debug(f"Стадия теста: {report.when}, Cостояние: {report.when}")
    print(report)
#тест упал :(
    if (report.when == "call" and report.outcome == "failed") or (report.when == "call" and hasattr(report,"wasxfail") and report.outcome == "passed"): 
        logger.error(f"Тест не прошёл ({report.outcome}) или у него была метка xfail и он прошёл")  
        if "browser" in item.funcargs: 
            browser = item.funcargs["browser"]  
            browser.save_screenshot(bag_screenshot) 
            logger.debug(f"Скриншот ({bag_screenshot})")  

        if "jira_client" in item.funcargs: 
            jira = item.funcargs["jira_client"]
            if jira:   
                issue_type = jira.issue_types()  
                print("_"*40+"SIGMA PRINT"+"_"*40)
                print(jira.projects()) 
                print(jira.issue_types())
                bug_type = issue_type[5] 
                jira_issue = {
                    "project": {"key": "SIGMA"},
                    "summary":f"{item.name}",
                    "description": f"Ошибка: {report.longreprtext}\n\n Дата: {datetime.now()}",
                    "issuetype": {"id":bug_type.id}
                    }
                new_issue = jira.create_issue(fields=jira_issue)

                jira.add_attachment(new_issue.key,bag_screenshot)
                logger.debug(f"Создание Бага в JIRA ({jira_issue['issuetype']}) {bag_screenshot})")  
                
