#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

import sys
if sys.version_info < (3,0,0):
    py3 = False
else:
    py3 = True

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk
    from ttkthemes import ThemedStyle

import guinsspy_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    guinsspy_support.set_Tk_var()
    top = PKI__GUI_for_NSS (root)
    guinsspy_support.init(root, top)
    root.mainloop()

w = None
def create_PKI__GUI_for_NSS(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    guinsspy_support.set_Tk_var()
    top = PKI__GUI_for_NSS (w)
    guinsspy_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PKI__GUI_for_NSS():
    global w
    w.destroy()
    w = None

g_iso3166_codes = (
"Австралия","AU","Австрия","AT","Азербайджан","AZ","Аландские о-ва","AX","Албания","AL","Алжир","DZ","Американское Самоа","AS","Ангилья",
"AI","Ангола","AO","Андорра","AD","Антарктида","AQ","Антигуа и Барбуда","AG","Аргентина","AR","Армения","AM","Аруба","AW",
"Афганистан","AF","Багамские о-ва","BS","Бангладеш","BD","Барбадос","BB","Бахрейн","BH","Беларусь","BY","Белиз","BZ","Бельгия","BE","Бенин","BJ",
"Бермудские о-ва","BM","Болгария","BG","Боливия","BO","Босния и Герцеговина","BA","Ботсвана","BW","Бразилия","BR",
"Британская территория в Индийском океане","IO","Британские Виргинские о-ва","VG","Бруней Даруссалам","BN",
"Буркина Фасо","BF","Бурунди","BI","Бутан","BT","Вануату","VU","Ватикан","VA","Великобритания","GB","Венгрия","HU","Венесуэла","VE",
"Виргинские о-ва (США)","VI","Внешние малые острова (США)","UM","Внешняя Океания","QO","Восточный Тимор","TL","Вьетнам","VN",
"Габон","GA","Гаити","HT","Гайана","GY","Гамбия","GM","Гана","GH","Гваделупа","GP","Гватемала","GT","Гвинея","GN","Гвинея-Бисау","GW","Германия","DE",
"Гернси","GG","Гибралтар","GI","Гондурас","HN","Гонконг (особый район)","HK","Гренада","GD","Гренландия","GL","Греция","GR","Грузия","GE",
"Гуам","GU","Дания","DK","Демократическая Республика Конго","CD","Джерси","JE","Джибути","DJ","Диего-Гарсия","DG","Доминика","DM",
"Доминиканская Республика","DO","Европейский союз","EU","Египет","EG","Замбия","ZM","Западная Сахара","EH","Зимбабве","ZW",
"Израиль","IL","Индия","IN","Индонезия","ID","Иордания","JO","Ирак","IQ","Иран","IR","Ирландия","IE","Исландия","IS","Испания","ES","Италия","IT",
"Йемен","YE","Казахстан","KZ","Каймановы острова","KY","Камбоджа","KH","Камерун","CM","Канада","CA","Канарские о-ва","IC","Катар","QA",
"Кения","KE","Кипр","CY","Киргизия","KG","Кирибати","KI","Китай","CN","Кокосовые о-ва","CC","Колумбия","CO","Коморские о-ва","KM","Конго","CG",
"Коста-Рика","CR","Кот дИвуар","CI","Куба","CU","Кувейт","KW","Лаос","LA","Латвия","LV","Лесото","LS","Либерия","LR","Ливан","LB","Ливия","LY","Литва","LT",
"Лихтенштейн","LI","Люксембург","LU","Маврикий","MU","Мавритания","MR","Мадагаскар","MG","Майотта","YT","Макао (особый район)","MO",
"Македония","MK","Малави","MW","Малайзия","MY","Мали","ML","Мальдивские о-ва","MV","Мальта","MT","Марокко","MA","Мартиника","MQ",
"Маршалловы о-ва","MH","Мексика","MX","Мозамбик","MZ","Молдова","MD","Монако","MC","Монголия","MN","Монтсеррат","MS","Мьянма","MM","Намибия","NA",
"Науру","NR","Непал","NP","Нигер","NE","Нигерия","NG","Нидерландские Антильские о-ва","AN","Нидерланды","NL","Никарагуа","NI","Ниуе","NU",
"Новая Зеландия","NZ","Новая Каледония","NC","Норвегия","NO","ОАЭ","AE","Оман","OM","Остров Буве","BV","Остров Вознесения","AC",
"Остров Клиппертон","CP","Остров Мэн","IM","Остров Норфолк","NF","Остров Рождества","CX","Остров Святого Бартоломея","BL",
"Остров Святого Мартина","MF","Остров Святой Елены","SH","Острова Зеленого Мыса","CV","Острова Кука","CK",
"Острова Тёркс и Кайкос","TC","Острова Херд и Макдональд","HM","Пакистан","PK","Палау","PW","Палестинские территории","PS",
"Панама","PA","Папуа Новая Гвинея","PG","Парагвай","PY","Перу","PE","Питкэрн","PN","Польша","PL","Португалия","PT","Пуэрто-Рико","PR",
"Республика Корея","KR","Реюньон","RE","Российская Федерация","RU","Руанда","RW","Румыния","RO","Сальвадор","SV","Самоа","WS","Сан-Марино","SM",
"Сан-Томе и Принсипи","ST","Саудовская Аравия","SA","Свазиленд","SZ","Свальбард и Ян-Майен","SJ","Северная Корея","KP",
"Северные Марианские о-ва","MP","Сейшельские о-ва","SC","Сен-Пьер и Микелон","PM","Сенегал","SN","Сент-Винсент и Гренадины",
"VC","Сент-Киттс и Невис","KN","Сент-Люсия","LC","Сербия","RS","Сербия и Черногория","CS","Сеута","и","Мелилья","EA","Сингапур","SG",
"Сирия","SY","Словакия","SK","Словения","SI","Соломоновы о-ва","SB","Сомали","SO","Судан","SD","Суринам","SR","США","US","Сьерра-Леоне","SL",
"Таджикистан","TJ","Таиланд","TH","Тайвань","TW","Танзания","TZ","Того","TG","Токелау","TK","Тонга","TO","Тринидад и Тобаго","TT",
"Тристан-да-Кунья","TA","Тувалу","TV","Тунис","TN","Туркменистан","TM","Турция","TR","Уганда","UG","Узбекистан","UZ","Украина","UA",
"Уоллис и Футуна","WF","Уругвай","UY","Фарерские о-ва","FO","Федеративные Штаты Микронезии","FM","Фиджи","FJ","Филиппины","PH",
"Финляндия","FI","Фолклендские о-ва","FK","Франция","FR","Французская Гвиана","GF","Французская Полинезия","PF",
"Французские Южные Территории","TF","Хорватия","HR","ЦАР","CF","Чад","TD","Черногория","ME","Чехия","CZ","Чили","CL","Швейцария","CH","Швеция",
"SE","Шри-Ланка","LK","Эквадор","EC","Экваториальная Гвинея","GQ","Эритрея","ER","Эстония","EE","Эфиопия","ET","ЮАР","ZA",
"Южная Джорджия и Южные Сандвичевы Острова","GS","Ямайка","JM","Япония","JP"
)

regionRF = ( 'Республика Адыгея (Адыгея)',                       
'Республика Башкортостан',                          
'Республика Бурятия',                               
'Республика Алтай',                                 
'Республика Дагестан',                              
'Республика Ингушетия',                             
'Кабардино-Балкарская Республика',                  
'Республика Калмыкия',                              
'Карачаево-Черкесская Республика',                  
'Республика Карелия',                               
'Республика Коми',                                  
'Республика Марий Эл',                              
'Республика Мордовия',                              
'Республика Саха (Якутия)',                         
'Республика Северная Осетия - Алания',              
'Республика Татарстан',                             
'1Республика Тыва',                                 
'Удмуртская Республика',                            
'Республика Хакасия',                               
'Чеченская Республика',                             
'Чувашская Республика - Чувашия',                   
'Алтайский край',                                   
'Краснодарский край',                               
'Красноярский край',                                
'Приморский край',                                  
'Ставропольский край',                              
'Хабаровский край',                                 
'Амурская область',                                 
'Архангельская область и Ненецкий автономный округ',
'Астраханская область',                             
'Белгородская область',                             
'Брянская область',                                 
'Владимирская область',                             
'Волгоградская область',                            
'Вологодская область',                              
'Воронежская область',                              
'Ивановская область',                               
'Иркутская область',                                
'Калининградская область',                          
'Калужская область',                                
'Камчатский край',                                  
'Кемеровская область',                              
'Кировская область',                                
'Костромская область',                              
'Курганская область',                               
'Курская область',                                  
'Ленинградская область',                            
'Липецкая область',                                 
'Магаданская область',                              
'Московская область',                               
'Мурманская область',                               
'Нижегородская область',                            
'Новгородская область',                             
'Новосибирская область',                            
'Омская область',                                   
'Оренбургская область',                             
'Орловская область',                                
'Пензенская область',                               
'Пермский край',                                    
'Псковская область',                                
'Ростовская область',                               
'Рязанская область',                                
'Самарская область',                                
'Саратовская область',                              
'Сахалинская область',                              
'Свердловская область',                             
'Смоленская область',                               
'Тамбовская область',                               
'Тверская область',                                 
'Томская область',                                  
'Тульская область',                                 
'Тюменская область',                                
'Ульяновская область',                              
'Челябинская область',                              
'Забайкальский край',                               
'Ярославская область',                              
'г. Москва',
'г. Санкт-Петербург',                               
'Еврейская автономная область',                     
'Ханты-Мансийский автономный округ - Югра',         
'Чукотский автономный округ',                       
'Ямало-Ненецкий автономный округ',                  
'Иные территории, включая, г. Байконур')


def Digit (ent, len, text, size):
#    print ('Text=' + '"' + text + '"')
    size = int(size)
    len = int(len)
    if (text.isdigit() == False):
#        ent.configure(style='red.TEntry')
        return False
#    if (text.isdigit() == True):
#    ent.configure(style='cyan.TEntry')
    length = 0
#Почему-то не срабатывает
#    l1 = len(text)
#Пришлось сделать так!!!
    for t in text:
    	length = length + 1
#    print ('LText=' + '"' + str(length) + '"')
    if (length > size):
        return False
    if (len >= size):
        return False
    return True

country_inv = {}
def makeformWho(frameWho, fields):
    global country_inv
    frameWho.entries = []
    i = 0
    row = Frame(frameWho)
    vcmdDigit = root.register(Digit)
    for field in fields:
      lab = Label(row, background="#00ff7f", text=field, anchor='w')
      if (i > 1):
          ent = ttk.Entry(row)
          if (field.find('ИНН') != -1 or field.find('СНИЛС') != -1 or field.find('ОГРН') != -1 ):
            if (field.find('ИНН') != -1):
                lenkv = 12
            elif (field.find('СНИЛС') != -1):
                lenkv = 11
            elif (field.find('ОГРНИП') != -1):
                lenkv = 15
            elif (field.find('ОГРН') != -1):
                lenkv = 13
            ent.configure(validate="key", validatecommand=(vcmdDigit, ent, '%i', '%P', lenkv))
      else:
          ent = ttk.Combobox(row, width=25, background="white")
          if (i == 1):
                ent.configure(values=regionRF)
                ent.delete(0,END)
                ent.insert(END, regionRF[49])
          elif (i == 0):
                country = {}
                for j in range(0, len(g_iso3166_codes) - 1, 2) :
#	    print (g_iso3166_codes[j+1] + '=' + g_iso3166_codes[j])
                    country[g_iso3166_codes[j+1]] = str(g_iso3166_codes[j])
                    country_inv[g_iso3166_codes[j]] = str(g_iso3166_codes[j+1])
                lc = list(country.values())
                lc.sort()
                ent.configure(values=lc)
                ent.delete(0,END)
                ent.insert(END, country['RU'])
          
      lab.grid(row=i, column=0, sticky='we')
      ent.grid(row=i, column=1, sticky='we')
      frameWho.entries.append((field, ent))
      i = i + 1
    row.grid_columnconfigure(1, weight=1)
    row.pack(side=TOP, fill=X, padx=5, pady=1)

    return frameWho.entries

def returnRequest(ents, self1, frameWho):
    frameWho.pack_forget()
    self1.TFrame1.pack(in_=self1.Frame1,expand=1,fill='both',padx=5,pady='1mm 0',side='top')
    rb = guinsspy_support.varDB.get()
    if (rb == '0'):
        self1.TLabel1.configure(text=''' ИОК/PKI. Хранилище сертификатов Berkeley DB (Mozilla)''')
    else:
        self1.TLabel1.configure(text=''' ИОК/PKI. Хранилище сертификатов SQLite (Google)''')
    self1.TLabel1.configure(image=guinsspy_support.img_svitok, compound='left')

def createWho(vlad, frameWho, self1):
    typeCert = ('Физическое лицо', 'Индивидуальный предприниматель', 'Юридическое лицо')
    reqFL = {
        'C' : ' 1. Страна', 
        'ST' : ' 2. Регион', 
        'CN' : ' 3. ФИО',
	'SN' : ' 4. Фамилия',
	'givenName' : ' 5. Имя, Отчество',
	'E' : ' 6. Электронная почта',
	'L' : ' 7. Населенный пункт',
	'street' : ' 8. Улица, номер дома',
	'INN' : ' 9. ИНН (10 или 12 символов)',
	'SNILS' : '10. СНИЛС (11 символов)'}
    reqUL = {
        'C' : ' 1. Страна', 
        'ST' : ' 2. Регион', 
        'CN' : ' 3. Организация',
	'O' : ' 4. Наименование организации',
	'E' : ' 5. Электронная почта',
	'L' : ' 6. Населенный пункт',
	'street' : ' 7. Улица, номер дома',
	'OU' : ' 8. Подразделение организации',
	'title' : ' 9. Должность',
	'SN' : '10. Фамилия',
	'givenName' : '11. Имя, Отчество',
	'OGRN' : '12. ОГРН (13 символов)',
	'INN' : '13. ИНН (10 или 12 символов)'}
    reqIP = {
        'C' : ' 1. Страна', 
        'ST' : ' 2. Регион', 
        'CN' :  ' 3. ФИО',
	'SN' : ' 4. Фамилия',
	'givenName' : ' 5. Имя, Отчество',
	'E' : ' 6. Электронная почта',
	'L' : ' 7. Населенный пункт',
	'street' : ' 8. Улица, номер дома',
	'INN' : ' 9. ИНН (10 или 12 символов)',
	'OGRNIP' : '10. ОГРНИП (15 символов)',
	'SNILS' : '11. СНИЛС (11 символов)'}
    reqAss = {
        'C' : ' 1. Страна', 
        'ST' : ' 2. Регион', 
	'O' : ' 3. Организация',
	'L' : ' 4. Населенный пункт',
	'street' : ' 5. Улица, номер дома',
	'U' : ' 6. Подразделение организации',
	'title' : ' 7. Должность',
	'INN' : ' 8. ИНН (10 или 12 символов)',
	'OGRN' : ' 9. ОГРН (13 символов)',
	'OGRNIP' : '10. ОГРНИП (15 символов)',
	'SNILS' : '11. СНИЛС (11 символов)',
	'KPP' : '12. КПП (10 символов)'}
#    print('nss_my_support.acceptVlad')

#    print (vlad)
#vlad = ЮрЛицо, ФизЛицо, ИП reqAss зависят от типа 
    if vlad == 'Физическое лицо':
        d1 = list(reqFL.values())
    elif vlad == 'Индивидуальный предприниматель':
        d1 = list(reqIP.values())
    elif vlad == 'Юридическое лицо':
        d1 = list(reqUL.values())
    else:
        return
    d1.sort()
#Создания полей для CN
#    ents = makeform(root, fields)
    ents = makeformWho(frameWho, d1)

    ttk.Style().configure("TSeparator",background='#e0e0da', relief='groove', anchor='s')
#    ttk.Style().configure("TSeparator", height=9,borderwidth=9, background='#e0e0da', relief='groove', anchor='s')
    
    frameWho.retCreate = ttk.Button(frameWho, text='Вернуться', command=(lambda e=ents: returnRequest(e, self1,frameWho)))
    frameWho.retCreate.pack(anchor='se',side='bottom', padx=5, pady=5)
    frameWho.whoSep = ttk.Separator(frameWho)
    frameWho.whoSep.pack(anchor='s',expand=YES,fill=X,side=BOTTOM )


class PKI__GUI_for_NSS:
    def __init__(self, top=None):
        global py3
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
#        _bgcolor = '#c0bab4'  # X11 color: '#e0e0da'
        _bgcolor = 'white'  # X11 color: '#e0e0da'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: '#e0e0da'
        _ana1color = '#d9d9d9' # X11 color: '#e0e0da' 
#        _ana2color = '#d9d9d9' # X11 color: '#e0e0da' 
        _ana2color = '#e0e0da' # X11 color: '#e0e0da' 

        font10 = "-family courier -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        import ttkthemes
        self.style = ttkthemes.ThemedStyle()
        if (py3 == True):
    	    import ttkthemes
    	    self.style.theme_use('breeze')
    	    self.style.configure('TEntry',padding=-3)
    	    self.style.configure('TCombobox',padding=-3)
    	    self.style.configure('TButton',padding=3)
    	    self.style.configure('TButton',background='white')
        else:
    	    self.style.theme_use('arc')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.style.configure('white.TEntry', foreground='black')
        self.style.configure('blue.TEntry', foreground='blue')
        self.style.configure('red.TEntry', foreground='red')
        self.style.configure('cyan.TEntry', foreground='green')

        top.geometry("773x607+135+117")
        top.title("PKI. GUI for NSS")
        top.configure(borderwidth="2")
        top.configure(relief="flat")
        top.configure(background="#cdc7c2")

        self.Frame1 = Frame(top)
        self.Frame1.pack(expand=1,fill='both', padx= 0,pady= 0,side='top')
        self.Frame1.configure(borderwidth="0")
        self.Frame1.configure(background="#f7f6f5")
        self.Frame1.configure(width=775)

        self.TLabel1 = ttk.Label(self.Frame1, anchor=CENTER)
        self.TLabel1.pack(in_=self.Frame1, expand=0,fill='none',padx=5,pady= 5,side='top')
#        self.TLabel1.configure(background="#c0bab4")
        self.TLabel1.configure(background="#f7f6f5")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=("Times", 11, "bold", "italic"))
