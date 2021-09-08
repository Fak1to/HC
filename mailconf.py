import smtplib

def email_west():

    SERVER = "server_ip"
    FROM = "from_email"
    TO = ["to_email"] 

    SUBJECT = "WEST"
    TEXT = "WEST"

    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER)
    server.login("smtp_login", "smtp_pass")
    server.sendmail(FROM, TO, message)
    server.quit()
    
def email_south():

    SERVER = "server_ip"
    FROM = "from_email"
    TO = ["to_email"]

    SUBJECT = "SOUTH"
    TEXT = "SOUTH"

    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER)
    server.login("smtp_login", "smtp_pass")
    server.sendmail(FROM, TO, message)
    server.quit()
    
def email_main():

    SERVER = "server_ip"
    FROM = "from_email"
    TO = ["to_email"]

    SUBJECT = "MAIN"
    TEXT = "MAIN"

    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER)
    server.login("smtp_login", "smtp_pass")
    server.sendmail(FROM, TO, message)
    server.quit()