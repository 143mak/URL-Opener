from tkinter import *
from tkcalendar import DateEntry
from datetime import date,datetime,timedelta
from PIL import Image, ImageTk
import webbrowser
from ttkwidgets.autocomplete import AutocompleteEntry

win=Tk()

#bodystructure
win.title("URL OPENER")
win.maxsize(width=550,height=400)
win.minsize(width=550,height=400)

photo = PhotoImage(file ="logo.png")
win.iconphoto(False, photo)

img =Image.open("spicejet.jpg")
bg = ImageTk.PhotoImage(img)

label = Label(win, image=bg)
label.place(x = -500,y = -500)



#--------------------------------sectors to be filled---------------------------------------------------------------

paytmsectors=['JAI-Jaipur','CCU-Kolkata','DHM-Dharamsala','IXY-Kandla',
              'PNQ-Pune','MAA-Chennai','CGP-Chittogram','DXB-Dubai',
              'IXB-Bagdogra','PAT-Patna','IXG-Belgavi','GWL-Gwalior',
              'GOI-Goa','DEL-Delhi','DED-Dehradun','RAJ-Rajkot','KBK-Khushinagar',
              'ISK-Nashik','HJR-Khajurao','SAG-Shirdi','GAU-Guwahati','PYG-Pakyong',
              'TIR-Tirupati','DAC-Dhaka','IXM-Madurai','BOM-Mumbai','IXE-Manglore',
              'UDR-Udaipur','RDP-Durgapur','IXS-Silchar','SXR-Srinagar','HYD-Hyderabad',
              'STV-Surat','JRG-Jharsuguda','VNS-Varanasi','DBR-Darbanga','PNY-Pondicherry',
              'KNU-Kanpur','IXZ-Port Blair','TRV-Trivandrum','JDH-Jodhpur','JLR-Jabalpur',
              'IXJ-Jammu','JSA-Jaisalmer','ATQ-Amritsar','GOP-Gorakhpur','IXL-Leh',
              'KQH-Kishangarh','PBD-Porbandar','RUH-Riyadh','COK-Kochi','VTZ-Vishakapatnam',
              'BLR-Bengaluru','CJB-Coimbatore','JED-Jeddah','BKK-Bangkok','AMD-Ahmedabad',
              'CMB-Colombo','BHU-Bhavnagar','CCJ-Kozhikode','GOX-Goa','SHL-Shillong','AYJ-Ayodhya']



emtectors=['JAI-Jaipur-India','CCU-Kolkata-India','CCU-Kolkata-India',
           'DHM-Dharamsala-India','IXY-Kandla-India','PNQ-Pune-India',
           'MAA-Chennai-India','CGP-Chittogram-India','DXB-Dubai-UnitedArab',
           'IXB-Bagdogra-India','PAT-Patna-India','IXG-Belgavi-India','GWL-Gwalior-India',
           'GOI-Goa-India','DEL-Delhi-India','DED-Dehradun-India','RAJ-Rajkot-India',
           'KBK-Khushinagar-India','ISK-Nashik-India','HJR-Khajurao-India','SAG-Shirdi-India',
           'GAU-Guwahati-India','PYG-Pakyong-India','TIR-Tirupati-India','DAC-Dhaka-Bangladesh',
           'IXM-Madurai-India','BOM-Mumbai-India','IXE-Manglore-India','UDR-Udaipur-India',
           'RDP-Durgapur-India','IXS-Silchar-India','SXR-Srinagar-India','HYD-Hyderabad-India',
           'STV-Surat-India','JRG-Jharsuguda-India','VNS-Varanasi-India','DBR-Darbanga-India',
           'PNY-Pondicherry-India','KNU-Kanpur-India','IXZ-Port Blair-India','TRV-Trivandrum-India',
           'JDH-Jodhpur-India','JLR-Jabalpur-India','IXJ-Jammu-India','JSA-Jaisalmer-India',
           'ATQ-Amritsar-India','GOP-Gorakhpur-India','IXL-Leh-India','KQH-Kishangarh-India',
           'PBD-Porbandar-India','RUH-Riyadh-SaudiArabia','COK-Kochi-India',
           'VTZ-Vishakapatnam-India','BLR-Bengaluru-India','CJB-Coimbatore-India',
           'JED-Jeddah-SaudiArabia','BKK-Bangkok-Thailand','AMD-Ahmedabad-India',
           'CMB-Colombo-India','BHU-Bhavnagar-India','CCJ-Kozhikode-India','GOX-Goa-India','SHL-Shillong-India','AYJ-Ayodhya-India']