#        self.TLabel1.configure(borderwidth="3")
#        self.TLabel1.configure(relief=RIDGE)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text=''' ИОК/PKI. GUI для Network Security Services ''')

#        self.TFrame1 = ttk.Frame(self.Frame1, relief=GROOVE, borderwidth="0", width=715)
        self.TFrame1 = Frame(self.Frame1, relief=GROOVE, borderwidth="0", background="#cdc7c2",width=715)
        self.TFrame1.pack(in_=self.Frame1,expand=1,fill='both',padx=5,pady=0,side='top')

        self.TFrameWho = []
        i = 0
#Фреймы для Юрлица, Физлица и ИП
        typeCert = ('Физическое лицо', 'Индивидуальный предприниматель', 'Юридическое лицо')
        for i in range(0,3):
#            self.TFrameWho[i].pack(in_=self.Frame1,expand=1,fill='both',padx=5,pady=5,side='top')
            self.TFrameWho.append(ttk.Frame(self.Frame1, relief=GROOVE, borderwidth="2", width=715))
            createWho(typeCert[i], self.TFrameWho[i], self)


        self.Frame2 = LabelFrame(self.TFrame1)
        self.Frame2.configure(text="Наши возможности", labelanchor='n', font='helvetica 10 bold roman')
        self.Frame2.pack(in_=self.TFrame1,expand=0,fill='y',padx=(0,3),pady=(3,0),side='right')

        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="0")
        self.Frame2.configure(background="#eff0f1")
