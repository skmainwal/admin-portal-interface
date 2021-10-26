import json
from re import search
import re
from fastapi import APIRouter, Request
from app.api.data_routes import send_new_question_to_core, add_dummy_data, get_all_question_from_core, delete_question_from_core, update_question_to_core, add_question_sequence, get_question_sequence_from_core, update_questionSequence, delete_question_sequence, add_section_to_core, get_section_list_from_core, delete_section_from_core, update_section_to_db, add_demographic_details

from app.model import schema
import datetime

router = APIRouter()

# getting all the cancer types


@router.get("/get_cancerTypes")
def getCancerTypes(request: Request):
    json_data = [{"cancer_types": [
        {"cancer_type": "Demographic ", "short_name": "DEM"},
        {"cancer_type": "Lung ", "short_name": "LUN"}, {"cancer_type": "Head and Neck", "short_name": "HNN"}, {
            "cancer_type": "Colon ", "short_name": "COL"}, {"cancer_type": "Urogenital", "short_name": "URO"}, {"cancer_type": "Breast", "short_name": "BRE"}
    ]},
        {
        "language_types": [{"language_type": "English", "short_name": "ENG"},
                           {"language_type": "Hindi", "short_name": "HIN"},
                           {"language_type": "Kannada", "short_name": "KAN"}]
    }
    ]

    return json_data


@router.get('/get_response_data_to_process')
def getResponseAndDataToProcess(request: Request):
    json_data = [{'response_types': [
        {'response_type': 'DOB'},
        {'response_type': 'ESIC_NUMBER'},
        {'response_type': 'LANGUAGE_SELECTION'},
        {'response_type': 'MOBILE'},
        {'response_type': 'NAME'},
        {'response_type': 'NONE'},
        {'response_type': 'REFERRING_DOCTOR_NAME'},
        {'response_type': 'SINGLE_CHOICE'},
        {'response_type': 'SECTION_COUNTER'},
        {'response_type': 'TEXT'},
    ]
    },

        {'data_to_processs': [
            {'data_to_process': 'BOOLEAN'},
            {'data_to_process': 'CHILDREN'},
            {'data_to_process': 'CANCER_SELECTION'},
            {'data_to_process': 'DOB'},
            {'data_to_process': 'ESIC_NUMBER'},
            {'data_to_process': 'GENDER_SELECTION'},
            {'data_to_process': 'LANGUAGE_SELECTION'},
            {'data_to_process': 'MOBILE'},
            {'data_to_process': 'NAME'},
            {'data_to_process': 'REFERRING_DOCTOR_NAME'},
            {'data_to_process': 'SINGLE_CHOICE'},
            {'data_to_process': 'TEXT'},

        ]}

    ]

    return json_data


@router.post("/add_new_question")
def add_newQuestion(request: Request, data: schema.addNewQuestion):
    print("*******Data Came from UI********")
    print(data)
    print("********End******")
    req = send_new_question_to_core(data)
    print("*******Sent to core response********")
    print(req)
    print("************End**************")
    return"Data came, Ok"


@router.post("/get_all_questions")
def allQuestions(request: Request, data: schema.getAllQuestions):
    print("*********Query *******8")
    print(data)
    req = get_all_question_from_core(data)

    if(req != None):
        for question in req:
            Response_Option = question['response_options']
            # was sending the wrong formate to UI
            # "[{\"text\": \"Few weeks\", \"option\": \"1\", \"input_tool_tip\": \"Few weeks\"}, {\"text\": \"1 month\"
            question['response_options'] = json.loads(Response_Option)
            # req = json.loads(req[0])
            print("*******Data Came from COre********88")
            print((req))
    # print(json.loads(req.response_options))
    # print(req)

    return req


@router.delete("/delete_question")
def deleteTheQuestion(request: Request, question_id):
    print("********to delete Question***********8")
    print(question_id)
    req = delete_question_from_core(question_id)
    print(req)

    return "Question Deleted , Ok"


@router.put("/update_question")
def updateQuestion(request: Request, question_id, selected_language, data: schema.addNewQuestion):
    print(question_id)
    print(selected_language)
    print(data)
    req = update_question_to_core(question_id, selected_language, data)

    return "question updated, ok"


@router.post('/add_question_sequence')
def addQuestionSequence(request: Request, data: schema.addQuestionSequence):
    print("*******Data Came from Ui*******")
    print(data)
    print("**********End***********")
    req = add_question_sequence(data)

    return "Ok "


# @router.post("/add_dummy_question")
# def add_dummy_question(request: Request, data: schema.addDummyQuestion):
#     print("**********Dummy Data came from Ui")
#     print(data)
#     print("********End**********")
#     req = add_dummy_data(data)
#     print("*******Core response*********")
#     print(req)
#     return "Dummy Data  ,Ok"


@router.get('/get_question_sequence')
def getQuestionSequence(request: Request, cancer_type):
    print("*********Query *******8")
    # print(data)
    req = get_question_sequence_from_core(cancer_type)
    print("Data Came from CORE")
    print(req)

    if(req != None):

        for question in req:
            Last_question_list = question['last_question_list']
            Dependency_rule = question['dependency_rule']
            print("Going to send the Data")
            # print(Last_question_list)
            print((Dependency_rule))
            if(Dependency_rule != None):
                question['dependency_rule'] = json.loads(Dependency_rule)

            question['last_question_list'] = json.loads(Last_question_list)

    print("*******Data Came from COre********88")
    # print((req))
    return req


@router.put('/update_question_sequence')
def updateQuestionSequence(request: Request, last_question_asked, next_question_asked, data: schema.addQuestionSequence):
    print('Data Came from Ui')
    print(data)
    req = update_questionSequence(
        last_question_asked, next_question_asked, data)
    print(req)

    return "Ok"


@router.delete('/delete_question_sequence')
def deleteQuestionSequence(request: Request, last_question_asked, next_question_asked):
    print('Data Came from UI')
    print(last_question_asked, next_question_asked)
    req = delete_question_sequence(last_question_asked, next_question_asked)
    print(req)
    return "Ok"


@router.post('/add_section')
def add_section(resquest: Request, data: schema.addSection):
    print("DATA CAME FROM UI")
    print(data)
    req = add_section_to_core(data)
    return "Ok"


@router.get('/get_section_list')
def get_section(request: Request, section_id, selected_language):
    print("Section Id")
    print(section_id)
    req = get_section_list_from_core(section_id, selected_language)
    if(req != None):
        for question in req:
            Response_options = question['response_options']

            # print(Last_question_list)

            question['response_options'] = json.loads(Response_options)
    # print(req.json)
    return req


@router.delete('/delete_section')
def get_delete_section(request: Request, section_id, selected_language):
    print("Section_Id")
    print(section_id)
    req = delete_section_from_core(section_id, selected_language)
    return req


@router.put('/update_section_details')
def update_section_details(request: Request, question_id, selected_language, data: schema.addSection):

    print("Data Came from Ui")
    # json_data = {
    #     "question_id": data.question_id,
    #     "in_language": data.in_language,
    #     "response_type": data.response_type,
    #     "response_options": data.response_options
    # }
    print(data)
    req = update_section_to_db(question_id, selected_language, data)
    return req


@router.post('/add_demographic_question')
def add_demographic(request: Request, data: schema.addDemographic):
    req = add_demographic_details(data)

    return "Ok"
