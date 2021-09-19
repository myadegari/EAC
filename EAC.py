import re
import pyperclip
import os

out_file = open("temp_out.txt","w")
cra = []
with open ("temp.txt","r",encoding='utf8',errors='replace') as f:
    contents = f.readlines()
    for content in contents:
        content=re.sub(r'\ufb02','fl',content)
        content=re.sub(r'\ufb01','fi',content)
        content=re.sub(r'\u2192','->',content)
        content=re.sub(r'\u2208','in',content)
        content=re.sub(r'\u221a','sqrt ',content)
        content=re.sub(r'\u2212',' - ',content)
        content=re.sub(r'\u223c',' ~ ',content)
        content=re.sub(r'\ufffe','',content)
        cons = re.findall(r"[A-Z]+\.\s*[A-Z]|[\s]{3}|[1-9]+\)\s+[A-Z]",content)
        if cons != cra:
            content = re.sub(cons[0][0],"\n"+cons[0][0],content)
            out_file.write(content)
        else:
            if re.match("•",content):
                content_new = re.sub("•","\n"+"*-*",content)
            else:
                content_new = re.sub(r"[\n]+"," ",content)
            out_file.write(content_new)

out_file.close()
with open("temp_out.txt","r") as f:
    content = f.read()
    
    pyperclip.copy(content)

os.remove("temp_out.txt")
