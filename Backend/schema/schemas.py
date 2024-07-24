def individual_serial(todo) -> dict:
    return{
        "id":str(todo["_id"]),
        "email": todo["query"],
        "subject":todo["response"],
        "body":todo["complete"]
    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]