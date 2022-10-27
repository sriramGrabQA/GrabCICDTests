import time

import requests
import payload
import datetime as datetime
import database
import Constants


def check_create_order_SDP(env):
    if env == 'SIT':
        create_order_sdp = Constants.SITSDPCREATETRIP
    requests.post(create_order_sdp, data=payload.create_body_sdp)
    return payload.sdp_trip_id


def check_create_order(env):
    if env == 'SIT':
        create_order_api = Constants.SITCREATEORDERAPI
    requests.post(create_order_api, data=payload.create_body, headers=payload.create_headers)
    return payload.trip_id


def check_update_order(env):
    if env == 'SIT':
        update_order_api = Constants.SITUPDATEORDERAPI
    requests.post(update_order_api, data=payload.update_body, headers=payload.update_headers)
    return payload.trip_id


def read_create_order_logs(env):
    if env == 'SIT':
        url = Constants.SITWEBSERVICELOG
    url = url + str(datetime.date.today()) + '_' + datetime.datetime.now().strftime(
        "%H") + '_CreateOrderQueueDetails.txt'
    r = requests.get(url, auth=(Constants.SITWEBSERVICELOGUSERNAME, Constants.SITWEBSERVICELOGPASSWORD))
    page = r.content
    return [page, url]


def read_update_order_logs(env):
    if env == 'SIT':
        url = Constants.SITWEBSERVICELOG
    url = url + str(datetime.date.today()) + '_' + datetime.datetime.now().strftime(
        "%H") + '_updateOrderItemQueue.txt'
    r = requests.get(url, auth=(Constants.SITWEBSERVICELOGUSERNAME, Constants.SITWEBSERVICELOGPASSWORD))
    page = r.content
    return [page, url]


def string_contains(first, second):
    flag = False

    if str(second) in str(first):
        flag = True

    return bool(flag)


def check_login(env):
    if env == 'SIT':
        login_api = Constants.SITAPI
    print("Entering payload and calling the login API")
    response_login = requests.post(login_api, data=payload.login_payload, headers=payload.login_header).json()
    sid = response_login["sid"]
    return [response_login["response"], response_login, sid]


# def get_sid():
#     login_api = Constants.SITAPI
#     response_login = requests.post(login_api, data=payload.login_payload, headers=payload.login_header).json()
#     sid = response_login["sid"]
#     return sid

def check_checkin(env):
    if env == 'SIT':
        checkin_api = Constants.SITAPI
    print("Entering payload and calling the checkin API")
    sid = check_login(env)
    checkin_data = payload.checkin_payload.replace("{id}", sid[2])
    response_checkin = requests.post(checkin_api, data=checkin_data, headers=payload.checkin_header).json()
    return [response_checkin["response"], response_checkin]


def check_get_order_api(env):
    if env == 'SIT':
        get_order_api = Constants.SITAPI
    sid = check_login()
    get_order_body = payload.get_order_payload1.replace("{id}", sid[2])
    response_get_order = requests.post(get_order_api, data=get_order_body, headers=payload.get_order_header).json()
    return [response_get_order["response"], response_get_order]


def check_order_allocated_api(env):
    if env == 'SIT':
        order_allocated_api = Constants.SITAPI
    print("Entering payload and calling the Order Allocated API")
    oid = database.B2C_execute_query(
        "SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    # print(oid[0][0])
    order_allocated_body = payload.order_allocated_payload.replace("{order_id}", str(oid[0][0]))
    response_order_allocated = requests.post(order_allocated_api, data=order_allocated_body,
                                             headers=payload.order_allocated_header).json()
    return [response_order_allocated["response"], response_order_allocated]


def get_oid():
    oid = database.B2C_execute_query(
        "SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    return oid[0][0]


def check_order_status_in_DB():
    response = database.B2C_execute_query(
        "SELECT order_status FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    return str(response[0][0])


def get_otp_from_DB():
    response = database.B2C_execute_query(
        "SELECT SUBSTRING((SELECT CAST(security_codes AS CHARACTER ) FROM tbl_order_main WHERE pos_order_id='" + payload.trip_id + "'), 6 , 4)")
    otp = response
    return otp


def check_order_reached_api(env):
    if env == 'SIT':
        order_reached_api = Constants.SITAPI
    print("Entering payload and calling the Order Reached API")
    oid = database.B2C_execute_query(
        "SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    # print(oid[0][0])
    order_reached_body = payload.order_reached_payload.replace("{order_id}", str(oid[0][0]))
    response_order_reached = requests.post(order_reached_api, data=order_reached_body,
                                           headers=payload.order_reached_header).json()
    return [response_order_reached["response"], response_order_reached]


def check_order_to_deliver_api(env):
    if env == 'SIT':
        order_to_deliver_api = Constants.SITAPI
    # print("Entering payload and calling the Order Reached API")
    oid = database.B2C_execute_query(
        "SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    # print(oid[0][0])
    order_to_deliver_body1 = payload.order_to_deliver_payload1.replace("{oid}", str(oid[0][0]))
    sid = check_login()
    order_to_deliver_body = order_to_deliver_body1.replace("{sid}", sid[2])
    response_order_to_deliver = requests.post(order_to_deliver_api, data=order_to_deliver_body,
                                              headers=payload.order_to_deliver_header).json()
    return [response_order_to_deliver["response"], response_order_to_deliver]


def check_order_full_delivery_prepaid_api(env):
    if env == 'SIT':
        order_full_delivery_prepaid_api = Constants.SITAPI
    print("Entering payload and calling the Order full delivery prepaid")
    oid = database.B2C_execute_query(
        "SELECT OID FROM tbl_order_main WHERE pos_order_id like '%" + payload.trip_id + "%'")
    # print(oid[0][0])
    otp = get_otp_from_DB()
    print(otp)
    order_full_delivery_prepaid_body2 = payload.order_full_delivery_prepaid_payload1.replace("{oid}", str(oid[0][0]))
    sid = check_login()
    # sid = "42329e6f3b7e2fd1748a1db105c6fc1b0cc"
    order_full_delivery_prepaid_body1 = order_full_delivery_prepaid_body2.replace("{sid}", sid[2])
    order_full_delivery_prepaid_body = order_full_delivery_prepaid_body1.replace("{otp}", str(otp[0][0]))
    print(order_full_delivery_prepaid_body)
    print(payload.order_full_delivery_prepaid_payload)
    response_order_full_delivery_prepaid = requests.post(order_full_delivery_prepaid_api,
                                                         data=order_full_delivery_prepaid_body,
                                                         headers=payload.order_full_delivery_prepaid_header).json()
    return [response_order_full_delivery_prepaid["response"], response_order_full_delivery_prepaid]


def check_create_order_api_shipsy(env):
    if env == 'SIT':
        host = Constants.SITHOST
    shipsy_create_order_api = host + "Clientapi/Digitalcalls/createtripforshipsy"
    response_create_order_api_shipsy = requests.post(shipsy_create_order_api, data=payload.shipsy_create_order_body,
                                                     headers=payload.shipsy_create_order_header).json()
    return [response_create_order_api_shipsy["success"], response_create_order_api_shipsy, payload.shipsy_trip_id]


def check_update_order_api_shipsy(env):
    if env == 'SIT':
        host = Constants.SITHOST
    shipsy_update_order_api = host + "Clientapi/Digitalcalls/updatetripforshipsy"
    response_update_order_api_shipsy = requests.post(shipsy_update_order_api, data=payload.shipsy_update_order_body,
                                                     headers=payload.shipsy_update_order_header).json()
    return [response_update_order_api_shipsy["success"], response_update_order_api_shipsy, payload.shipsy_trip_id]
