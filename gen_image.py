
import datetime, locale, tempfile, subprocess, sys, os

def generate_imgblue(valores):
  locale.setlocale(locale.LC_TIME, "es_AR.UTF-8")

  with open('out.html', 'wb') as o:
    with open('template.html') as f:
      template = f.read()

      for v in valores:
        buy = str(v['values'][0])
        sell = str(v['values'][1])
        template = template.replace('%%%s_Compra%%' % v['name'], buy)
        template = template.replace('%%%s_Venta%%' % v['name'], sell)

      template = template.replace('%FECHA%', datetime.datetime.now().strftime('%c'))
      o.write(template)
      o.flush()

  subprocess.call(['wkhtmltoimage', '--width', '504', 'out.html', os.path.join('out', 'facebook.png')])
  subprocess.call(['wkhtmltoimage', '--width', '528', 'out.html', os.path.join('out', 'twitter.png')])
  subprocess.call(['wkhtmltoimage', '--width', '960', '--height', '720', 'out.html', os.path.join('out', 'instagram.png')])

generate_imgblue([
  {'name':'Blue', 'values':sys.argv[1:3]},
  {'name':'Oficial', 'values':sys.argv[3:5]}
  ])
