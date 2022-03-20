from tkinter import *
import pygame


pygame.mixer.init()
pygame.mixer.music.load("naza.mp3")

#fonction de playe la music 
def lancer():
    pygame.mixer.music.play(-1)
    
#fonction arrête la music     
def arrete():
    pygame.mixer.music.stop()
    
#fonction dessinant le tableau    
def damier(): 
    ligne_vert()
    ligne_hor()
        
def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='black')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='black')
        c_y+=c
        
#fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
def click_gauche(event): 
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='black')
    dico_case[x,y]=1
    
 #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
def click_droit(event):
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    dico_case[x,y]=0
    
#fonction pour changer la vitesse(l'attente entre chaque étape)
def change_vit(event): 
    global vitesse
    vitesse = int(eval(entree.get()))
    print(vitesse)
    
 #fonction dessinant le célèbre canon à planeur de Bill Gosper
def canon():
    dico_case[0*c,5*c]=1
    dico_case[0*c,6*c]=1
    dico_case[1*c,5*c]=1
    dico_case[1*c,6*c]=1
    dico_case[10*c,5*c]=1
    dico_case[10*c,6*c]=1
    dico_case[10*c,7*c]=1
    dico_case[11*c,4*c]=1
    dico_case[11*c,8*c]=1
    dico_case[12*c,3*c]=1
    dico_case[12*c,9*c]=1
    dico_case[13*c,3*c]=1
    dico_case[13*c,9*c]=1
    dico_case[14*c,6*c]=1
    dico_case[15*c,4*c]=1
    dico_case[15*c,8*c]=1
    dico_case[16*c,5*c]=1
    dico_case[16*c,6*c]=1
    dico_case[16*c,7*c]=1
    dico_case[17*c,6*c]=1
    dico_case[20*c,3*c]=1
    dico_case[20*c,4*c]=1
    dico_case[20*c,5*c]=1
    dico_case[21*c,3*c]=1
    dico_case[21*c,4*c]=1
    dico_case[21*c,5*c]=1
    dico_case[22*c,2*c]=1
    dico_case[22*c,6*c]=1
    dico_case[24*c,1*c]=1
    dico_case[24*c,2*c]=1
    dico_case[24*c,6*c]=1
    dico_case[24*c,7*c]=1
    dico_case[34*c,3*c]=1
    dico_case[34*c,4*c]=1
    dico_case[35*c,3*c]=1
    dico_case[35*c,4*c]=1    
    go()
#démarrage de l'animation
def go():
    global flag
    flag =1
    play()
        
#arrêt de l'animation      
def stop():
    global flag    
    flag =0

    #continier l'animation        
def continuer():
    global flag
    flag =1
    play()
    
#fonction comptant le nombre de cellules vivantes autour de chaque cellule    
def play(): 
    global flag, vitesse
    v=0
    while v!= width/c:
        w=0
        while w!= height/c:
            x=v*c
            y=w*c
            
            # cas spéciaux:
            # les coins
            
            #coin en haut à gauche
            if x==0 and y==0: 
                compt_viv=0
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
             #coin en bas à gauche    
            elif x==0 and y==int(height-c):
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            
            #coin en haut à droite
            elif x==int(width-c) and y==0: 
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            
             #coin en bas à droite
            elif x==int(width-c) and y==int(height-c):
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
            # cas spéciaux:
            # les bords du tableau (sans les coins)
            
             # bord de gauche
            elif x==0 and 0<y<int(height-c):
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and 0<y<int(height-c): # bord de droite
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(width-c) and y==0: # bord du haut
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(width-c) and y==int(height-c): # bord du bas
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            #cas généraux
            #les cellules qui ne sont pas dans les bords du tableau
            else:
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
                
            w+=1
        v+=1
    redessiner()
    if flag >0: 
        fen1.after(vitesse,play)

        
#fonction redessinant le tableau à partir de dico_etat
def redessiner(): 
    can1.delete(ALL)
    damier()
    t=0
    while t!= width/c:
        u=0
        while u!= height/c:
            x=t*c
            y=u*c
            if dico_etat[x,y]==3:
                dico_case[x,y]=1
                can1.create_rectangle(x, y, x+c, y+c, fill='black')
            elif dico_etat[x,y]==2:
                if dico_case[x,y]==1:
                    can1.create_rectangle(x, y, x+c, y+c, fill='black')
                else:
                    can1.create_rectangle(x, y, x+c, y+c, fill='red')
            elif dico_etat[x,y]<2 or dico_etat[x,y]>3:
                dico_case[x,y]=0
                can1.create_rectangle(x, y, x+c, y+c, fill='red')
            u+=1
        t+=1
        
    
#les différentes variables:

# taille de la grille

height = 400
width = 1000

#taille des cellules
c = 20

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=100

flag=0
#dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_etat = {} 
#dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
dico_case = {} 
i=0
 #assigne une valeur 0(morte) a chaque coordonnées(cellules) (valeur par défault en quelque sorte )
while i!= width/c:
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        dico_case[x,y]=0
        j+=1
    i+=1

#programme "principal" 
Tata = Tk(className="🧩JEU DE LA VIE🧩")


can1 = Canvas(Tata, width =width, height =height, bg ='red')

#Association clic/action
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack(side =TOP, padx =6, pady =6)

damier()

b1 = Button(Tata, text ='Joue', command =go).pack(side =LEFT, padx =3)
b2 = Button(Tata, text ='Pause', command =stop).pack(side =LEFT, padx =3)
b3 = Button(Tata, text ='Canon planeur', command =canon).pack(side =LEFT, padx =3)
b4 = Button(Tata, text ='Continuer', command =continuer).pack(side =LEFT, padx =3)
b5 = Button(Tata, text ='Music', command =lancer).pack(side =RIGHT, padx =3)
b6 = Button(Tata, text ='arrête du music', command =arrete).pack(side =RIGHT, padx =3)
#b7= Button(Tata, text = 'Quitter', bg = "#993366",fg = "white", width = 14,command = self.Ecran0.destroy).pack(side =RIGHT, padx =3)

#lancement 
Tata.mainloop()
