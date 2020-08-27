import sys

lineno = 0

title = ""
link = ""

outputs = []

for line in sys.stdin:    
    if lineno == 2:
        lineno = 0
        
    if "title:" in line:
        title = line.split("title:")[1].strip()
    
    if "link:" in line:
        link = line.split("link:")[1].strip()
        
    if lineno == 1:
        output = "- \"" + title + ": <a href=\\\"" + link + "\\\">" + link + "</a>\""
        outputs.append(output)
    
    lineno = lineno + 1
        
for output in outputs:
    print(output)