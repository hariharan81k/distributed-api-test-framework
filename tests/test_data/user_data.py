CREATE_USER_DATA = [
    {
        "name": "Hariharan",
        "username": "hari",
        "email": "hari@example.com"
    },
    {
        "name": "Arun",
        "username": "arun",
        "email": "arun@example.com"
    }
]

UPDATE_USER_DATA = [
    {
        "user_id": 1,
        "data": {
            "name": "Hariharan",
            "username": "hari",
            "email": "newhari@example.com"
        }
    },
    {
        "user_id": 2,
        "data": {
            "name": "Arun",
            "username": "arun",
            "email": "newarun@example.com"
        }
    }
]

PATCH_USER_DATA = [
    {
        "user_id": 1,
        "data": {
            "email": "patchhari@example.com"
        }
    },
    {
        "user_id": 2,
        "data": {
            "email": "patcharun@example.com"
        }
    }
]

DISTRIBUTED_CREATE_USER_DATA = [
    {
        "name": "Hariharan Distributed",
        "username": "hari_distributed",
        "email": "hari.distributed@example.com"
    },
    {
        "name": "Arun Distributed",
        "username": "arun_distributed",
        "email": "arun.distributed@example.com"
    }
]