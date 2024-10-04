# In terminal: python3 -m pip install pywhatkit
import pywhatkit

mobile_num= "+46 723873597"
msg= "Malvavisca"

pywhatkit.sendwhatmsg_instantly(mobile_num, msg, 15)
#(mobile_num,msg, 16,45,30)