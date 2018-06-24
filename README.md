# IPASS

## Getting Started

### Vereisten

Dit script is geschreven in python 3.6, het is verstandig om deze versie ook te gebruiken om het script te draaien.
Ouddere versiesv van python 3 zouden ook kunnen werken, maar deze kunnen instabiel zijn. ***Let op: dit script werkt niet met python 2***

### Installeren

1. Allereerst moet het script gedownload worden. Dit kan in een folder naar wens geplaats worden.
2. Als tweede moet het configuratie bestand aangemaakt worden. Dit gebeurt automatisch bij het starten van het script. het script kan gestart worden met het volgende commando:
```
python main.py
```
Als ook python 2 geïnstalleerd is, moet specifiek python 3 aangeroepen. Dit kan als volgt:
```
python3 main.py
```
3. Nadat het configuratie bestand aangemaakt is, kan deze naar wens aangepast worden. Dit configuratie bestand (config.ini) is te vinden in de zelfde map als de twee python scripts. <br><br>
In config.ini zijn er 3 dingen die aangepast kunnen worden:
<br>- logfolder : Dit is het pad naar de map waar het logbestand staat.
<br>- logfile: Dit is de naam met bestandsextentie van het logbestand.
<br>- exportfolder: Dit is de locatie waar de exports heen worden geschreven.
4. Als laatste kan je weer main.py draaien en gebruik maken van het script.

### Gebruik

Dit script kan op twee verschillende manieren gebruikt worden: met input van de gebruiker, of geautomatiseerd. <br><br>
Om als gebruker gebruik te maken van het script kan je het script draaien zoals eerder beschreven bij **Installeren**.

Om het script geautomatiseerd te kunnen draaien kan het script aangeroepen worden met parameters. Momenteel zijn er nog 2 parameters die meegegeven kunnen worden: -f en -t.<br><br>
Met -f is het mogelijk om de mislukte downloads uit te lezen en met -t is het mogelijk om de top 10 van de gedownloadde bestanden uit te lezen. Het is mogelijk om zowel 1 of beide parameters mee te geven.<br><br>

Wanneer je het script met parameters wilt draaien kan dat met het volgende commando:

Beide parameters:
```
python3 main.py -f -t
```
Alleen misluke downloads:
```
python3 main.py -f
```
Alleen top 10 downloads:
```
python3 main.py -t
```
Hier is het dus mogelijk om alleen -f, alleen -t of beiden te gebruiken.<br><br>

Na het draaien van het script staan er in de exportfolder tekst bestanden met de output, zodat deze ook terug te zien zijn na het automatisch draaien van het script. Wanneer er geen exportfolder is gedefinïeeerd, is deze te vinden in de zelfde map als het script.

## Auteur

* **Vincent Kling**
