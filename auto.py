from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException, ElementNotVisibleException, ElementNotSelectableException, ElementNotInteractableException, InvalidSessionIdException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from filesmanger import *

derr_path = r"./chromedriver.exe"


def waite(derr: WebDriver, timeOut: int = 10):
    return WebDriverWait(derr, timeOut, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])


def login(derr: WebDriver, account, cokei, check, fill, unknow):
    derr.refresh()
    time.sleep(2)
    if 'category=your_pages' in derr.current_url:
        return True
    elif ('login_attempt=1' in derr.current_url) or ('login.php?next=' in derr.current_url):
        remove_account(cokei)
        set_fill_account(fill, account=account)
        return False
    elif 'checkpoint' in derr.current_url:
        checked_account(check, account=account)
        remove_account(cokei)
        return False


def openPageLink(derr: WebDriver):
    try:
        el = waite(derr=derr, timeOut=10).until(
            lambda d: d.find_element_by_css_selector('[href*="?ref=pages_you_manage"]'))
        el.click()
        return True
    except:
        return False


def openAddsLinks(derr: WebDriver, cokies, account, unknow):
    try:
        try:
            el = waite(derr=derr, timeOut=30).until(
                lambda d: d.find_element_by_css_selector('[href*="/ad_center/create/boostpost/?entry_point"]'))
            el.click()
        except ElementNotInteractableException:
            el = waite(derr=derr, timeOut=5).until(
                lambda d: d.find_element_by_css_selector('[href*="/ad_center/create/boostpost/?entry_point"]'))
            el.click()
        try:
            el2 = waite(derr=derr, timeOut=30).until(lambda d: d.find_element_by_css_selector(
                '[aria-label="Boost Post Now"] div.s1i5eluu'))
            el2.click()
        except ElementNotInteractableException:
            el2 = waite(derr=derr, timeOut=30).until(lambda d: d.find_element_by_css_selector(
                '[aria-label="Boost Post Now"] div.s1i5eluu'))
            el2.click()
        return True
    except TimeoutException:
        remove_account(cokies)
        set_fill_account(unknow, account)
        return False


def click_next(derr: WebDriver, timeOut=10):
    try:
        time.sleep(0.5)
        el = waite(derr=derr, timeOut=timeOut).until(
            lambda d: d.find_element_by_css_selector('[aria-label="Next"]'))
        el.click()
    except ElementNotInteractableException:
        click_next(derr=derr)


def click_save(derr: WebDriver, timeOut=10):
    try:
        time.sleep(0.5)
        el = waite(derr=derr, timeOut=timeOut).until(
            lambda d: d.find_element_by_css_selector('[aria-label="Save"]'))
        el.click()
    except ElementNotInteractableException:
        click_save(derr=derr)


def click_back(derr: WebDriver):
    try:
        time.sleep(0.5)
        el = waite(derr=derr, timeOut=10).until(
            lambda d: d.find_element_by_css_selector('[aria-label="Back"]  span.knomaqxo'))
        el.click()
    except ElementNotInteractableException:
        click_back(derr=derr)


def click_get_started(derr: WebDriver):
    time.sleep(0.5)
    el = waite(derr=derr, timeOut=5).until(
        lambda d: d.find_element_by_css_selector('aria-label="Get Started"'))
    el.click()


def click_done(derr: WebDriver):
    time.sleep(0.5)
    el = waite(derr=derr, timeOut=5).until(
        lambda d: d.find_element_by_css_selector('[aria-label="Done"]'))
    el.click()


def click_close(derr: WebDriver):
    time.sleep(0.5)
    el = waite(derr=derr, timeOut=5).until(
        lambda d: d.find_element_by_css_selector('aria-label="Close"'))
    el.click()


def click_leav(derr: WebDriver):
    time.sleep(0.5)
    el = waite(derr=derr, timeOut=5).until(
        lambda d: d.find_element_by_css_selector('aria-label="Leave"'))
    el.click()


def click_publish(derr: WebDriver):
    time.sleep(0.5)
    el = waite(derr=derr, timeOut=5).until(
        lambda d: d.find_element_by_css_selector('[aria-label="Publish Page"] span.g0qnabr5'))
    el.click()


def leav_whatsapp(derr: WebDriver):
    click_close(derr=derr)
    time.sleep(0.7)
    click_leav(derr=derr)


def publish(derr: WebDriver):
    click_publish(derr=derr)
    time.sleep(3)
    derr.refresh()


def get_started(derr: WebDriver):
    try:
        click_done(derr=derr)
    except:
        pass
    time.sleep(0.7)
    click_next(derr=derr, timeOut=5)
    click_get_started(derr=derr)


def openPage(derr: WebDriver):
    try:
        get_started(derr=derr)
    except:
        pass
    if openPageLink(derr=derr):

        try:
            leav_whatsapp(derr=derr)
        except:
            pass
        return True
    else:
        return False


def select_contry(derr: WebDriver):
    contry = waite(derr).until(lambda d: d.find_element_by_xpath(
        "//*/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div/div/div/div/div/label/div"))
    contry.click()
    time.sleep(2)
    venz = wait(derr=derr).until(lambda d: d.find_element_by_xpath(
        "//*/div/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[241]"))
    venz.click()
    time.sleep(1)
    click_save(derr=derr)


