# -*- coding: utf-8 -*-
__author__ = 'pwust'
# Module reporting
# Version 
# (c) by Patric Wust (patric.wust@gmx.de) 10/2015

import os
import glob
import calendar
import time
import locale
import re
import shutil


def ask_date():
    """
    Will offer a printout of a monthly calendar covering the
    last 4 weeks, where this can be covering 1 or 2 months.
    Will then ask the user to supply a valid date.
    :return: the chosen date as struct_time
    """
    # todone part 2: ask for date ...done
    previousday = time.localtime(time.time() - 86400)
    previousmonth = time.localtime(time.mktime(previousday) - 86400 * 28)
    print()
    if previousmonth[1] != previousday[1]:
        left = calendar.month(previousmonth[0], previousmonth[1], 3).split('\n')
        right = calendar.month(previousday[0], previousday[1], 3).split('\n')
        for counter in range(len(left)):
            print('%-27s   |  %-27s' % (left[counter], right[counter]))
    else:
        calendar.prmonth(previousday[0], previousday[1], 3)
    print('Gestern war der %s.' % (time.strftime('%d.%m.%Y (%A)', previousday)))
    print()
    print('Für welchen Tag soll der Kassenabschluss nachgeholt oder erneut erstellt werden?')

    print('\tJahr       [%s]: ' % previousday[0], end='')
    try:
        myyear=int(input(''))
        # only use the last two digits of the year entry:
        myyear=myyear % 100 + 2000
    except:
        # invalid entry will default to previous day's year
        myyear=previousday[0]
    if myyear > previousday[0]:
        # make sure that year is not in the future
        myyear=previousday[0]

    print('\tMonat (1-12) [%s]: ' % previousday[1], end='')
    try:
        mymonth=int(input(''))
        # only use the last two digits of the month entry:
        mymonth=mymonth % 100
    except:
        # invalid entry will default to previous day's month
        mymonth=previousday[1]
    if mymonth > 12:
        # make sure that month is not beyond December
        myyear=previousday[1]

    print('\tTag   (1-31) [%s]: ' % previousday[2], end='')
    try:
        myday=int(input(''))
    except:
        # invalid entry will default to previous day
        myday=previousday[2]
    if mymonth > 31:
        # make sure that month is not too highr
        myday=previousday[2]

    # check if day is in the future:
    if (time.strptime(str(myday) + '.' + str(mymonth) + '.' + str(myyear), '%d.%m.%Y')) > time.localtime():
        # in the future, so reset to previous day:
        myyear, mymonth, myday = previousday[0], previousday[1], previousday[2]
    # final date to be selected:
    print('--> Es wird der %s.%s.%s ausgewertet.' % (myday, mymonth, myyear))

    return time.strptime(str(myday) + '.' + str(mymonth) + '.' + str(myyear), '%d.%m.%Y')


def read_inifile(mypath=os.path.curdir, myfile='kasse.ini'):
    """
    Will read from a MoccaSin INI file, and returns the settings as
    dictionary.
    The file shall contain comma-seperated lines of key and value,
    e.g. "KEY,VALUE".
    If there are duplicate keys, only the last one of a sequential
    read will be stored.
    Comments are ignored (lines starting with ';', '#', or '@')
    :param mypath: path to the INI file (defaults to current script dir)
    :param myfile: name of INI file (defaults to 'kasse.ini')
    :return: a dictionary with all settings from the file
    """
    # todone part 1: read settings ...done
    myconfig={}
    with open(os.path.join(mypath, myfile), 'r') as configfile:
        for line in configfile:
            myline = line.rstrip("\r\n\t ")
            if not (re.match('^(\s*|\s*[#;@]+.*)$',line)):
                key, value = [part.strip().lower() for part in myline.split(',', 1)]
                myconfig[key] = value

        return myconfig


def create_filename(date):
    """
    Check in bookings main directory, if the closing file of the
    requested date already exists.
    The file name patter for the closing file is 'k_13_10_04.mka',
    with 13 as year, 10 as month, and 04 as day of the closing.
    :param path: path to booking directory to be checked (usually
                 the configured temp1 of kasse.ini settings)
    :param date: date as struct_time requested
    :return: boolean True if the file is already there, False if not.
    """
    # todone part 3: check for existing closing ...done
    (yy, mm, dd) = convert_to_date_tuple(date)

    filename = 'k_' + yy + '_' + mm + '_' + dd + '.mka'

    return filename


