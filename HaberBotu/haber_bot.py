import feedparser
from tkinter import *
import webview

def open_url(event):
    webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
    webview.start()

def clear_frame():
    for widget in fr_haberler.winfo_children():
        widget.destroy()

def default_color_button():
    btn_son_dakika.configure(bg="lightblue")
    btn_dunya.configure(bg="lightblue")
    btn_ekonomi.configure(bg="lightblue")
    btn_saglik.configure(bg="lightblue")

def add_haberler(haberler):
    haber_count = 0

    for haber in haberler.entries:
        haber_count += 1
        if haber_count > 2:
            break
        Label(fr_haberler, text=haber.title, anchor='w', font=('Helveticabold', 14)).pack(side=TOP, fill="x")
        lbl_link = Label(fr_haberler, text=haber.link, anchor='w', font=('Helveticabold', 14), fg="blue", cursor="hand2")
        lbl_link.pack(side=TOP, fill="x")
        lbl_link.bind("<Button-1>", open_url)
        Label(fr_haberler, text="-", anchor='c', bg="pink").pack(side=TOP, fill="x")

def SonDakikaCommand():
    clear_frame()
    default_color_button()
    btn_son_dakika.configure(bg="blue")

    for url in son_dakika_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def DunyaCommand():
    clear_frame()
    default_color_button()
    btn_dunya.configure(bg="blue")

    for url in dunya_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def EkonomiCommand():
    clear_frame()
    default_color_button()
    btn_ekonomi.configure(bg="blue")

    for url in ekonomi_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)

def SaglikCommand():
    clear_frame()
    default_color_button()
    btn_saglik.configure(bg="blue")

    for url in saglik_url:
        haberler = feedparser.parse(url)
        add_haberler(haberler)


son_dakika_url = ["https://www.cnnturk.com/feed/rss/all/news",
                  "https://www.ntv.com.tr/son-dakika.rss",
                  "https://www.milliyet.com.tr/rss/rssnew/sondakikarss.xml",
                  "https://www.sozcu.com.tr/feeds-son-dakika"]

dunya_url = ["https://www.cnnturk.com/feed/rss/dunya/news",
             "https://www.ntv.com.tr/dunya.rss",
             "https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml",
             "https://www.sozcu.com.tr/feeds-rss-category-dunya"]

ekonomi_url = ["https://www.cnnturk.com/feed/rss/ekonomi/news",
               "https://www.ntv.com.tr/ekonomi.rss",
               "https://www.milliyet.com.tr/rss/rssnew/ekonomi.xml",
               "https://www.sozcu.com.tr/feeds-rss-category-ekonomi"]

saglik_url = ["https://www.cnnturk.com/feed/rss/saglik/news",
              "https://www.ntv.com.tr/saglik.rss",
              "https://www.milliyet.com.tr/rss/rssnew/saglik.xml",
              "https://www.sozcu.com.tr/feeds-rss-category-saglik"]

#UI#
window = Tk()
window.title("Haber Botu")
window.geometry("1000x600")

fr_haberler = Frame(window, height=600)
fr_butonlar = Frame(window, relief=RAISED, bg="pink", bd=2)

btn_son_dakika = Button(fr_butonlar, text="Son Dakika", font=('Helveticabold',14), bg="lightblue", command=SonDakikaCommand)
btn_dunya = Button(fr_butonlar, text="Dünya", font=('Helveticabold',14), bg="lightblue", command=DunyaCommand)
btn_ekonomi = Button(fr_butonlar, text="Ekonomi", font=('Helveticabold',14), bg="lightblue", command=EkonomiCommand)
btn_saglik = Button(fr_butonlar, text="Sağlık", font=('Helveticabold',14), bg="lightblue", command=SaglikCommand)
btn_deneme = Button(fr_butonlar, text = "Deneme")

btn_son_dakika.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_dunya.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_ekonomi.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_saglik.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

fr_butonlar.grid(row=0, column=0, sticky="ns")
fr_haberler.grid(row=0, column=1, sticky="ns")

window.mainloop()