# Mailspammer
import smtplib as smtp
import threading
import ssl

# Dein Text
dein_text = "Sample Text"


# Spam-Mail
def versendeMail(nachricht):
    global server
    deine_mail = "ceo@google.com"
    dein_passwort = "passwort1234"
    empfaenger = "recv@gmail.com"

    # Try-Exception Error-Handling
    try:
        # googles smtp auf port 587
        # nutze 465 bei Fehlschlag
        server = smtp.SMTP("smtp.gmail.com", 587)
        # extended smtp hello
        server.ehlo()
        # TLS Verbindung
        server.starttls(context=ssl.create_default_context())
        server.ehlo()
        server.login(deine_mail, dein_passwort)
        # Python Methode zur Versendung deiner Mail
        server.sendmail(deine_mail, empfaenger, nachricht)

    except Exception as fehler:
        print(fehler)
    # Schliessung der SMTP-Connection, ungeachtet der try Klausel
    finally:
        server.quit()


# Threads
def spam_mail():
    while True:
        versendeMail(dein_text)
    threads = []
    for i in range(40):
        t = threading.Thread(target=spam_mail())
        t.daemon = True
        threads.append(t)
    for i in range(40):
        threads[i].start()
    for i in range(40):
        threads[i].join()
