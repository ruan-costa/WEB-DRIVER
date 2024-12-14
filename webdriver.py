from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib3
import logging


class Driver:
    """
    Esta classe representa um driver web Selenium.

    Atributos:
        headless (bool): Indica se o driver deve ser executado no modo headless (sem interface gráfica) ou não. O padrão é False.
        dir_dwld (str): O diretório onde os arquivos baixados devem ser salvos. O padrão é None.

    Métodos:
        driver: Retorna o driver web inicializado.
        setup: Inicializa e configura o driver web.
    """


    def __init__(self, headless=False, dir_dwld=None):
        self.headless = headless
        self.dir_dwld = dir_dwld
        self._driver = None

    @property
    def driver(self):
        if self._driver is None:
            self._driver = self.setup()
        return self._driver

    def setup(self):
        print("> Iniciando driver")
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        os.environ['WDM_LOG'] = str(logging.NOTSET)
        os.environ['WDM_SSL_VERIFY'] = '0'
        options = Options()
        if self.headless:
            options.add_argument('headless')
        if self.dir_dwld is not None:
            p = {'download.default_directory': self.dir_dwld}
            options.add_experimental_option('prefs', p)
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument('--window-size=1200,800')
        options.add_argument("--lang=pt-BR")
        #service = webdriver.ChromeService(r'\\repositorio.tivit.bpo\MIS\OPERACIONAL\CONTROLES MIS\SERVICOS\AUTOMACOES\VR\chromedriver.exe')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
