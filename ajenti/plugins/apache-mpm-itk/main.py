
import ajenti
from ajenti.api import *
from ajenti.plugins.webserver_common.api import WebserverPlugin
from reconfigure.configs import PasswdConfig

@plugin
class ApacheMpmItk (WebserverPlugin):
    inflate = 'apache-mpm-itk:main'
    service_name = 'apache2'
    service_buttons = [
        {
            'command': 'force-reload',
            'text': _('Reload'),
            'icon': 'step-forward',
        }
    ]
    hosts_available_dir = '/etc/apache2/sites-available'
    hosts_enabled_dir = '/etc/apache2/sites-enabled'

    template = """<VirtualHost *:80>
    ServerAdmin webmaster@localhost.my

    DocumentRoot /var/www

    <Directory />
            Options FollowSymLinks
            AllowOverride None
    </Directory>

    <Directory /var/www/>
            Options Indexes FollowSymLinks MultiViews
            AllowOverride None
            Order allow,deny
            allow from all
    </Directory>
</VirtualHost>
"""

    def init(self):

        self.title = 'Apache MPM ITK'
        self.category = _('Software')
        self.icon = 'globe'

        if ajenti.platform == 'centos':
            self.service_name = 'httpd'

        users_select = self.find('users')
        users_select.value = 'www-data'
        users = [x.name for x in PasswdConfig(path='/etc/passwd').load().tree.users]
        users_select.values = users_select.labels = users

