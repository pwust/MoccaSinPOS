# -*- coding: utf-8 -*-

from string import Template

def antwort_anfang(antw="text/html"):
    return('Content-type: ' + antw + ';charset: utf-8\n\n')

def seitenanfang(titel):
    with open('templates/header.html') as header_d:
        h_text = header_d.read()
    header = Template(h_text)
    return(header.substitute(title=titel))

def seitenende(links):
    with open('templates/footer.html') as footer_d:
        f_text = footer_d.read()
    link_string = ''
    for schlüssel in links:
        link_string += '<a href="' + links[schlüssel] + '">' + schlüssel + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(f_text)
    return(footer.substitute(links=link_string))

def form_anfang(die_url, form_typ="POST"):
    return('<form action="' + die_url + '" method="' + form_typ + '">')

def form_ende(submit_text="Absenden"):
    return('<p></p><input type=submit value="' + submit_text + '"/></form>')

def radio_button(rb_name, rb_wert):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_wert + '"> ' + rb_wert + '</input><br />')

def u_liste(l_elemente):
    u_string = '<ul>'
    for l_element in l_elemente:
        u_string += '<li>' + l_element + '</li>'
    u_string += '</ul>'
    return(u_string)

def heading(h_text, h_ebene=2):
    return('<h' + str(h_ebene) + '>' + h_text +
           '</h' + str(h_ebene) + '>')

def para(p_text):
    return('<p>' + p_text + '</p>') 
