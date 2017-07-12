import string
master = "26_05_17_top_100_extended.html" #Name of English master template
f = open(master) 
text = f.read()
list_of_words = ['en_','ire_','scan_','usa_','can_','aus_','asia_','row_','es_','fr_','de_','it_','ru_','ja_']
num =2
filename = f 
for word in list_of_words:
    new_text = string.replace(text,"en_",word)
    f_new = open(str(word)+str(master),"w")
    f_new.write(new_text)
    f_new.close()
    num +=1