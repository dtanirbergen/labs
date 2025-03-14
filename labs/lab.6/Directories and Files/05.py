filename = "0_txt_1.txt"
text = ("Изначально никто не живет на небесаx: ","ни ты, ни я, ни даже Бог.","Но скоро пустое место на небесном троне, которое так грустно видеть, будет занято." ,"Отныне я буду жить на небесах")
with open (filename, "w", encoding="utf-8") as file:
    for item in text:
      txt = file.write(item + "\n")