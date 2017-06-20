import jinja2

banner = '''banner exec ^
********************************************************
*                                                      *
* {{ '%-15s' % modell }} {{ '%-36s' % adresszeile_1 }} *
*                 {{ '%-36s' % adresszeile_2 }} *
*                                                      *
********************************************************
*                                                      *
*                 Hostname: $(hostname).$(domain)         *
*                 Line: $(line)                              *
*                                                      *
********************************************************
^
banner login ^
********************************************************
*   Access to this system may be logged for quality    *
*          monitoring and security purposes.           *
*       UNAUTHORIZED ACCESS STRICTLY PROHIBITED        *
********************************************************
^'''

banner_template = jinja2.Template(banner)
print(banner_template.render(adresszeile_1='Oberseestrasse 10', adresszeile_2='8640 Rapperswil', modell='c2960-8PC'))
