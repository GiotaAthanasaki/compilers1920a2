import re 

#Κανονικές εκφράσεις άσκησης
#Εξαγωγή και εκτύπωση του τίτλου
rexp1 = re.compile(r'<title>(.+?)</title>')

#Απαλοιφή των σχολίων
rexp2 = re.compile(r'<!--.*?-->',re.DOTALL) 

#Απαλοιφή script & style σε μία κανονική έκφραση
rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL)

#Απαλοιφή  script
#pscript=(r'<script(.*?)</script>',re.DOTALL)
#Απαλοιφή  style
#pstyle=(r'<style(.*?)</style>',re.DOTALL)

#href
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) 

#Απαλοιφή των tags
rexp5 = re.compile(r'<.+?>|</.+?>',re.DOTALL) #Απαλοιφή tags με διπλή μορφή
rexp5x = re.compile(r'<.+?/>',re.DOTALL) #Απαλοιφή tags με μονή μορφή

#html 
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);')

#whitespace
rexp7 = re.compile(r'\s+') 

#Μετατροπή html entities
def cb(m):
  if(m.group(0)=='&amp;'):
    return '&'
  elif (m.group(0)=='&gt;'):
    return '>'
  elif (m.group(0)=='&lt;'):
    return '<'
  elif (m.group(0)=='&nbsp;'):
    return ' '

#Άνοιγμα html αρχείου από windows, testpage.txt είναι το κείμενο εισόδου
with open('testpage.txt','r',encoding='utf-8') as fp: 
  text = fp.read()

  m = rexp1.search(text) 
  print(m.group(1)) 

  text = rexp2.sub(' ',text) 
  text = rexp3.sub(' ',text) 
  
#Έξοδος προγράμματος
  for m in rexp4.finditer(text): 
    print('{} {}'.format(m.group(1),m.group(2)))

  text = rexp5.sub(' ',text) 
  text = rexp5x.sub(' ',text) 
  text = rexp6.sub(cb,text) 
  text = rexp7.sub(' ',text) 

  print(text)