#        self.Frame2.configure(highlightbackground="#c0bab4")
        self.Frame2.configure(width=265)
#RadioButton
        self.typeRab = ["Разработчик", "Управление модулями PKCS#11",
	    "Управление сертификатами", "Подписать файл", "Зашифровать файл", 
	    "Проверить ЭП файла", "Извлечь оригинал из PKCS#7", "Создать запрос"]
        i = 0
        self.TButtonR = []
        count_rab = len(self.typeRab)
        for i in range(0, count_rab):
    	    self.TButtonRB = ttk.Radiobutton(self.Frame2)
    	    self.TButtonRB.configure(text=self.typeRab[i])
    	    self.TButtonRB.configure(variable=guinsspy_support.varBut)
    	    self.TButtonRB.configure(value=i)
    	    self.TButtonRB.pack(in_=self.Frame2,expand=1,fill='x',side= 'top', ipady=3,padx=5,pady=0)
    	    self.TButtonRB.configure(command=guinsspy_support.ReloadNSS)
#    	    self.TButtonRB.configure(state='disabled')
    	    self.TButtonR.append(self.TButtonRB)


#        self.TButton10 = ttk.Button(self.Frame2, command=sys.exit)
        self.TButton10 = ttk.Button(top, command=sys.exit)
        self.TButton10.configure(takefocus="")
        self.TButton10.configure(text='''Завершаем''')

        self.Label1 = Label(self.Frame2)
        self.Label1.pack(in_=self.Frame2,anchor='center',expand=1,fill='both', ipadx=10,ipady=0,padx= 5,pady= 5,side='top')
        self.Label1.configure(activebackground="#ffffcd")
