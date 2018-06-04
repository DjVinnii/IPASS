# Importsimport osfrom collections import Counterimport configimport sysimport datetime# Globale variabelen makenlogfolder, logfile, exportfolder = config.init_cfg()if logfolder == "":    path = logfileelse:    path = str(logfolder) + '\\' + logfile# Functie voor het openen van het logbestanddef open_log(log_path):    # Try-Except voor de foutafhandeling wanneer een bestand niet bestaat    try:        # Openen van log        file_in = open(log_path, 'r')        # Regels van log lezen        lines = file_in.readlines()        # Log sluiten        file_in.close()        return lines    except FileNotFoundError:        # Foutmelding wanneer het niet lukt om het bestand te openen        print('FOUT: Bestand of pad bestaat niet!\nHuidig bestandspad: ' + log_path + '\nControleer config.ini')        input('Druk op een toets om terug te gaan naar het menu...')        clear()        menu()# Functie voor het vinden van de bestandsnaam in de logdef get_filename(line):    first_comma = line.index(',')    second_comma = line.index(',', first_comma + 1)    filename = line[first_comma+3:second_comma-1]    return filename# Functie voor het uitlezen van de log en hier de Top 10 of de mislukte downloads van te makendef read_log(log_path, action):    try:        # Openen van log        lines = open_log(log_path)        # Aanmaken van lijst        file_list = []        if action == "fail":            # Mislukte downloads            # Openen van export met gebruik van de datum en tijd om zo de log eenvoudig terug te vinden            file_out = open(exportfolder + "\Fail - " + str(datetime.datetime.now().strftime("%Y%m%d-%H%M")) + ".txt", "w")            # Eerste regel printen            print('Mislukte downloads:\n\n')            file_out.write('Mislukte downloads:\n\n')            # Iedere mislukte download printen            for line in lines:                if 'FAIL DOWNLOAD' in line:                    file = get_filename(line)                    # print(file)                    # file_out.write(file + "\n")                    file_list.append(file)            # Getelde lijst maken            counted_file_list = Counter(file_list)            # Lijst printen            for k, v in counted_file_list.items():                print(k + " (" + str(v) + " pogingen)")                file_out.write(k + " (" + str(v) + " pogingen)\n")        elif action == "top":            # Top 10            # Openen van export met gebruik van de datum en tijd om zo de log eenvoudig terug te vinden            file_out = open(exportfolder + "\Top - " + str(datetime.datetime.now().strftime("%Y%m%d-%H%M")) + ".txt", "w")            # Eerste regel printen            print('Top 10 downloads:\n\n')            file_out.write('Top 10 downloads:\n\n')            # Iedere gelukte download toevogen in de lijst            for line in lines:                if 'OK DOWNLOAD' in line:                    file = get_filename(line)                    file_list.append(file)            # Top 10 maken van de lijst            counted_file_list = Counter(file_list)            counted_file_list = counted_file_list.most_common(10)            loop_count = 1            # Top 10 printen            for counted_file_item in counted_file_list:                print(str(loop_count) + ": " + counted_file_item[0] + " (" + str(counted_file_item[1]) + " downloads)")                file_out.write(str(loop_count) + ": " + counted_file_item[0] + " (" + str(counted_file_item[1]) + " downloads)\n")                loop_count += 1        # Export sluiten        file_out.close()    # Foutafhandeling    except TypeError:        print('Uitlezen niet gelukt\n')    except FileNotFoundError:        print('FOUT: Exportfolder niet gevonden!\nHuidig bestandspad: ' + exportfolder + '\nControleer config.ini')# Functie voor het maken van het menudef menu():    print('Imteq FTP\n\nMaak een keuze:\n1: Lijst met mislukte downloads\n2: Top 10 gedownloadde bestanden\n0: Afsluiten')    menu_choice = input()    clear()    # Input van menu afhandelen    if menu_choice == '1':        # Mislukte downloads        read_log(path, "fail")        input('Druk op een toets om terug te gaan naar het menu...')        clear()        menu()    elif menu_choice == '2':        # Top 10 downloads        read_log(path, "top")        input('Druk op een toets om terug te gaan naar het menu...')        clear()        menu()    elif menu_choice == '0':        # Exit        exit()    else:        # Foute invoer        print('FOUT: Incorrecte invoer!')        input('Druk op een toets om terug te gaan naar het menu...')        clear()        menu()# Functie voor het legen van de CLIdef clear():    # voor het legen van de CLI wordt hiet een commando uitgevoerd op basis van het OS    osname = os.name    # Windows    if osname == 'nt':        os.system('cls')    # Linux    elif osname == 'posix':        os.system('clear')    # Anti Error    else:        print('\n' * 30)# Arguments afhandelen voor automatisering van het scriptif len(sys.argv) > 1:    # Eerste keer loopen om onjuiste argumenten er uit te halen    for arg in sys.argv[1:]:        if (arg != '-f') and (arg != '-t'):            print('Onjuist argument: ' + arg + '\nGebruik -f voor het exporteren van een lijst met de mislukte downloads\nGebruik -t voor het exporteren van een lijst met de top 10 gedownloadde bestanden')            sys.exit()    # Tweede keer loopen om argumenten af te handelen    for arg in sys.argv[1:]:        if arg == '-f':            # Mislukte bestanden exporteren            read_log(path, "fail")        elif arg == '-t':            # Top 10 exporteren            read_log(path, "top")# Zonder argumenten menu aanroepenelse:    # Eerste keer aanroepen van het menu    clear()    menu()