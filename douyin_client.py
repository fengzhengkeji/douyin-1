# -*- coding: UTF-8 -*-
import requests
import base64
import json

decurl = "http://133.130.98.90/douyin/decrypt"
encurl = "http://133.130.98.90/douyin/encrypt"

ciphetext = "dGMCED3Yv+yCXAl8DwLqRjt4j1AHsA7OlBVwiC+tzI4o269csyj4kw8nt15XOj6O4u9aBE8wRpdvnYe3BU3qN3o+A128SteAt0p7vaLLcoXj1NcTck0E2ctZY/9BCiwyZt0Ux3BwMRkTr0UUodmRddlwoI+ogs2lqniqocYjCbkSUp6oQVWAgiFL6y++hP3QeS3MTXZcOyoHJ36MTs2PHZFn2ADrJVFFlhJ5qjLRWY2uIceTrkG3Ml0N5BMnEHEAKuPfi/HkMhj7TeV2R6xDgVQQsESHMnPJZykIdl/VkoSQ7cbfGMKVcgg1w9EvU+JJXSYT4nWBnrJy1EYY/24u8aDFKvNsz0meurH+X7FRp827IbVfrwq3HlGVmkhbDBHT4kMvZwZsf1IjssKvi7hbF2Qp9BLn5HtPHMA2ud/89/nLFPmXqgTpHZ45Tu1UNuW0rXET9+Q8Jb4lBkIu+DunDtge98A3bp6t3SoZcPSbu9KGVDiTDirWYLv9hvLofBiBHNPBBR1mBBXPAJEvaYeYY9tgvUJHGaEPEfBIErd14g3I3yLTSCvVwJP3oeyKuMJTmA6Os7t/yrNxUk1d8nkN0zLoEVMAtfEVtyTf0j3aPUrwrPLHjjefzvIW+g/sKUGgDqMoG3AziInxK5CwxuI8woxqGIpXpY54CAcpwq5gG7qqz52rswlztrHj/E2AY9NQQ413RI/j7wUzr/ZroBn3wIE1kiMa0Xf32Vnc95GSqXXm1a3IFhUcq7AgrlXu/bLSqxeXRbcSyQxvgh59y/d01DuZUFA+z+wWOr77VT48jn/02QAlBKVeCJxiLkltnN1KhtbcSkRbw2/vqtKmea9LOVgw+BhNVuT8IBJ9oGI68DAq3BO74Xjet2eq1NPzDsFe70UDiPO2Yh9Co5xQx8edUGop/oUV29BN+pZgOTgYW6EiqaCUvcopsQwdIE5kxqQ4XA9ke123YmJO4C0eHLT3OsO9xZw="
r = requests.post(decurl, data=ciphetext)
plaintext = r.text
print(u"解密结果:")
print(plaintext)

r = requests.post(encurl, data= base64.b64encode(r.content))
print(u"加密结果:")
print(r.text)

