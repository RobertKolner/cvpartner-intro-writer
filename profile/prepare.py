from datetime import datetime
from typing import Optional, Any

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
    "certifications": TranslatedString(int="Certifications", no="Sertifiseringer"),
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
                f"- {l(position.name)}{_duration_str(position, language)}: {l(position.description)}"
            )

    if cv.project_experiences:
        info_text_lines.append("===")
        info_text_lines.append(f"{l(s['project_experiences'])}:")
        for pe in cv.project_experiences:
            info_text_lines.append(
                f"{l(pe.customer)}{_duration_str(pe, language)}: {l(pe.description)}"
            )
            for role in pe.roles:
                info_text_lines.append(
                    f"{l(s['role'])}: {l(role.name)}. {l(role.long_description)}"
                )
            info_text_lines.append("---")

    if cv.certifications:
        info_text_lines.append("===")
        info_text_lines.append(f"{l(s['certifications'])}:")
        for cert in cv.certifications:
            info_text_lines.append(f"- {l(cert.name)}: {l(cert.long_description)}")

    if cv.technologies:
        info_text_lines.append("===")
        info_text_lines.append(f"{l(s['technologies'])}:")
        for technology in cv.technologies:
            if not l(technology.category).strip():
                continue
            skills = ", ".join(
                f"{l(skill.tags)}{_duration_str(skill, language)}"
                for skill in technology.technology_skills
            )
            info_text_lines.append(f"- {l(technology.category)}: {skills}")

    return "\n".join(info_text_lines)


def _duration_str(item: Any, language: str) -> str:
    def l(o: Optional[TranslatedString]) -> str:  # noqa: E743
        return (getattr(o, language) or "").replace("\n", " ") if o else ""

    try:
        yf = int(item.year_from)
        yt = int(item.year_to) if item.year_to else datetime.now().year
        if yt > yf:
            return f" ({yt - yf} {l(s['years'])})"

    except AttributeError:
        pass
    except ValueError:
        pass

    try:
        return (
            f" ({item.total_duration_in_years} {l(s['years'])})"
            if item.total_duration_in_years
            else ""
        )
    except AttributeError:
        pass

    try:
        return f" ({item.years_of_experience} {l(s['years'])})" if item.years_of_experience else ""
    except AttributeError:
        pass

    return ""
