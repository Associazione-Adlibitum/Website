#!/usr/bin/env python3

import cherrypy
from jinja2 import Environment, FileSystemLoader
from datetime import date

templ = Environment(loader=FileSystemLoader('templates')).get_template(
        'website.html')
current_year = date.today().year

def menu(active=0):
    items = [
    ('index.html', 'Home page', 'Home'),
    ('chi_siamo.html', "Origine, finalità e statuto dell'associazione", 'Chi siamo'),
    ('scuola.html', 'La scuola di musica e le sue attività', 'La scuola'),
    ('news.html', 'I prossimi eventi', 'News'),
    ('contatti.html', 'Indirizzo, mappa, telefono, e-mail', 'Contatti')
    ]
    html = ''
    counter = 0
    for i in items:
        if active == counter:
            html += '\t\t\t\t\t<li id="active_item">{}</li>'.format(i[2])
        else:
            html += '\t\t\t\t\t<li><a href="{}" title="{}">{}</a></li>'.format(i[0], i[1], i[2])
        if counter + 1 < len(items):
            html += '\n'
        counter += 1
    return html

class AdLibitum(object):
    @cherrypy.expose
    def index(self):
        return templ.render(
                subtitle='Home',
                description="Sito ufficiale dell'Associazione Ad libitum di Renate e della sua scuola di musica.",
                menu=menu(0),
                content=open('content/index.html').read()[:-1], # removing the last newline
                year=current_year
                )

    @cherrypy.expose
    def about(self):
        return "Chi siamo"

    @cherrypy.expose
    def scuola(self):
        return "La scuola"

    @cherrypy.expose
    def news(self):
        return "News"

    @cherrypy.expose
    def contatti(self):
        return "Contatti"

    @cherrypy.expose
    def credits(self):
        return "Credits"

if __name__ == '__main__':
    cherrypy.quickstart(AdLibitum())
