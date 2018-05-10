# Met config.py wordt de config.ini uitgelezen
# Mocht de config.ini niet aanwezig zijn wordt deze gemaakt in dezelfde map als main.py

import configparser
import os

# Globale variabelen maken
configfile_name = 'config.ini'

# Deze functie maakt de configuratie file als deze nog niet bestaat
def make_config(configfile):
    cfgfile = open(configfile, 'w')

    parser = configparser.ConfigParser()
    parser.add_section('filelocations')
    parser.set('filelocations', 'logfolder', '')
    parser.write(cfgfile)
    cfgfile.close()


# Deze functie lees de configuratie file als deze al bestaat
def read_config(configfile):
    parser = configparser.ConfigParser()
    parser.read(configfile)
    log_folder = parser.get('filelocations', 'logfolder')
    return log_folder

def init_cfg():
    # Kijk of config.ini al bestaat
    if os.path.isfile(configfile_name):
        # config.ini bestaat, dus lees deze uit
        log_folder = read_config(configfile_name)
        return log_folder

    else:
        # config.ini bestaat niet, dus maak deze en lees deze daarna uit
        make_config(configfile_name)
        log_folder = read_config(configfile_name)
        return log_folder

