from datetime import datetime

from bcrypt import gensalt, hashpw


def seed_resellers(cashback):
    """Seed initial resellers"""
    resellers = cashback["resellers"]
    resellers.insert_many([
        {
            "name": "Alex",
            "last_name": "Volnei Galante",
            "cpf": "06909142969",
            "email": "alex@cashback.com",
            "password": hashpw("123456".encode('utf-8'), gensalt(12)),
            "active": True,
            "roles": ["manager", "support"],
            "purchases": [
                {
                    "code": "V00001",
                    "value": 1399.85,
                    "date": datetime.now(),
                    "status_code": 1,
                    "status_description": "Aprovado",
                    "created_by": "06909142969",
                    "created_at": datetime.now()
                },
                {
                    "code": "V00002",
                    "value": 75.80,
                    "date": datetime.now(),
                    "status_code": 1,
                    "status_description": "Aprovado",
                    "created_by": "06909142969",
                    "created_at": datetime.now()
                },
                {
                    "code": "V00003",
                    "value": 3.99,
                    "date": datetime.now(),
                    "status_code": 1,
                    "status_description": "Aprovado",
                    "created_by": "06909142969",
                    "created_at": datetime.now()
                }
            ],
            "created_by": "06909142969",
            "created_at": datetime.now(),
            "updated_by": "06909142969",
            "updated_at": datetime.now()
        },
        {
            "name": "Bill",
            "last_name": "Gates",
            "cpf": "15350946056",
            "email": "bill@cashback.com",
            "password": hashpw("123456".encode('utf-8'), gensalt(12)),
            "active": True,
            "roles": ["manager", "support"],
            "purchases": [
                {
                    "code": "V00034",
                    "value": 35.66,
                    "date": datetime.now(),
                    "status_code": 1,
                    "status_description": "Aprovado",
                    "created_by": "06909142969",
                    "created_at": datetime.now()
                }
            ],
            "created_by": "06909142969",
            "created_at": datetime.now(),
            "updated_by": "06909142969",
            "updated_at": datetime.now()
        },
    ])
