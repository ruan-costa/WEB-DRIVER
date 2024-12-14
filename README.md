'''Automação de Download de Bases Simplic - Módulo webdriver.py




O módulo webdriver.py gerencia a instância do WebDriver do navegador Google Chrome, configurando-o de forma programática com a biblioteca Selenium. Ele permite ajustar preferências como o diretório de download e a opção de executar o navegador em modo headless (sem interface gráfica). Além disso, utiliza o pacote webdriver_manager para gerenciar automaticamente a versão correta do driver.

🚀 Funcionalidades

Gerenciamento do WebDriver: Configura automaticamente o WebDriver com opções personalizadas.

Execução Headless: Permite a execução do navegador sem interface gráfica.

Persistência de Configurações: Suporte a perfis do navegador para evitar a repetição de logins e CAPTCHAs.


📋 Uso

Exemplo de Importação e Uso:

# Importa a classe Driver do módulo webdriver.py
from webdriver import Driver

# Instancia o driver com configurações personalizadas
# Exemplo: Executar em modo headless e salvar downloads no diretório especificado
my_driver = Driver(headless=True, dir_dwld="/caminho/para/downloads")

# Obtém a instância configurada do WebDriver
driver = my_driver.driver

# Usando o driver para acessar um site
driver.get("https://www.google.com")

# Fechando o navegador ao final
driver.quit()

📂 Estrutura do Projeto

Abaixo está um exemplo da estrutura de pastas e arquivos deste projeto:


├── webdriver.py                # Script para gerenciamento do WebDriver  
├── profilenavegador/           # Pasta que armazena o perfil do navegador (não deve ser apagada)  
└── README.md                   # Este arquivo README  

📝 Detalhes do Arquivo webdriver.py

Classe Driver: Encapsula a lógica de criação e configuração do WebDriver.

Atributos:

headless (bool): Define se o navegador será executado sem interface gráfica. Útil para ambientes de produção.

dir_dwld (str): Define o caminho para salvar os arquivos baixados.

_driver: Instância do WebDriver, inicializada ao acessar a propriedade driver.

Métodos:

setup(): Configura e retorna o WebDriver com as opções necessárias.

driver: Propriedade que retorna o WebDriver já inicializado. Se ainda não existir uma instância, ele chama setup().

Integração: O módulo pode ser usado em scripts como baixar_bases_simplic.py para facilitar o login automático e a manipulação de páginas.

⚠️ Observações Importantes

Primeira Execução: Ao iniciar a aplicação pela primeira vez, execute o módulo baixar_bases_simplic.py e descomente as linhas relacionadas ao login. Resolva o CAPTCHA manualmente para salvar as informações de sessão na pasta profilenavegador. Após isso, comente novamente as linhas de login.

Pasta profilenavegador: Não delete esta pasta. Ela contém informações de cookies e sessões salvas, evitando a necessidade de resolver CAPTCHAs em futuras execuções.



📧 Contato

Se tiver dúvidas, entre em contato:

Email: ruan.xxx1@gmail.com
Tel: 81 9918-44940
'''


