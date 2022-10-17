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
    Should Be Equal     ${response_login}[0]     success     Login API Failed, request response is ${response_login}[1]

04. To check the working of Checkin API
    log to console      \n Entering payload and calling the checkin API
    @{response_checkin} =  APIcalls.check_checkin
    Should Be Equal     ${response_checkin}[0]     success     Checkin API Failed, request response is ${response_checkin}[1]

05. To check the working of Pull Order API
    log to console      \n Entering payload and calling the Pull order API
    @{response_checkin} =  APIcalls.check_get_order_api
    Should Be Equal     ${response_checkin}[0]     success     Checkin API Failed, request response is ${response_checkin}[1]

06. To check working of Accept Order API
    log to console      \n Entering payload and calling the Accept Order API
    @{response_order_allocated} =   APIcalls.check_order_allocated_api
    Should Be Equal     ${response_order_allocated}[0]     success     Order Allocated API Failed, request response is ${response_order_allocated}[1]

07. To check the order status in DB after Accepting the order
    ${order_status_in_DB} =         APIcalls.check_order_status_in_DB
    log to console      \n checking the order status after Accepting the order
    Should Be Equal     ${order_status_in_DB}     3     The order_status in the DB after allocating the order is not 3 but ${order_status_in_DB}

08. To check working of Rider Reached to Pickup Point API
    log to console      \n Entering payload and calling the Rider Reached to Pickup Point (Merchant) API
    @{response_order_reached} =   APIcalls.check_order_reached_api
    Should Be Equal     ${response_order_reached}[0]     success     Order Allocated API Failed, request response is ${response_order_reached}[1]

09. To check the order status in DB after the Rider Reaches to Pickup Point
    log to console      \n checking the order status after the Rider Reaches to Pickup Point (Merchant)
    ${order_status_in_DB} =         APIcalls.check_order_status_in_DB
    Should Be Equal     ${order_status_in_DB}     4     The order_status in the DB after the order reaches is not 4 but ${order_status_in_DB}

10. To check working of Order Picked up API
    log to console      \n Entering payload and calling the Order Picked up API
    @{response_order_to_deliver} =   APIcalls.check_order_to_deliver_api
    Should Be Equal     ${response_order_to_deliver}[0]     success     Order Picked up API Failed, request response is ${response_order_to_deliver}[1]
    log to console      The order to deliver API is successfully passed

11. To check the order status in DB after the Order is Picked up
    log to console      \n checking the order status after the order is picked
    ${order_status_in_DB} =         APIcalls.check_order_status_in_DB
    Should Be Equal     ${order_status_in_DB}     5     The order_status in the DB after the order is picked is not 5 but ${order_status_in_DB}

12. To check working of Order Full Delivery API
    log to console      \n Entering payload and calling the Full Delivery API
    @{response_order_full_delivery_prepaid} =       APIcalls.check_order_full_delivery_prepaid_api
    Should Be Equal     ${response_order_full_delivery_prepaid}[0]     success     Order full Delivery Prepaid API Failed, request response is ${response_order_full_delivery_prepaid}[1]
    log to console      The order full delivery prepaid API is successfully passed

13. To check the order status in DB after the order full deliver API is completed
    log to console      \n checking the order status after the order full delivered
    ${order_status_in_DB} =         APIcalls.check_order_status_in_DB
    Should Be Equal     ${order_status_in_DB}     6     The order_status in the DB after the order is picked is not 6 but ${order_status_in_DB}
#
14. To check the working of create order API in Shipsy
    log to console      \n checking the working of Create Order API in Shipsy
    @{response_create_order_shipsy} =       APIcalls.check_create_order_api_shipsy
    Log To Console    ${response_create_order_shipsy}[2]
    Should Be Equal      ${response_create_order_shipsy}[0]    true    The Create order Shipsy API has failed and the response is ${response_create_order_shipsy}[1]

15. To check the working of update order API in Shipsy
    log to console      \n checking the working of Update Order API in Shipsy
    @{response_update_order_shipsy} =       APIcalls.check_update_order_api_shipsy
    Log To Console    ${response_update_order_shipsy}[2]
    Should Be Equal      ${response_update_order_shipsy}[0]    true    The Update Order Shipsy API has failed and the response is ${response_update_order_shipsy}[1]
