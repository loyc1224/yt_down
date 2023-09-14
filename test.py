import re

s ="jajjd      ogoaoa      \n \
jajgjgajj      "

selectName:str = re.sub(r'\s+', '', s)   

print(s)

print("out:"+selectName)