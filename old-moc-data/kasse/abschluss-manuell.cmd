@echo off
:: TAGESABSCHLUSS DES KASSENPROGRAMMS NACHHOLEN
:: --------------------------------------------------------------------
:: (Muster einer Buchungsdatei = 000000000311800_151024172733.mcb)
:: Um einen Kassen-Tagesabschluss manuell nachzuholen, dieses Skript 
:: bitte im Ordner .\KASSE der Kasse ausführen.
:: 
:: Parameter: #1 = Jahr (00), #2 = Monat (00), #3 = Tag (00)
:: Eingabe: Unterverzeichnis .\temp1\ mit den Buchungsdateien
:: Ausgabe: Unterverzeichnis .\temp1\ und .\temp2\ für die ".mka"-Datei
::
:: (c) Patric Wust 10/2015 für MoccaSin = SüdWest Kaffee GmbH, Karlsruhe
::

if "%3" == "" goto NOARGS
set JAHR2=%1
set MONAT2=%2
set TAG2=%3

if exist temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka copy temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka-sik
if exist temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka del temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka
for /f %%a in ('dir /b temp1\000000?????????_%JAHR2%%MONAT2%%TAG2%??????.mcb') do (echo MOCCASIN-BUCHUNG,%%a & type temp1\%%a & echo.)>>temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka
copy temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka temp2\k_%JAHR2%_%MONAT2%_%TAG2%.mka


goto EOF

:NOARGS
echo Zu wenig Parameter uebergeben, schade...
echo.
echo Aufruf: %0% JJ MM TT
echo   wobei JJ = Jahr  (zweistellig) fuer den Abschlusstag, z.B. 15 fuer 2015,
echo         MM = Monat (zweistellig), z.B. 09 fuer September,
echo         ZZ = Tag   (zweistellig), z.B. 01 fuer den ersten Tag eines Monats.
echo.
:EOF