from datetime import datetime


def seed_bonus(cashback):
    bonus = cashback["bonus"]
    bonus.insert_many([
        {
            "name": "Primeira Faixa",
            "starting_margin": 0.00,
            "final_margin": 1000.00,
            "bonus_percentage": 10.00,
            "active": True,
            "created_by": "06909142969",
            "created_at": datetime.now(),
            "updated_by": "06909142969",
            "updated_at": datetime.now()
        },
        {
            "name": "Segunda Faixa",
            "starting_margin": 1001.00,
            "final_margin": 1500.00,
            "bonus_percentage": 15.00,
            "active": True,
            "created_by": "06909142969",
            "created_at": datetime.now(),
            "updated_by": "06909142969",
            "updated_at": datetime.now()
        },
        {
            "name": "Terceira Faixa",
            "starting_margin": 1501.00,
            "final_margin": 99999999.99,
            "bonus_percentage": 20.00,
            "active": True,
            "created_by": "06909142969",
            "created_at": datetime.now(),
            "updated_by": "06909142969",
            "updated_at": datetime.now()
        }
    ])