def convert_to_date_tuple(date):
    """
    Converts a given struct_time to three two-letter strings,
    representing day, month, and year with two digits each.
    :param date: struct_time
    :return: (yy,mm,dd): a tuple of three 2-digit strings
    for year, month, and day
    """
    yy = str(date[0])[-2:]
    mm = str(date[1]).zfill(2)
    dd = str(date[2]).zfill(2)
    return (yy, mm, dd)


def show_closingsummary(file_with_path, spaces=0):
    """
    Show details about an existing POS closing file ('k_##_##_##.mka'):
     - number of receipts,
     - date and time of first and last receipt,
     - OS file date and time of last change,
     - total cash amount

    :param file_with_path: the full path and file name of the file
    :param tabs: if existing: shift output by # spaces
    :return: boolean if the file was in fact a closing file and could be examined
    """
    # todone part 4: show details from existing
    number_receipts = 0
    number_lines = 0
    number_cashlines = 0
    number_totals = 0
    number_orderlines = 0
    number_unclearlines = 0
    receipt_mintime = None
    receipt_maxtime = None
    sum_gross_sales = 0.0
    file_timestamp = time.localtime(os.stat(file_with_path).st_mtime)
    print(' ' * spaces, end='')
    print('Abschluss erstellt am %02d.%02d.%4d, %02d:%02d:%02d' % (file_timestamp[2], file_timestamp[1],
                                                                   file_timestamp[0], file_timestamp[3],
                                                                   file_timestamp[4], file_timestamp[5]))

    # Read file and parse all lines
    with open(file_with_path, 'r') as oldclosingfile:
        for line in oldclosingfile:
            number_lines += 1
            myline = line.rstrip("\r\n\t ")
            if myline[:16] == 'MOCCASIN-BUCHUNG':
                # This is the start line of a receipt
                # here we can find a timestamp
                # sample: 'MOCCASIN-BUCHUNG,000000000887053_131004074235.mcb'
                number_receipts += 1
                # 1st split: '000000000887053_131004074235.mcb'
                # 2nd split: '000000000887053_131004074235'
                # 3rd split: '131004074235'
                timestamp=time.strptime(myline.split(',')[1].split('.')[0].split('_')[1],'%y%m%d%H%M%S')

                if receipt_mintime == None or receipt_mintime > timestamp:
                    receipt_mintime = timestamp
                if receipt_maxtime == None or receipt_maxtime < timestamp:
                    receipt_maxtime = timestamp

            elif re.match('^[0-9]+:.*$', myline):
                # order line
                # Sample: '1: Latte Macchiato ohne Sirup to go;102200311401;2.80;Früh1;;;'
                number_orderlines += 1

            elif re.match('^(Gegeben|Zurück).*$', myline):
                # cash line
                # Sample: 'Gegeben;;;;20.00;;'
                # Sample: 'Zurück;;;;;13.80;'
                number_cashlines += 1

            elif re.match('^Summe.*', myline):
                # sum of a receipt
                # Sample: 'Summe;;;;;;6.20'
                number_totals += 1
                sum_gross_sales += round(float(myline.split(';')[6]),2)

            else:
                # unrecognized line
                number_unclearlines += 1
                print('%4s ??? UNKLAR: %s', (number_lines, myline))

        print(' ' * spaces, end='')
        print('%s Buchungen, %s Positionen, Bruttobetrag %.2f' % (number_receipts, number_orderlines, sum_gross_sales))
        if receipt_mintime != None:
            print(' ' * spaces, end='')
            print('erste Buchung:  %02d.%02d.%4d, %02d:%02d:%02d' %(receipt_mintime[2], receipt_mintime[1],
                                                                    receipt_mintime[0], receipt_mintime[3],
                                                                    receipt_mintime[4], receipt_mintime[5]))
            print(' ' * spaces, end='')
            print('letzte Buchung: %02d.%02d.%4d, %02d:%02d:%02d' %(receipt_maxtime[2], receipt_maxtime[1],
                                                                    receipt_maxtime[0], receipt_maxtime[3],
                                                                    receipt_maxtime[4], receipt_maxtime[5]))
        else:
            print(' ' * spaces, end='')
            print('??? EIN LEERER KASSENABSCHLUSS ???')