#        self.TButton10.pack(in_=self.Frame2,expand=1,fill='none',side= 'top' ,padx= 5)
        self.Label1.configure(background="#eff0f1")
        self.Label1.configure(disabledforeground="#b8a786")
        self.Label1.configure(highlightbackground="#c0bab4")
        self.Label1.configure(text='''Логотип''')

        self.Frame3 = Frame(self.TFrame1)
        self.Frame3.pack(in_=self.TFrame1,expand=1,fill='both',padx=3,pady=(3,0),side='left')
        self.Frame3.configure(borderwidth="0")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="cyan")
        self.Frame3.configure(width=125)

        self.FrameRab = []

        i = 0
        for i in range(0,count_rab):
    	    self.Frame4 = LabelFrame(self.Frame3)
    	    self.Frame4.configure(text=self.typeRab[i], labelanchor='n', font='helvetica 10 bold roman')
    	    self.Frame4.configure(relief=FLAT)
    	    self.Frame4.configure(borderwidth="2")
    	    self.Frame4.configure(background="white")
#    	    self.Frame4.configure(background="#f7f6f5")
    	    self.FrameRab.append(self.Frame4)

        self.Labelframe1 = LabelFrame(self.Frame1)
        self.Labelframe1.pack (in_=self.Frame1,expand=0,fill='x',side='bottom', padx=5,pady=(0,3)) 
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(borderwidth="0")
        self.Labelframe1.configure(text='Выберите тип хранилища сертификатов и путь к нему', labelanchor='n', font='helvetica 10 bold roman')