def next_and_back(derr: WebDriver):
    click_next(derr)
    click_save(derr)
    click_back(derr)


def _five_svave_back(derr: WebDriver):
    next_and_back(derr)
    time.sleep(2)
    next_and_back(derr)
    time.sleep(2)
    next_and_back(derr)
    time.sleep(2)
    next_and_back(derr)
    time.sleep(2)
    next_and_back(derr)


def end(derr: WebDriver):
    time.sleep(1)
    derr.quit()
    time.sleep(2)


class Automation:
    filePath = ''
    folderPath = ''
    cokies_count = 0

    def __init__(self, runing, parent,  automated=True):
        self._runing = runing
        self.parent = parent
        self.automated = automated

    def set_file_path(self, file_path: str):
        self.filePath = file_path
        self.cokies_count = len(open(self.filePath, 'r').readlines())
        return self.filePath.strip() != ''

    def set_folder_path(self, folder_path: str):
        self.folderPath = folder_path
        return self.folderPath.strip() != ''

    def run(self):
        while self._runing != False:
            derr: WebDriver
            try:
                if self.automated:
                    derr = self.automation()
                else:
                    derr = self.partly_auto()
            except Exception as e:
                try:
                    derr.quit()
                except:
                    pass
            time.sleep(1)

    def setStutus(self, running):
        self._runing = running

    def set_automated(self, automated):
        self.automated = automated

    def automation(self):
        try:
            user, passw, cokeis = get_account_from_file(self.filePath)
        except:
            return
        done, check, fill, unknow = create_files(self.folderPath)
        info = get_files_inf([done, check, fill, unknow])
        sum_inf = int(sum(info))
        self.parent.update_info(info, sum_inf, self.cokies_count)
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option('useAutomationExtension', False)
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        option.page_load_strategy = "eager"
        derr = webdriver.Chrome(derr_path, options=option)

        try:
            derr.get(
                "https://www.facebook.com/pages/?category=your_pages&ref=bookmarks")
            for cokei in cokeis:
                try:
                    name, val = cokei.split("=")
                    name = name.replace(' ', '').replace(
                        '\r', '').replace('\n', '')
                    val = val.replace(' ', '').replace(
                        '\r', '').replace('\n', '')
                    cok = {'name': name, 'value': val, 'sameSite': 'Strict'}
                    derr.add_cookie(cookie_dict=cok)
                except:
                    pass
                derr.add_cookie(cookie_dict=cok)
            cok = {'name': 'locale', 'value': 'en_US', 'sameSite': 'Strict'}
            derr.add_cookie(cookie_dict=cok)
        except WebDriverException:
            derr.quit()

        writed = user+":"+passw+":"+';'.join(cokeis)
        if login(derr=derr, account=writed, cokei=self.filePath, check=check, fill=fill, unknow=unknow) == True:
            if openPage(derr=derr):
                try:
                    publish(derr=derr)
                except:
                    pass
                if openAddsLinks(derr, self.filePath, writed, unknow) == True:
                    try:
                        select_contry(derr=derr)
                    except:
                        pass
                    _five_svave_back(derr)
                    remove_account(self.filePath)
                    set_done_accout(done, account=writed)
                    end(derr=derr)
                else:
                    derr.quit()
                    return
            else:
                remove_account(self.filePath)
                set_fill_account(fill, account=writed)
                derr.quit()
        else:
            derr.quit()
        return derr

    def partly_auto(self):
        try:
            user, passw, cokeis = get_account_from_file(self.filePath)
        except:
            return
        done, check, fill, unknow = create_files(self.folderPath)
        info = get_files_inf([done, check, fill, unknow])
        sum_inf = int(sum(info))
        self.parent.update_info(info, sum_inf, self.cokies_count)
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option('useAutomationExtension', False)
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        option.page_load_strategy = "eager"
        derr = webdriver.Chrome(derr_path, options=option)

        try:
            derr.get(
                "https://www.facebook.com/pages/?category=your_pages&ref=bookmarks")
            for cokei in cokeis:
                try:
                    name, val = cokei.split("=")
                    name = name.replace(' ', '').replace(
                        '\r', '').replace('\n', '')
                    val = val.replace(' ', '').replace(
                        '\r', '').replace('\n', '')
                    cok = {'name': name, 'value': val, 'sameSite': 'Strict'}
                    derr.add_cookie(cookie_dict=cok)
                except:
                    pass
                derr.add_cookie(cookie_dict=cok)
            cok = {'name': 'locale', 'value': 'en_US', 'sameSite': 'Strict'}
            derr.add_cookie(cookie_dict=cok)
        except WebDriverException:
            derr.quit()

        writed = user+":"+passw+":"+';'.join(cokeis)
        if login(derr=derr, account=writed, cokei=self.filePath, check=check, fill=fill, unknow=unknow) == True:
            while True:
                try:
                    _ = derr.window_handles
                except Exception as e:
                    del derr
                    set_done_accout(done, writed)
                    remove_account(self.filePath)
                    break
                    return
                time.sleep(1)
        else:
            derr.quit()
        return derr