def compose_new_dayclosing(closingdate, mybookdir1, mybookdir2):
    """
    Create a new POS closing file for a given date in givien directories.
    The closing file must not exist, so take care to remove old versions first!
    The booking files that will be used need to live in mybookdir1, with the name pattern:
    '000000000887457_131004203413.mcb'
    -^^^^^^^^^^^^^^#_yymmddHHMMSS.mcb-
    The first part is a serial number, the second part is a complete datetimestamp in localtime.
    :param date: struct_time of the date for which a POS closing file shall be recreated
    :param mybookdir1: main directory where all booking files exist, and where closing will be saved to
    :param mybookdir2: backup directory where closing file will be copied to
    :return:
    """
    # tododone part 7: create new closing file from bookings
    # tododone part 8: save new closing to defined directories
    # todo With Moc outlet at Durlach, some closing files did not work at 10/2015 after having them created with this tool. This needs deep troubleshooting.
    # Progress bar:
    print('In Arbeit: ', end='')
    myprogresscolumn = 11

    myclosingfilename = create_filename(closingdate)
    (yy, mm, dd) = convert_to_date_tuple(closingdate)

    mypattern = '???????????????_' + yy + mm + dd + '??????.mcb'


    with open(os.path.join(mybookdir1, myclosingfilename), 'wt') as outfile:
        for receipt in glob.glob(os.path.join(mybookdir1, mypattern)):
            # print progress to console
            print('.', end='')
            myprogresscolumn += 1
            if myprogresscolumn > 80:
                print()
                myprogresscolumn = 0
            # print header
            outfile.write('MOCCASIN-BUCHUNG,')
            # print filename into header
            outfile.write(os.path.basename(receipt) + '\n')
            # print file contents
            with open(receipt, 'rt') as receipthandle:
                receiptcontents = receipthandle.read()
            outfile.write(receiptcontents + '\n')

    # progress bar finish
    print('!')

    # now copy the finished file to mybookingdir2:
    shutil.copy(os.path.join(mybookdir1, myclosingfilename),
                os.path.join(mybookdir2, myclosingfilename))


def main():
    """
    Recreate a day's closing file from POS module (KASSE),
    either because someone forgot to create it in time within
    POS module, or it needs to be recreated anyway.
    The user will be asked for a date. An existing closing will
    be shown with the option to recreate anyway.
    :return:
    """
    locale.setlocale(locale.LC_TIME, 'german')
    # myconf=read_inifile('c:\\private\\moc\\rit\\kasse', 'Kasse-python.ini')
    myconf=read_inifile('.', 'Kasse.ini')
    mybookdir1 = os.path.normpath(myconf['temp1'])
    mybookdir2 = os.path.normpath(myconf['temp2'])
    # print(mybookdir1)
    # print(mybookdir2)

    mydate = ask_date()
    #mydate = time.strptime('04.10.2013', '%d.%m.%Y')


    myclosingfile = create_filename(mydate)

    if os.path.isfile(os.path.join(mybookdir1, myclosingfile)):
        # closing file exists, so show details and ask how to proceed
        print()
        print('Die Datei %s ist schon da:' % myclosingfile)
        show_closingsummary(os.path.join(mybookdir1, myclosingfile), 4)

        # todone part 5: ask for overwriting
        print()
        myanswer = input('Möchten Sie den bestehenden Kassenabschluss überschreiben (j/n)? ').strip().lower()
        #print('>%s<' % tempinput)
        if  myanswer[:1] == 'j':
            # make backup of old file in mybookdir1
            # todone part 6: make backup
            # if name of backup already exists: delete it prior to renaming old closing file:
            if os.path.isfile(os.path.join(mybookdir1, myclosingfile + '-old')):
                os.remove(os.path.join(mybookdir1, myclosingfile + '-old'))
            os.rename(os.path.join(mybookdir1, myclosingfile), os.path.join(mybookdir1, myclosingfile + '-old'))
            # also remove existing file from backup dir:
            if os.path.isfile(os.path.join(mybookdir2, myclosingfile)):
                os.remove(os.path.join(mybookdir2, myclosingfile))

        else:
            # directly exit, as no new file will be created.
            print('--> Ok. Da die bestehende Datei nicht überschrieben werden soll, wird auch keine frische erstellt.')
            exit()

    # Either an existing closing file has been renamed to ...'-old', or
    # the closing file is not yet created, so do it!
    print('Ich erstelle die Datei %s neu...' % myclosingfile)

    compose_new_dayclosing(mydate, mybookdir1, mybookdir2)

    print('...fertig.')
    print('Daten des neu erstellen Kassenabschlusses:')
    show_closingsummary(os.path.join(mybookdir1, myclosingfile), 4)


if __name__ == '__main__':
    main()
