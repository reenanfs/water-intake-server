from enum import Enum


class ActivityLevels(Enum):
    SEDENTARY = "sedentary"
    LIGHTLY_ACTIVE = "lightly_active"
    MODERATELY_ACTIVE = "moderately_active"
    VERY_ACTIVE = "very_active"


ACTIVITY_LEVELS = {
    "sedentary": 0.8,
    "lightly_active": 1.2,
    "moderately_active": 1.5,
    "very_active": 1.8,
}
