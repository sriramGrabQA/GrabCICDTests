#SDP Order Queue URLs
SITCREATEORDERAPI = 'https://jiograbsitqueue.queue.core.windows.net/createordersit/messages?sv=2018-03-28&si=createord' \
                     'ersit-a&sig=nCKI4o4FFhzSx5Qa4n2ZqZaVvY9ny9lEEx%2BBIZ9LNVM%3D'
SITUPDATEORDERAPI = 'https://jiograbsitqueue.queue.core.windows.net/updateordersit/messages?sv=2018-03-28&si' \
                 '=updateordersit-a&sig=LAG2HxuitPcZbuhMKv/U6CRpUq8Y0LHHyHa%2BzvqL364%3D'
#Host
SITHOST = 'https://sit.grab.in/'

#Webservice log related constants
SITWEBSERVICELOG = SITHOST + 'web_service_log/'
SITWEBSERVICELOGUSERNAME = 'webber'
SITWEBSERVICELOGPASSWORD = 'Pass@123'

#Client API details
SITAPI = SITHOST + 'grabriderapp'
SITSDPCREATETRIP = SITHOST + 'Clientapi/Sdpcalls/createsdptrip'

#DB connection details
SITDBHOST = '172.17.2.93'
SITDBNAME = 'db_grab_sit'
SITDBUSERNAME = 'debashishkha'
SITDBPASSWORD = 'Deb@shih#321'

#Prod Replica connection details
PRODDBHOST = '172.20.4.246'
PRODDBNAME = 'db_grab_prod'
PRODDBUSERNAME = 'srisai_r'
SITDBPASSWORD = '$r!s@i_R$%53'
