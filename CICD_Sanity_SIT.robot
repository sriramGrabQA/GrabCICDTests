*** Settings ***

Library     APIcalls.py
Library     database.py



*** Test Cases ***


01. To check the working of Create Order API
    log to console      \n Entering payload and calling the Create Order API \n
    ${order_id} =       APIcalls.check_create_order
    log to console      ${order_id}
    log to console      \n reading order logs please wait one minute
    Sleep   60 seconds
    @{create_order_logs}=    read_create_order_logs     webber     Pass@123
    ${flag}     APIcalls.string_contains    ${create_order_logs}[0]    Success Order Details : [{"res":{"message":"success","errorCode":"0","bulk_order_id":1,"pos_order_id":["${order_id}
    Should be equal 	${flag}  ${true} 	The Create API is failed, please see the below logs \n${create_order_logs}[1]

02. To check the working of Update Order API
    log to console      \n Entering payload and calling the Update Order API
    ${order_id} =       APIcalls.check_update_order
    log to console      ${order_id}
    log to console      \n reading order logs please wait one minute
    Sleep   60 seconds
    log to console      \n reading order logs please wait one minute
    @{update_order_logs}=    read_update_order_logs     webber     Pass@123
    ${flag}     APIcalls.string_contains    ${update_order_logs}[0]    {"success":"true","errorCode":"0","errorDescription":"","order_id":"${order_id}
    Should be equal 	${flag}  ${true} 	The Update API is failed, please see the below logs \n${update_order_logs}[1]

03. To check the working of Login API
    log to console      \n Entering payload and calling the login API
    @{response_login} =  APIcalls.check_login
    Log To Console    The SID is: ${response_login}[2]
    Should Be Equal     ${response_login}[0]     success     Login API Failed, request response is ${response_login}[1]

04. To check the working of Checkin API
    log to console      \n Entering payload and calling the checkin API
    @{response_checkin} =  APIcalls.check_checkin
    Should Be Equal     ${response_checkin}[0]     success     Checkin API Failed, request response is ${response_checkin}[1]

5. To check the working of create order API in Shipsy
    log to console      \n checking the working of Create Order API in Shipsy
    @{response_create_order_shipsy} =       APIcalls.check_create_order_api_shipsy
    Log To Console    ${response_create_order_shipsy}[2]
    Should Be Equal      ${response_create_order_shipsy}[0]    true    The Create order Shipsy API has failed and the response is ${response_create_order_shipsy}[1]

6. To check the working of update order API in Shipsy
    log to console      \n checking the working of Update Order API in Shipsy
    @{response_update_order_shipsy} =       APIcalls.check_update_order_api_shipsy
    Log To Console    ${response_update_order_shipsy}[2]
    Should Be Equal      ${response_update_order_shipsy}[0]    true    The Update Order Shipsy API has failed and the response is ${response_update_order_shipsy}[1]
