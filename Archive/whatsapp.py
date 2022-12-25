import pywhatkit

phone_number = '+16477725807'
message = 'hey, its me Nick'

hour = 1
minute = 13

pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
