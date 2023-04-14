from datetime import datetime
from typing import Optional

from dateutil.relativedelta import relativedelta

from cvpartner.types.cv import TranslatedString, CVResponse


s = {
    "name": TranslatedString(int="Name", no="Navn"),
    "age": TranslatedString(int="Age", no="Alder"),
    "position": TranslatedString(int="Position", no="Stillingsbetegnelse"),
    "years": TranslatedString(int="year(s)", no="år"),
    "project_experiences": TranslatedString(int="Project experiences", no="Prosjekterfaring"),
    "role": TranslatedString(int="Role", no="Rolle"),
    "technologies": TranslatedString(int="Technologies", no="Teknologier"),
}


def prepare_profile(cv: CVResponse, language: str) -> str:
    def l(o: Optional[TranslatedString]) -> str:  # noqa: E743
        return (getattr(o, language) or "").replace("\n", " ") if o else ""

    age = relativedelta(datetime.now(), datetime(cv.born_year, cv.born_month, cv.born_day))
    info_text_lines: list[str] = [f"{l(s['name'])}: {cv.name}", f"{l(s['age'])}: {age.years}"]

    if cv.positions:
        info_text_lines.append("===")
        info_text_lines.append(f"{l(s['position'])}:")
        for position in cv.positions:
            info_text_lines.append(
                f"- {l(position.name)} ({position.years_of_experience} {l(s['years'])})"
            )
            for role in position.roles:
                info_text_lines.append(f"  - {l(role.name)}: {l(role.long_description)}")

    if cv.project_experiences:
        info_text_lines.append("===")
        info_text_lines.append(f"{l(s['project_experiences'])}:")
        for project_experience in cv.project_experiences:
            info_text_lines.append(
                f"{l(project_experience.customer)}: {l(project_experience.description)}"
            )
            for role in project_experience.roles:
                info_text_lines.append(
                    f"{l(s['role'])}: {l(role.name)}. {l(role.long_description)}"
                )
                info_text_lines.append("")

    if cv.technologies:
        info_text_lines.append("===")
        info_text_lines.append(f"{l(s['technologies'])}:")
        for technology in cv.technologies:
            skills = ", ".join(
                f"{l(skill.tags)} ({skill.total_duration_in_years} {l(s['years'])})"
                for skill in technology.technology_skills
            )
            info_text_lines.append(f"- {l(technology.category)}: {skills}")

    return "\n".join(info_text_lines)
