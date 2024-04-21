from datetime import datetime

from src.encoding import UTF_8

INSIGHT_GENIE_PROMPT_PATH = "src/prompts/insight_genie_prompt.md"

CURRENT_DATE_VARIABLE = "{{CURRENT_DATE}}"


def get_insight_genie_prompt():
    with open(INSIGHT_GENIE_PROMPT_PATH, "r", encoding=UTF_8) as prompt:
        current_date = datetime.today().date().isoformat()
        return prompt.read().replace(CURRENT_DATE_VARIABLE, current_date)
