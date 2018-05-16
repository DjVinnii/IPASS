# Met config.py wordt de config.ini uitgelezen
# Mocht de config.ini niet aanwezig zijn wordt deze gemaakt in dezelfde map als main.py

import configparser
import os

# Globale variabelen maken
configfile_name = os.path.dirname(__file__) + '\config.ini'


# Deze functie maakt de configuratie file als deze nog niet bestaat
def make_config(configfile):
    cfgfile = open(configfile, 'w')

    parser = configparser.ConfigParser()
    parser.add_section('filelocations')
    parser.set('filelocations', 'logfolder', '')
    parser.set('filelocations', 'logfile', 'vsftpd.log')
    parser.write(cfgfile)
    cfgfile.close()


# Deze functie lees de configuratie file als deze al bestaat
def read_config(configfile):
    parser = configparser.ConfigParser()
    parser.read(configfile)
    log_folder = parser.get('filelocations', 'logfolder')
    log_file = parser.get('filelocations', 'logfile')
    return log_folder, log_file


def init_cfg():
    # Kijk of config.ini al bestaat of niet
    if not os.path.isfile(configfile_name):
        make_config(configfile_name)

    # config.ini waardes uitlezen en doorsturen
    log_folder, log_file = read_config(configfile_name)
    return log_folder, log_file