clearsectors=['JAI','CCU','DHM','IXY','PNQ','MAA','CGP',
              'DXB','IXB','PAT','IXG','GWL','GOI','DEL',
              'DED','RAJ','KBK','ISK','HJR','SAG','GAU',
              'PYG','TIR','DAC','IXM','BOM','IXE','UDR',
              'RDP','IXS','SXR','HYD','STV','JRG','VNS',
              'DBR','PNY','KNU','IXZ','TRV','JDH','JLR',
              'IXJ','JSA','ATQ','GOP','IXL','KQH','PBD',
              'RUH','COK','VTZ','BLR','CJB','JED','BKK',
              'AMD','CMB','BHU','CCJ','GOX','SHL','AYJ']

mmtsectors=['JAI','CCU','DHM','IXY','PNQ','MAA','CGP',
              'DXB','IXB','PAT','IXG','GWL','GOI','DEL',
              'DED','RAJ','KBK','ISK','HJR','SAG','GAU',
              'PYG','TIR','DAC','IXM','BOM','IXE','UDR',
              'RDP','IXS','SXR','HYD','STV','JRG','VNS',
              'DBR','PNY','KNU','IXZ','TRV','JDH','JLR',
              'IXJ','JSA','ATQ','GOP','IXL','KQH','PBD',
              'RUH','COK','VTZ','BLR','CJB','JED','BKK',
              'AMD','CMB','BHU','CCJ','GOX','SHL','AYJ']
  
#content-----------------------------

lbl_1= Label(win,text="Locaction:1")
lbl_1.place(x=20, y=100)
lbl_2= Label(win,text="Locaction:2")
lbl_2.place(x=300, y=100)

#-------------------------------------------


date_1=StringVar()
lbl_d1= Label(win,text="Date:1")
lbl_d1.place(x=50, y=200)
date_1=Entry(win)
date_1.place(x=100,y=200)

#-------------------------------------------------

lbl_d2= Label(win,text="Date:2")
lbl_d2.place(x=330, y=200)
date_2=Entry(win)
date_2.place(x=380,y=200)


#---------------------------------------------------
options = [
"EMT", 
"Paytm",
"ClearTrip",
"MMT"
]
ent_1=StringVar()
ant_1=StringVar()

ent_2=StringVar()
ant_2=StringVar()

ent_3=StringVar()
ant_3=StringVar()

ent_4=StringVar()
ant_4=StringVar()

clr1=StringVar()
clr2=StringVar()

def dshow(event):
  global ent_1 
  global ent_2
  global ent_3
  global ant_1
  global ant_2
  global ant_3
  global ent_4
  global ant_4

  if menu.get()=="Paytm":
   dateshowpaytm=Label(win,text="yyyy-mm-dd")
   dateshowpaytm.place(x=100, y=170)
   dateshowpaytm=Label(win,text="yyyy-mm-dd")
   dateshowpaytm.place(x=380, y=170)
   ent_1=AutocompleteEntry(win,completevalues=paytmsectors)
   ent_1.place(x=100,y=100)
   ant_1=AutocompleteEntry(win, completevalues=paytmsectors)
   ant_1.place(x=385,y=100)

  elif menu.get()=='EMT':
    dateshowpaytm=Label(win,text="dd/mm/yyyy")
    dateshowpaytm.place(x=100, y=170)
    dateshowemt=Label(win,text="dd/mm/yyyy")
    dateshowemt.place(x=380, y=170)
    
    ent_2=AutocompleteEntry(win,completevalues=emtectors)
    ent_2.place(x=100,y=100)
    ant_2=AutocompleteEntry(win, completevalues=emtectors)
    ant_2.place(x=385,y=100)

  elif menu.get()=='ClearTrip':
    
    dateshowpaytm=Label(win,text="dd/mm/yyyy")
    dateshowpaytm.place(x=100, y=170)
    dateshowclr=Label(win,text="dd/mm/yyyy")
    dateshowclr.place(x=380, y=170)
    ent_3=AutocompleteEntry(win,completevalues=clearsectors)
    ent_3.place(x=100,y=100)
    ant_3=AutocompleteEntry(win,completevalues=clearsectors)
    ant_3.place(x=385,y=100)

  elif menu.get()=='MMT':
    
    dateshowpaytm=Label(win,text="dd/mm/yyyy")
    dateshowpaytm.place(x=100, y=170)
    dateshowclr=Label(win,text="dd/mm/yyyy")
    dateshowclr.place(x=380, y=170)
    ent_4=AutocompleteEntry(win,completevalues=mmtsectors)
    ent_4.place(x=100,y=100)
    ant_4=AutocompleteEntry(win,completevalues=mmtsectors)
    ant_4.place(x=385,y=100)

  
