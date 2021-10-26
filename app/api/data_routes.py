import os

from fastapi import APIRouter
import requests
import json

from requests.api import delete

router = APIRouter()


def send_new_question_to_core(data):
    print("********Sending the new ques. to core********")

    # print(json.dumps(data.response_options))

    json_data = {
        "question_id": data.question_id,
        "in_language": data.in_language,
        "question": data.question,
        "question_in_brief": data.question_in_brief,
        "response_type": data.response_type,
        "response_options": data.response_options,
        "data_to_process": data.data_to_process,
        "section_count": data.section_count,
        "section_name": data.section_name,
        "total_sections": data.total_sections,
        "sub_section_count": data.sub_section_count,
        "question_count": data.question_count,
        "sub_section_name": data.sub_section_name,
        "total_sub_sections": data.total_sub_sections}
    print(json_data)
    print("*************End*************")

    endpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/insert_new_question"
    req = requests.post(endpoint, json=json_data)
    print("*******Core Response******")
    print(req)
    print("*********End*******")

    return "Sent data to core"


def get_all_question_from_core(data):
    print("******Request body********8")
    print(data)
    json_data = {"cancer_type": data.cancer_type,
                 "selected_language": data.selected_language
                 }

    endpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/get_all_question"

    req = requests.post(endpoint, json=json_data)
    print("*******Core Response******")
    # print(req.json())
    print("*********End*******")
    return req.json()


def add_dummy_data(data):
    json_data = {"question_id": data.question_id,
                 "in_language": data.in_language,
                 "question": data.question}

    enpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/get_dummy_data"
    req = requests.post(enpoint, json=json_data)
    print("********Dummy data Core response********")
    print(req)
    return "Dumyy data came from core"


def delete_question_from_core(question_id):
    json_data = {"question_id": question_id}
    print("*******Sending to core********8")
    print(json_data)

    enpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/delete_question"
    req = requests.post(enpoint, json=json_data)
    print("********Dummy data Core response********")
    print(req)
    return "Dumyy data came from core"


def update_question_to_core(question_id, selected_language, data):
    # json_data = {"question_id": question_id}
    print("*******Sending to core********")
    print(selected_language)
    print(question_id)
    print(data)
    json_data = {
        "question_id": data.question_id,
        "in_language": data.in_language,
        "question": data.question,
        "question_in_brief": data.question_in_brief,
        "response_type": data.response_type,
        "response_options": data.response_options,
        "data_to_process": data.data_to_process,
        "section_count": data.section_count,
        "section_name": data.section_name,
        "total_sections": data.total_sections,
        "sub_section_count": data.sub_section_count,
        "question_count": data.question_count,
        "sub_section_name": data.sub_section_name,
        "total_sub_sections": data.total_sub_sections}
    print(json_data)

    enpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/update_question?question_id={} &&selected_language={}".format(
        question_id, selected_language)
    req = requests.put(enpoint, json=json_data)
    # print("********Dummy data Core response********")
    # print(req)
    return "Dumyy data came from core"


def add_question_sequence(data):
    print(data.last_question_list)
    print(data)
    json_data = {
        "last_question_list": data.last_question_list,
        "dependency_rule": data.dependency_rule,
        "next_question": data.next_question,
        "is_first_question": data.is_first_question,
        "is_last_question": data.is_last_question
    }
    print("****Adding question sequence*********")
    print(json_data)
    print("********End***********")
    enpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/add_question_sequence"
    req = requests.post(enpoint, json=json_data)
    print("********Dummy data Core response********")
    print(req)

    return "Sending to the core "


def get_question_sequence_from_core(cancer_type):
    print("******Request body********8")
    # print(data)
    # json_data = {"cancer_type": data.cancer_type,
    #              "selected_language": data.selected_language
    #  }

    endpoint = os.getenv("CORE_SERVICE_ENDPOINT") + \
        "/data/get_question_sequence?cancer_type={}".format(
            cancer_type)

    req = requests.get(endpoint)
    print("*******Core Response******")
    # print(req.json())
    print("*********End*******")
    return req.json()


def update_questionSequence(last_question_asked, next_question_asked, data):
    print("Sending to the core")
    print(data)
    json_data = {
        "last_question_list": data.last_question_list,
        "dependency_rule": data.dependency_rule,
        "next_question": data.next_question,
        "is_first_question": data.is_first_question,
        "is_last_question": data.is_last_question
    }
    enpoint = os.getenv("CORE_SERVICE_ENDPOINT") + "/data/update_question_sequence?last_question_asked={}&&next_question_asked={}".format(
        last_question_asked, next_question_asked)
    req = requests.post(enpoint, json=json_data)
    print("********Dummy data Core response********")
    print(req)

    return "Sending to the core "


def delete_question_sequence(last_question_asked, next_question_asked):
    print(last_question_asked, next_question_asked)
    enpoint = os.getenv("CORE_SERVICE_ENDPOINT") + "/data/delete_question_sequence?last_question_asked={}&&next_question_asked={}".format(
        last_question_asked, next_question_asked)
    req = requests.delete(enpoint)
    print("********Dummy data Core response********")
    print(req)

    return "Sending to the core "


def add_section_to_core(data):
    json_data = {
        "question_id": data.question_id,
        "in_language": data.in_language,
        "response_type": data.response_type,
        "response_options": data.response_options
    }
    # json_data = json.dumps(data)

    enpoint = os.getenv("CORE_SERVICE_ENDPOINT") + "/data/add_section"
    req = requests.post(enpoint, json=json_data)
    print("********Dummy data Core response********")
    print(req)

    return req


def get_section_list_from_core(section_id, selected_language):
    enpoint = os.getenv("CORE_SERVICE_ENDPOINT") + \
        "/data/get_section_list?section_id={} &selected_language={}".format(
            section_id, selected_language)
    req = requests.get(enpoint)
    print("********Dummy data Core response********")
    print(req.json())

    return req.json()


def delete_section_from_core(section_id, selected_language):
    enpoint = os.getenv("CORE_SERVICE_ENDPOINT") + \
        "/data/delete_section?section_id={} &&selected_language={}".format(
            section_id, selected_language)
    req = requests.delete(enpoint)
    print("********Dummy data Core response********")
    print(req)

    return req.json()

    return section_id


def update_section_to_db(question_id, selected_language, data):
    print("Data")
    json_data = {
        "question_id": data.question_id,
        "in_language": data.in_language,
        "response_type": data.response_type,
        "response_options": data.response_options
    }
    print(json_data)
    # return 'Ok'
    endpoint = os.getenv("CORE_SERVICE_ENDPOINT")+"/data/update_section_details?question_id={}&selected_language={}".format(
        question_id, selected_language)
    print("EndPoint")
    print(endpoint)
    req = requests.put(endpoint, json=json_data)
    print("REquest")
    print(req)
    return "ok"


def add_demographic_details(data):
    json_data = {
        "question_id": data.question_id,
        "in_language": data.in_language,
        "question": data.question,
        "question_in_brief": data.question_in_brief,
        "response_type": data.response_type,
        "response_options": data.response_options,
        "data_to_process": data.data_to_process
    }
    endpoint = os.getenv("CORE_SERVICE_ENDPOINT") + \
        "/data/add_demographic_question"
    print("EndPoint")
    print(endpoint)
    req = requests.post(endpoint, json=json_data)
    print("REquest")
    print(req)
    return "ok"
