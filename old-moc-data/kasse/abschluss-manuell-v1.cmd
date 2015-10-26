::@echo off
:: ABSCHLUSSDATEI NACHHOEN
:: (Muster eines Buchungsdateinamens = 000000000311800_151024172733.mcb)
:: Um einen Kassen-Tagesabschluss manuell nachzuholen, dieses Skript 
:: bitte im Ordner "temp1" der Kasse ausführen.
:: Vorher bitte in den drei Zeilen unten Jahr, Monat, und Tag jeweils 
:: zweistellig anpassen (01 für Januar, 01 für den ersten des Monats)!
:: Patric Wust 10/2015
::
set JAHR2=15
set MONAT2=10
set TAG2=24

copy temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka-sik
del temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka
for /f %%a in ('dir /b temp1\000000?????????_%JAHR2%%MONAT2%%TAG2%??????.mcb') do (echo MOCCASIN-BUCHUNG,%%a & type temp1\%%a & echo.)>>temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka
copy temp1\k_%JAHR2%_%MONAT2%_%TAG2%.mka temp2\k_%JAHR2%_%MONAT2%_%TAG2%.mka
