import config# Globale variabelen makenlogfolder = config.init_cfg()logfile = 'vsftpd.log'if logfolder == "":    path = logfileelse:    path = str(logfolder) + '\\' + logfiledef read_log(log_path):    errors = {}    file_in = open(log_path, 'r')    lines = file_in.readlines()    file_in.close()    for line in lines:        if 'FAIL DOWNLOAD' in line:            print(line)read_log(path)