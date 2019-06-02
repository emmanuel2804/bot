<!-- # Telegram Bot for learn the API 


# Free Hosting
# See: 

https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=2ahUKEwi1hvvRtd_hAhVLXq0KHeFtDZoQwqsBMAN6BAgJEAc&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DO0MAWtbg34g&usg=AOvVaw3FeATtkl7BCkDLBn3Dw36s

# or: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots


# hosten on: https://www.pythonanywhere.com
             -->

# <p align="center">Proyecto de Modelos de Optimizacion II

<p align="center">Simple juego que funciona como un bot de Telegram, que utiliza la <a href="https://core.telegram.org/bots/api">API</a> de este, a través del módulo <a href="https://pypi.python.org/pypi/pyTelegramBotAPI">pyTelegramBotAPI</a>. Inpirado en el juego <a href="https://t.me/chtwrsbot">Chat Wars</a>

  * [Instalar pyTelegramBotAPI](#instalar-pyTelegramBotAPI)
  * [Ejecutar el bot](#ejecutar-el-bot)
    * [Acceder al bot](#acceder-al-bot)

## Instalar pyTelegramBotAPI.

Esta API fue probada con Python 2.6, 2.7, 3.4, Pypy y Pypy 3.
Existen dos formas de instalar la librería.

* Instalación usando pip (un administrador de paquetes de Python)

```
$ pip install pyTelegramBotAPI
```
* Instalación desde el código fuente (se requiere git)

```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install
```

<!-- It is generally recommended to use the first option. -->
Generalmente se recomienda usar la primera opción

<!-- **While the API is production-ready, it is still under development and it has regular updates, do not forget to update it regularly by calling `pip install pytelegrambotapi --upgrade`* -->

**Si bien la API está lista para la producción, todavía está en desarollo y tiene actualizaciones periódicas, no olvide actualizarla regularmente ejecutando `pip install pytelegrambotapi --upgrade`*

## Ejecutar el bot.

Para iniciar el bot solo es necesario ejecutar el siguiente código: 

``` bash
$ python3 init.py
```

### Proxy

Si necesita el uso de un proxy, acceda al archivo `proxy.json` y llene los campos con la información correcta. Para iniciar el bot cuando está usando un proxy ejecute el comando:

``` bash
$ python3 init.py --proxy
```

### Acceder al bot.

Para acceder al bot es necesario iniciar una cuenta de Telegram, ya sea en su versión <a href="https://web.telegram.org">web</a> o desde la aplicación para teléfonos móviles. Una vez dentro podemos acceder al bot por su <a href="https://t.me/LemasFirstBot">link</a> o por su alias @LemasFirstBot