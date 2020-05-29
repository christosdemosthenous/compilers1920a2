import re

def function(m): 
  if (m.group(0)=='&amp;'):
    return '&'
  
  elif (m.group(0)=='&gt;'):
    return '>'

  elif (m.group(0)=='&lt;'):
    return '<'

  else:
    return ' '	

   
rea1 = re.compile('<title>(.+?)</title>')	
rea2 = re.compile('<!--.*?-->',re.DOTALL)  
rea3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) 
rea4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) 
rea5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) 
rea5_2 = re.compile(r'<.+?/>',re.DOTALL) 
rea6 = re.compile(r'&(amp|gt|lt|nbsp);') 
rea7 = re.compile(r'\s+')


with open('steff.txt','r') as fp:

  a = fp.read() 
  m = rea1.search(a) 
  print(m.group(1))	
  a = rea2.sub(' ',a)
  a = rea3.sub(' ',a) 
  for m in rea4.finditer(a): 
    print('{}    {}'.format(m.group(1),m.group(2)))
  a = rea5_1.sub(' ',a) 
  a = rea5_2.sub(' ',a) 
  a = rea6.sub(function,a) 
  a = rea7.sub(' ',a) 
  print(a)