#        self.Labelframe1.configure(background="#eff0f1")
        self.Labelframe1.configure(background="white")
        self.Labelframe1.configure(highlightbackground="#cdc7c2", highlightcolor="#cdc7c2", highlightthickness='3')
        self.Labelframe1.configure(width=150)

        self.Frame5 = Frame(self.Labelframe1, bg='#e0e0da')
        self.Frame5.pack (anchor='center',expand=0,fill='none',side='left', padx=5, pady='1mm 2mm') 
        self.Frame5.configure(relief=GROOVE)
        self.Frame5.configure(borderwidth="0")
#ttk::style map MyBorder.TButton -background [list disabled white pressed gray64 active skyblue !active #e2e2e1]
        self.style.map('TButton',background=[('disabled', 'white'), ('pressed', 'gray64'), ('active', 'skyblue'), ('!active', '#e2e2e1')])

        self.style.map('TRadiobutton',background=[('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton1 = ttk.Radiobutton(self.Frame5)

        self.TRadiobutton1.configure(variable=guinsspy_support.varDB)
        self.TRadiobutton1.configure(value="0")
        self.TRadiobutton1.configure(takefocus="")
        self.TRadiobutton1.configure(text='''Berkeley DB''')

        self.TRadiobutton2 = ttk.Radiobutton(self.Frame5)
        self.TRadiobutton2.configure(variable=guinsspy_support.varDB)
        self.TRadiobutton2.configure(value="1")
        self.TRadiobutton2.configure(takefocus="")
        self.TRadiobutton2.configure(text='''SQLite''')
        self.TRadiobutton1.pack(in_=self.Frame5, anchor='center',expand=0,fill='none',side='left', padx=0, pady=0)
        self.TRadiobutton2.pack(in_=self.Frame5, anchor='center',expand=0,fill='none',side='left', padx=2, pady=0)

        self.Entry1 = ttk.Entry(self.Labelframe1)
        self.Entry1.pack(anchor='center',expand=1,fill='x',side='left') 
        self.Entry1.configure(background="white")
        self.Entry1.configure(font=font10)

        self.TButton11 = Button(self.Labelframe1)

        self.TButton11.pack(anchor='w',side='right', padx='0 5', pady='2mm 2mm')
        self.TButton11.configure(command=(lambda:guinsspy_support.selectDB(self)))
        self.TButton11.configure(takefocus="")

#        self.TButton11.configure(text='''Выбрать каталог хранилища''', padding='0 3 0 3')


if __name__ == '__main__':
    vp_start_gui()



