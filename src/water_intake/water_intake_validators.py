from src.common.constants.activity_levels import ActivityLevels

add_water_intake_schema = {
    "type": "object",
    "properties": {
        "amount": {"type": "number"},
    },
    "required": ["amount"],
}

get_target_intake_amount_schema = {
    "type": "object",
    "properties": {
        "weight": {"type": "number"},
        "activity_level": {
            "type": "string",
            "enum": list(ActivityLevels.__members__),
        },
    },
    "required": ["weight", "activity_level"],
}
