login_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string", "minLength": 6},
    },
    "required": ["email", "password"],
}


register_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string", "minLength": 6},
    },
    "required": ["username", "email", "password"],
}