#----------------------------------------------------------------


menu= StringVar()
menu.set("Select Any Website")


drop= OptionMenu(win, menu, *options,command=dshow)
drop.place(x=200, y=26)

def getdaterange(start,end,format_):
  start=datetime.strptime(start,format_)
  enddate=datetime.strptime(end,format_)

  for i in range((enddate-start).days+1):
    yield start+timedelta(days=i)


def openlink():
    global ent_1 
    global ent_2
    global ent_3
    global ant_1
    global ant_2
    global ant_3
    start_date = date_1.get()
    end_date = date_2.get()

    if menu.get() == 'Paytm':
     
     format_='%Y-%m-%d'
     for date in getdaterange(start_date,end_date,format_):
       webbrowser.open("https://tickets.paytm.com/flights/flightSearch/"+ent_1.get()+"/"+ant_1.get()+"/1/0/0/E/"+date.strftime(format_)+"")
    
    elif menu.get() == 'EMT':
     #DEL-Delhi-India...BOM-Mumbai-India....dd/mm/yyyy
     format_='%d/%m/%Y'
     for date in getdaterange(start_date,end_date,format_):
       webbrowser.open("https://flight.easemytrip.com/FlightList/Index?srch="+ent_2.get()+"|"+ant_2.get()+"|"+date.strftime(format_)+"&px=1-0-0&cbn=0&ar=undefined&isow=true&isdm=true&lang=en-us&utm_source=google&utm_medium=cpc&utm_campaign=788997081&utm_content=39319940377&utm_term=easemytrip&utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_easemytrip&adgroupid=39319940377&gclid=CjwKCAjwrJ-hBhB7EiwAuyBVXWgbniQBMLc2AR07eZm1X5ULIccXE12JIABAcNw11RaRqXYDz-3zzhoCniYQAvD_BwE&IsDoubleSeat=false&CCODE=IN&curr=INR&apptype=B2C")
    
    elif menu.get() == 'ClearTrip':  
     #DD/MM/YYYY....DELGOP
     format_='%d/%m/%Y'
     for date in getdaterange(start_date,end_date,format_):
       webbrowser.open("https://www.cleartrip.com/flights/results?adults=1&childs=0&infants=0&class=Economy&depart_date="+date.strftime(format_)+"&from="+ent_3.get()+"&to="+ant_3.get()+"&intl=n&origin=BLR%20-%20Bangalore,%20IN&destination=BOM%20-%20Mumbai,%20IN&sft=&sd=1680412413594&rnd_one=O&sourceCountry=Bangalore&destinationCountry=Mumbai")


    elif menu.get() == 'MMT':
      format_='%d/%m/%Y'
      for date in getdaterange(start_date,end_date,format_):
       webbrowser.open("https://www.makemytrip.com/flight/search?itinerary="+ent_4.get()+"-"+ant_4.get()+"-"+date.strftime(format_)+"&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng")


#--------------------------------button for search--------------------

btn=Button(win, text="Search",width=17, command=openlink)
btn.place(x=200,y=350)
  
def clr():
  date_1.delete(0,END)
  date_2.delete(0,END)
  menu.set("Select Any Website")


rst=Button(win, text="Reset", command=clr)
rst.place(x=400,y=350)

win.mainloop()
