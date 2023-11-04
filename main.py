from botcity.core import DesktopBot
import pyautogui
from botcity.plugins.discord import BotDiscordPlugin
from datetime import datetime, timedelta
import requests
import logging
dia = datetime.today().strftime('%d')
mes = datetime.today().strftime('%m')
ano = datetime.today().strftime('%y')
logging.basicConfig(level=logging.INFO, filename=fr'C:\LogsFlutuacao\{dia+mes+ano}.txt', format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
class Bot(DesktopBot):
    def action(self, execution=None):
        # nome do arquivo a executar
        self.execute(f'C:\RMS\WRMS\SRVRMS\EXE\WRMS.exe')
        self.wait(5000)
        self.save_screenshot("inicio.png")
        url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
        ds = BotDiscordPlugin(urls=url, username="robo")
        ds.send_message(content='O Robo começou a rodar!')
        ds.send_file(files=['inicio.png'])
        # requests.get('http://192.168.0.179/telegram/a.php?messageText=' + 'INICIANDO ROBO FLUTUAÇÃO')
        # if not self.find( "cliq", matching=0.97, waiting_time=100000):
        #     self.not_found("cliq")
        # self.click()
        self.wait(2000)
        pyautogui.write('bot')
        self.tab()
        self.paste('abc.321.')
        self.enter()
        if not self.find( "cadastro", matching=0.97, waiting_time=100000):
            self.not_found("cadastro")
        self.doubleclick()
        if not self.find( "edi", matching=0.97, waiting_time=10000):
            self.not_found("edi")
        self.doubleclick()
        if not self.find( "exporta", matching=0.97, waiting_time=10000):
            self.not_found("exporta")
        self.doubleclick()
        if not self.find( "vigencia", matching=0.97, waiting_time=100000):
            self.not_found("vigencia")
        self.wait(2000)
        pyautogui.press('f6')
        self.wait(1000)
        dia = datetime.today() + timedelta(1)
        mes = datetime.today().strftime('%m')
        ano = datetime.today().strftime('%y')
        if dia.strftime("%d") == '01':
            mes = datetime.today() + timedelta(1)
            mes = mes.strftime('%m')
        if dia.strftime("%d") == '01' and mes == '01':
            ano = int(ano)
            ano = ano + 1
            ano = str(ano)
        dia = dia.strftime('%d')
        pyautogui.write(dia)
        pyautogui.write(mes)
        pyautogui.write(ano)
        data_flutuacao = f'20{ano}-{mes}-{dia}'
        logging.info(f'=================================================')
        logging.info(f'Data Informada: {dia}/{mes}/{ano}')
        # requests.get('http://192.168.0.179/telegram/a.php?messageText=' + 'INICIANDO PROCESSO DE EXPORTAÇÃO PRA WEB NO RMS')
        self.enter()
        pyautogui.press('f4')
        self.save_screenshot("rms.png")
        url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
        ds = BotDiscordPlugin(urls=url, username="robo")
        ds.send_message(content='Iniciando exportação para Web!')
        ds.send_file(files=['rms.png'])
        if not self.find( "fim", matching=0.97, waiting_time=1000000000000000):
            self.not_found("fim")
        self.double_click_relative(265, 242)
        self.wait(3000)
        pyautogui.press('f3')
        self.wait(2000)
        pyautogui.press('f3')
        self.wait(2000)
        if not self.find( "minimizado", matching=0.97, waiting_time=10000):
            self.not_found("minimizado")
        self.click()
        self.wait(2000)
        pyautogui.press('f3')
        self.wait(2000)
        self.enter()
        self.wait(10000)
        requests.get('http://192.168.0.179/telegram/a.php?messageText=' + 'PROCESSO NO RMS FINALIZADO!')
        logging.info(f'=================================================')
        logging.info(f'Final do Processo no RMS')
        logging.info(f'=================================================')
        logging.info(f'Iniciando processo do SysPDVWEB')

        # PARTE DO SYSPDVWEB
        self.browse("http://192.168.0.232:8081")
        self.save_screenshot("web.png")
        if not self.find( "login", matching=0.97, waiting_time=100000):
            self.not_found("login")
        self.click_relative(48, 41)
        self.paste('syspdv')
        self.tab()
        if not self.find( "senha", matching=0.97, waiting_time=10000):
            self.not_found("senha")
        self.click_relative(47, 39)
        self.paste('syspdv')
        self.enter()
        if not self.find( "lupa", matching=0.97, waiting_time=100000):
            self.not_found("lupa")
        self.click_relative(42, 10)
        self.paste('produtos retaguarda')
        if not self.find( "produtoss", matching=0.97, waiting_time=100000):
            self.not_found("produtoss")
        self.click()
        if not self.find( "todas", matching=0.97, waiting_time=1000000):
            self.not_found("todas")
        self.wait(5000)
        self.click_relative(-31, 2)
        self.wait(2000)
        if not self.find( "concluir", matching=0.97, waiting_time=1000000):
            self.not_found("concluir")
        self.click()
        self.wait(1000)
        requests.get('http://192.168.0.179/telegram/a.php?messageText=' + 'SINCRONIZANDO PRODUTOS RETAGUARDA')
        self.save_screenshot("retaguarda.png")
        url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
        ds = BotDiscordPlugin(urls=url, username="robo")
        ds.send_message(content='Sincronizando produtos retaguarda!')
        ds.send_file(files=['retaguarda.png'])
        if not self.find( "retaguardaokk", matching=0.97, waiting_time=10000000000):
            self.not_found("retaguardaokk")
        self.click_relative(168, 68)
        self.wait(5000)
        if not self.find( "lupa", matching=0.97, waiting_time=10000):
            self.not_found("lupa")
        self.click_relative(65, 16)
        self.paste('lojas')
        if not self.find( "sincronizandoloj", matching=0.97, waiting_time=10000):
            self.not_found("sincronizandoloj")
        self.click()
        if not self.find( "marcarlojas", matching=0.97, waiting_time=100000):
            self.not_found("marcarlojas")
        self.wait(2000)
        self.click_relative(19, 107)
        if not self.find( "alteradoss", matching=0.97, waiting_time=10000):
            self.not_found("alteradoss")
        self.click()
        if not self.find( "simmm", matching=0.97, waiting_time=10000):
            self.not_found("simmm")
        self.click()
        requests.get('http://192.168.0.179/telegram/a.php?messageText=' + 'SINCRONIZANDO LOJAS')
        self.save_screenshot("sincronizar.png")
        url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
        ds = BotDiscordPlugin(urls=url, username="robo")
        ds.send_message(content='Sincronizando lojas!')
        ds.send_file(files=['sincronizar.png'])
        self.wait(10000)
        self.enter()
        pyautogui.hotkey('ctrl', 'w')
        self.wait(2000)
        pyautogui.hotkey('ctrl', 'w')
        logging.info(f'=================================================')
        logging.info(f'Final do Processo no SysPDVWEB')
        requests.get('http://192.168.0.179/telegram/a.php?messageText=' + 'PROCESSO DO SYSPDVWEB FINALIZADO!')
        logging.info(f'=================================================')
        logging.info(f'Iniciando processo do CartazFacil')
        url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
        ds = BotDiscordPlugin(urls=url, username="robo")
        ds.send_message(content=f'Iniciando processo do cartazfacil!')
        res = requests.get(f'http://192.168.0.183:3469/initCV12/{data_flutuacao}/0')
        resultado = res.status_code
        logging.info(f'=================================================')
        logging.info(f'Processo finalizado')
        self.wait(5000)
        url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
        ds = BotDiscordPlugin(urls=url, username="robo")
        ds.send_message(content='Processo 1 do cartaz finalizado!')
        if resultado == 200:
            res2 = requests.get(f'http://192.168.0.183:3469/initCV16/{data_flutuacao}/0')
            resultado2 = res2.status_code
            logging.info(f'=================================================')
            logging.info(f'Processo 2 do cartaz finalizado')
            url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
            ds = BotDiscordPlugin(urls=url, username="robo")
            ds.send_message(content='Processo 2 do cartaz finalizado!')
            self.wait(5000)
            if resultado2 == 200:
                requests.get('http://192.168.0.179/cartazfacil/swift_email.php')
                logging.info(f'=================================================')
                logging.info(f'Processo 3 finalizado')
                url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
                ds = BotDiscordPlugin(urls=url, username="robo")
                ds.send_message(content='Cartaz finalizado!')

        else:
            logging.info(f'=================================================')
            logging.info(f'ERRO NO CARTAZFACIL')
            url = 'https://discord.com/api/webhooks/986238560904572988/pEfmDS_-Cvh6qJplwbwNpj3IvGjmtxqF9JXMVf7msI60ED2LXWQtoBCI44NSc-fn_B6E'
            ds = BotDiscordPlugin(urls=url, username="robo")
            ds.send_message(content=f'ERRO NO CARTAZFACIL')

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
