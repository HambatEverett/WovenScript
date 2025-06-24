# last updated:
# 6/23/25
thefile = input("What file?")

script = open(thefile,"r")

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_ansi(r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m"

def hex_to_ansi(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    return rgb_to_ansi(r, g, b)

def tokenize():
  eachlines = script.readlines()
  script.close()
  linelist = []
  position = []
    
  # tokenize
  
  for line in eachlines:
    line = line.strip().replace("$",";").split(";")
    if line[0] == '':
      linelist.append(["NEWLINE"])
    else:
      linelist.append(line)
  return linelist

def exec(tokens):
  #define values and lists
  
  variables = {}

  #define the weaves
  
  def varmake(where):
    name = tokens[where][1].strip()
    value = tokens[where][2].strip()
    variables[name] = value
  
  def out(where):
    check = where+1
    color = "\033[0;37m"
    
    if tokens[check][0] == "text":
      text = tokens[check][1]
    elif tokens[check][0] == "var":
      name = tokens[check][1]
      text = variables[name]
    else: 
      print("Error in line: ",check,", invalid syntax. Did you mean: [text] or [var] ?")
      text = "nil"
    
    if tokens[check+1][0] == "color":
      color = tokens[check+1][1]
      color = hex_to_ansi(color)
    print(color+text.strip())

  #actually exec
    
  for place,token in enumerate(tokens):
    if token[0] == "out":
      out(place)
    elif token[0] == "variable":
      varmake(place)
    elif token[0] == "NEWLINE":
      pass
    elif token[0] == "text":
      pass
    elif token[0] == "color":
      pass
    elif token[0] == "var":
      pass
    else:
      print("Error in line:",place+1,".")
      break
  

tokenized = tokenize()
#print(tokenized)

#for token in tokenized:
#  print(token)
exec(tokenized)
