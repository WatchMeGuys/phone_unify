import json
from fastapi import FastAPI, Body
from fastapi.responses import Response


app = FastAPI()


@app.post("/unify_phone_from_json")
def process_unify_phone(user_data: str = Body(...)):
    """Calls the outer function to process received phone number"""
    phone_number = json.loads(user_data)
    return Response(unify_phone(phone_number), media_type="text/plain")


def unify_phone(phone: str):
    """Fuction takes phone number and unifyes it. Returns string."""
    phone_st = []
    # Clear phone number from other symbols.
    for item in phone:
        if item.isdecimal():
            phone_st.append(item)

    # Trim phone number to 10 symbols or exit if it's not standart.

    if len(phone_st) == 11 and phone_st[1] == '9':
        phone_st.pop(0)
    elif len(phone_st) == 10 and phone_st[0] == '9':
        pass
    else:
        return ''.join(phone_st)


    # finally format the phone number
    phone_formatted = (f"8 ({''.join(phone_st[0:3])}) "
        f"{''.join(phone_st[3:6])}-{''.join(phone_st[6:8])}-"
        f"{''.join(phone_st[8:10])}")

    return phone_formatted
