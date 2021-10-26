from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class addNewQuestion(BaseModel):
    question_id: str
    in_language: Optional[str] = ""
    question: Optional[str] = ""
    question_in_brief: Optional[str] = ""
    response_type: Optional[str] = ""
    response_options: List[dict] = []
    data_to_process: Optional[str] = ""
    section_count: Optional[str] = ""
    section_name: Optional[str] = ""
    total_sections: Optional[str] = ""
    sub_section_count: Optional[str] = ""
    question_count: Optional[str] = ""
    sub_section_name: Optional[str] = ""
    total_sub_sections: Optional[str] = ""

    class Config:
        orm_mode = True


class getAllQuestions(BaseModel):
    cancer_type: Optional[str] = ""
    selected_language: Optional[str] = ""


class deleteTheQuestion(BaseModel):
    question_id: str


class addQuestionSequence(BaseModel):
    last_question_list: List[str]
    dependency_rule: List[dict]
    next_question: str
    is_first_question: str
    is_last_question: str


class addDummyQuestion(BaseModel):
    question_id: str = ""
    in_language: Optional[str] = ""
    question: Optional[str] = ""

    class Config:
        orm_mode = True


class addSection(BaseModel):
    question_id: str = ""
    in_language: str = ""
    response_type: str = ""
    response_options: List[dict] = []


class addDemographic(BaseModel):
    question_id: str
    in_language: Optional[str] = ""
    question: Optional[str] = ""
    question_in_brief: Optional[str] = ""
    response_type: Optional[str] = ""
    response_options: List[dict] = []
    data_to_process: Optional[str] = ""
