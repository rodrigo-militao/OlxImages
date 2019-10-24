import bs4 as bs
import urllib.request
import os

from tkinter import *
  
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 40
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 40
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 40
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Pegando imagens da OLX")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()
  
        self.urlLabel = Label(self.segundoContainer,text="URL", font=self.fontePadrao)
        self.urlLabel.pack(side=LEFT)
  
        self.url = Entry(self.segundoContainer)
        self.url["width"] = 60
        self.url["font"] = self.fontePadrao
        self.url.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Salvar Imagens"
        self.autenticar["font"] = ("Calibri", "16")
        self.autenticar["width"] = 24
        self.autenticar["command"] = self.dld_images
        self.autenticar.pack()

        ##url = str(input ('Qual a URL que você quer baixar as imagens?'))

    def dld_images(self):
        url = self.url.get()
        source = urllib.request.urlopen(url)

        soup = bs.BeautifulSoup(source,'lxml')

        title = soup.find('h1')
        imgs = soup.find_all('img', limit=20)

        folder = str(title.text)
        os.mkdir(folder)

        for img in imgs:
            url_imagem = img.get('src')
            filename = folder + '/' + str(img.get('alt'))
        #Fazer Download apenas das imagens dos apts.
            
            if img.get('alt') != "App Store" and img.get('alt') != "Google Play" and img.get('alt') != "None":
                imagefile = open(filename + '.jpg', 'wb')
                imagefile.write(urllib.request.urlopen(url_imagem).read())
                imagefile.close()
                self.url.delete(0, END)


    #Funcionalidades : mensagens de sucesso.



root = Tk()
Application(root)
root.mainloop()


