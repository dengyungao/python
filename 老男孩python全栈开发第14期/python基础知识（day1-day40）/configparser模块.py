import configparser
import os


config = configparser.ConfigParser()

config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11': 'yes'
                     }

config['bitbucket.org'] = {'User': 'hg'}

config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}

with open(os.path.dirname(__file__) + '/config/settings.ini', 'w',encoding="utf-8") as configfile:
	config.write(configfile)
	