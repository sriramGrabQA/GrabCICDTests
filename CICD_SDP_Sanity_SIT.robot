*** Settings ***

Library     APIcalls.py
Library     database.py



*** Test Cases ***


01. To check the working of SDP Create Order API
    log to console      \n Entering payload and calling the Create Order API \n
    ${order_id} =       APIcalls.check_create_order_SDP     SIT
    log to console      ${order_id}
    #log to console      \n reading order logs please wait one minute
    #Sleep   60 seconds
    #@{create_order_logs}=    read_create_order_logs     SIT
    #${flag}     APIcalls.string_contains    ${create_order_logs}[0]    Success Order Details : [{"res":{"message":"success","errorCode":"0","bulk_order_id":1,"pos_order_id":["${order_id}
    #Should be equal 	${flag}  ${true} 	The Create API is failed, please see the below logs \n${create_order_logs}[1]

02. To check the working of Login API
    log to console      \n Entering payload and calling the login API
    @{response_login} =  APIcalls.check_login       SIT
    Log To Console    The SID is: ${response_login}[2]
    Should Be Equal     ${response_login}[0]     success     Login API Failed, request response is ${response_login}[1]

03. To check the working of Checkin API
    log to console      \n Entering payload and calling the checkin API
    @{response_checkin} =  APIcalls.check_checkin       SIT
    Should Be Equal     ${response_checkin}[0]      success     Checkin API Failed, request response is ${response_checkin}[1]

