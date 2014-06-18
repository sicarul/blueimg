
import datetime, locale, tempfile, subprocess, sys, os

def generate_imgblue(valores):
  locale.setlocale(locale.LC_TIME, "es_AR.UTF-8")
  
  with open('out.html', 'wb') as o:
    with open('template.html') as f:
      template = f.read()

      for v in valores:
        template = template.replace('%%%s_Compra%%' % v['name'], str(v['values'][0]))
        template = template.replace('%%%s_Venta%%' % v['name'], str(v['values'][1]))

      template = template.replace('%FECHA%', datetime.datetime.now().strftime('%c'))
      o.write(template)
      o.flush()
  
  subprocess.call(['wkhtmltoimage', '--width', '504', 'out.html', os.path.join('out', 'facebook.png')])
  subprocess.call(['wkhtmltoimage', '--width', '440', 'out.html', os.path.join('out', 'twitter.png')])

generate_imgblue([
  {'name':'Blue', 'values':sys.argv[1:3]},
  {'name':'Oficial', 'values':sys.argv[3:5]},
  {'name':'Ahorro', 'values':sys.argv[5:7]},
  {'name':'Tarjeta', 'values':sys.argv[7:9]}
  ])
