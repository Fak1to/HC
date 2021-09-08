from pythonping import ping
from mailconf import email_west, email_south, email_main


west_ping = ping('host_ip1', count=10, size=32)
south_ping = ping('host_ip2', count=10, size=32)


def allert_west():
    allert_trigger = 0
    if 30 <= int(west_ping.rtt_max_ms) < 2000:
        allert_trigger_west = allert_trigger + 1
    else:
        allert_trigger_west = allert_trigger
    return allert_trigger_west
send_email_west = allert_west()


def allert_south():
    allert_trigger = 0
    if 30 <= int(south_ping.rtt_max_ms) < 2000:
        allert_trigger_south = allert_trigger + 1
    else:
        allert_trigger_south = allert_trigger
    return allert_trigger_south
send_email_south = allert_south()


def send(allert, allert2):
    if allert == 1 and allert2 == 1:
        #print('main')
        email_main()
    elif allert == 1 and allert2 == 0:
        #print('south')
        email_south()
    elif allert == 0 and allert2 == 1:
        #print('west')
        email_west()    
    else:
        0       

send(send_email_south, send_email_west)