from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TranslatedString(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None
    se: Optional[str] = None
    dk: Optional[str] = None
    fi: Optional[str] = None


class Blog(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Any
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    modifier_id: Any
    month: str
    name: TranslatedString
    order: int
    origin_id: Any
    owner_updated_at: Any
    recently_added: bool
    starred: bool
    updated_at: Any
    url: Optional[str]
    version: int
    year: str


class Certification(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: str
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    modifier_id: Any
    month: str
    month_expire: str
    name: TranslatedString
    order: int
    organiser: TranslatedString
    origin_id: Any
    owner_updated_at: Optional[str]
    recently_added: bool
    starred: bool
    updated_at: str
    version: int
    year: str
    year_expire: str
    attachments: List


class Course(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Optional[str] = None
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    modifier_id: Any
    month: Optional[str] = None
    name: TranslatedString
    order: int
    origin_id: Any
    owner_updated_at: Optional[str]
    program: TranslatedString
    recently_added: bool
    starred: bool
    updated_at: str
    version: int
    year: Optional[str] = None
    attachments: List


class Role(BaseModel):
    field_id: str = Field(..., alias="_id")


class ProjectExperience(BaseModel):
    field_id: str = Field(..., alias="_id")
    roles: List[Role]
    diverged_from_master: bool


class CvRole(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: str
    disabled: bool
    diverged_from_master: bool
    modifier_id: Any
    name: TranslatedString
    order: int
    origin_id: Any
    owner_updated_at: Optional[str]
    recently_added: bool
    starred: bool
    starred_order: Any
    updated_at: str
    version: Optional[int]
    years_of_experience: int
    years_of_experience_offset: int
    project_experiences: List[ProjectExperience]


class Education(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Any
    degree: TranslatedString
    description: TranslatedString
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    modifier_id: Any
    month_from: Optional[str] = None
    month_to: Optional[str] = None
    order: int
    origin_id: Any
    owner_updated_at: Any
    recently_added: bool
    school: TranslatedString
    starred: bool
    updated_at: Optional[str] = None
    version: int
    year_from: str
    year_to: str
    attachments: List


class HonorsAward(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Any
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    for_work: TranslatedString
    issuer: TranslatedString
    long_description: TranslatedString
    modifier_id: Any
    month: str
    name: TranslatedString
    order: int
    origin_id: Any
    owner_updated_at: str
    recently_added: bool
    starred: bool
    updated_at: str
    version: int
    year: str


class KeyQualification(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Any
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    label: Dict[str, Any]
    long_description: TranslatedString
    modifier_id: Any
    order: int
    origin_id: Any
    owner_updated_at: Any
    recently_added: bool
    starred: bool
    tag_line: Dict[str, Any]
    updated_at: str
    version: int


class Language(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Any
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    level: TranslatedString
    modifier_id: Any
    name: TranslatedString
    order: int
    origin_id: Any
    owner_updated_at: Any
    recently_added: bool
    starred: bool
    updated_at: Optional[str]
    version: int


class Position(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: str
    description: TranslatedString
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    modifier_id: Any
    name: TranslatedString
    order: int
    origin_id: Any
    owner_updated_at: str
    recently_added: bool
    roles: list[Role] = []
    starred: bool
    updated_at: str
    version: int
    year_from: str
    year_to: str
    years_of_experience: Optional[int] = None


class Presentation(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: str
    description: TranslatedString
    disabled: bool
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    modifier_id: Any
    month: str
    order: int
    origin_id: Any
    owner_updated_at: Optional[str] = None
    recently_added: bool
    starred: bool
    updated_at: str
    version: int
    year: str


class ProjectExperienceSkill(BaseModel):
    field_id: str = Field(..., alias="_id")
    base_duration_in_years: int
    modifier_id: Any
    offset_duration_in_years: int
    order: int
    proficiency: int
    tags: TranslatedString
    total_duration_in_years: int
    version: int


class Role1(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Optional[str] = None
    cv_role_id: Optional[str] = None
    disabled: bool
    diverged_from_master: bool
    long_description: TranslatedString
    modifier_id: Any
    name: Optional[TranslatedString] = None
    order: int
    origin_id: Any
    recently_added: bool
    starred: bool
    summary: Dict[str, Any]
    updated_at: Optional[str] = None
    version: Optional[int] = None


class ProjectExperience1(BaseModel):
    field_id: str = Field(..., alias="_id")
    area_amt: Any
    area_unit: Any
    created_at: Optional[str]
    customer: TranslatedString
    customer_anonymized: Dict[str, Any]
    customer_description: Dict[str, Any]
    customer_selected: str
    customer_value_proposition: Dict[str, Any]
    description: TranslatedString
    disabled: bool
    diverged_from_master: bool
    exclude_tags: Optional[List[Any]]
    expected_roll_off_date: Any
    extent_hours: Optional[str]
    external_unique_id: Any
    industry: TranslatedString
    location_country_code: Any
    long_description: TranslatedString
    modifier_id: Any
    month_from: str
    month_to: str
    order: int
    origin_id: Any
    owner_updated_at: Optional[str]
    percent_allocated: Optional[str]
    project_experience_skills: List[ProjectExperienceSkill] = []
    project_extent_amt: Optional[str]
    project_extent_currency: Optional[str]
    project_extent_hours: Optional[str]
    project_type: TranslatedString
    recently_added: bool
    related_work_experience_id: Any
    roles: List[Role1]
    starred: bool
    total_extent_amt: Optional[str]
    total_extent_currency: Optional[str]
    total_extent_hours: Optional[str]
    updated_at: str
    version: int
    year_from: str
    year_to: str
    images: List


class TechnologySkill(BaseModel):
    field_id: str = Field(..., alias="_id")
    base_duration_in_years: int
    modifier_id: Any
    offset_duration_in_years: int
    order: int
    proficiency: int
    tags: TranslatedString
    total_duration_in_years: int
    version: Optional[int] = None


class Technology(BaseModel):
    field_id: str = Field(..., alias="_id")
    category: TranslatedString
    created_at: Optional[str]
    disabled: bool
    diverged_from_master: bool
    exclude_tags: Optional[List[Any]]
    external_unique_id: Any
    modifier_id: Any
    order: Optional[int]
    origin_id: Any
    owner_updated_at: Optional[str]
    recently_added: bool
    starred: bool
    technology_skills: List[TechnologySkill]
    uncategorized: bool
    updated_at: str
    version: int


class WorkExperience(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Optional[str] = None
    description: TranslatedString
    disabled: bool
    diverged_from_master: bool
    employer: TranslatedString
    external_unique_id: Any
    long_description: TranslatedString
    modifier_id: Any
    month_from: str
    month_to: Optional[str] = None
    order: int
    origin_id: Any
    owner_updated_at: Optional[str]
    recently_added: bool
    starred: bool
    updated_at: Optional[str] = None
    version: int
    year_from: str
    year_to: Optional[str] = None


class URL(BaseModel):
    url: str


class Image(BaseModel):
    url: str
    thumb: URL
    fit_thumb: URL
    large: URL
    small_thumb: URL


class CVResponse(BaseModel):
    field_id: str = Field(..., alias="_id")
    blogs: List[Blog] = []
    born_day: int
    born_month: int
    born_year: int
    bruker_id: str
    certifications: List[Certification]
    courses: List[Course]
    created_at: str
    custom_tag_ids: List
    cv_roles: List[CvRole]
    default: bool
    educations: List[Education]
    honors_awards: List[HonorsAward] = []
    imported_date: Any
    key_qualifications: List[KeyQualification]
    landline: Any
    languages: List[Language]
    level: Any
    locked_at: Any
    locked_until: Any
    modifier_id: Any
    name_multilang: Dict[str, Any]
    nationality: TranslatedString
    navn: str
    order: Any
    owner_updated_at: str
    owner_updated_at_significant: str
    place_of_residence: TranslatedString
    positions: List[Position] = []
    presentations: List[Presentation] = []
    project_experiences: List[ProjectExperience1]
    technologies: List[Technology]
    telefon: str
    tilbud_id: Any
    title: TranslatedString
    twitter: Optional[str] = None
    updated_at: str
    version: int
    work_experiences: List[WorkExperience]
    name: str
    user_id: str
    company_id: str
    external_unique_id: Any
    email: str
    country_code: str
    language_code: str
    language_codes: List[str]
    proposal: Any
    custom_tags: List
    updated_ago: str
    template_document_type: str
    default_word_template_id: str
    default_ppt_template_id: Any
    highlighted_roles: List
    image: Image
    can_write: bool
