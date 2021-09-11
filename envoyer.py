import smtplib
from email.message import EmailMessage


def send_email(mesg,nom,tele,email):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('centre.declaration@gmail.com','bouchaib2021')
    msg = EmailMessage()
    message=mesg+f"\n \n le nom : {nom} \n le numéro de téléphone est : {tele} \n l'adreese e-mail est {email}"
    msg.set_content(message)
    msg['Subject']="Message de déclaration produit Awelk"
    msg['From']='centre.declaration@gmail.com'
    msg['To']='bou8027@gmail.com' 
    server.sendmail('centre.declaration@gmail.com','bou8027@gmail.com',msg.as_string())
    server.quit()
    
def buy(user,nbrproduct,tele,adr,city,produit,color):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('acheter.produit@gmail.com','bouchaib2021')
    messag = EmailMessage()
    message=f"il prend {nbrproduct} sur produit {produit} de color: {color} ;\n \n le nom : {user} \n le numéro de téléphone est : {tele} \n adresse : {adr},{city}"
    messag.set_content(message)
    messag['Subject']=f"Un demande sur un produit Awelk :{produit}"
    messag['From']='centre.declaration@gmail.com'
    messag['To']='bou8027@gmail.com' 
    server.sendmail('centre.declaration@gmail.com','bou8027@gmail.com',messag.as_string())
    server.quit()
    
def verif_msg(randnbr):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('centre.declaration@gmail.com','bouchaib2021')
    msg = EmailMessage()
    message=f"\n code est : {randnbr}"
    msg.set_content(message)
    msg['Subject']="code de verification de awelk"
    msg['From']='centre.declaration@gmail.com'
    msg['To']='bou8027@gmail.com' 
    server.sendmail('centre.declaration@gmail.com','bou8027@gmail.com',msg.as_string())
    server.quit()
    