import cohere
from controller.search_controller import search


def ask(user, system, cohere_key):
    co = cohere.Client(api_key=cohere_key)

    context = search(user)
    new_user = f"""
        ## Stories: {context}.

        ## Crisis: {user}

        ## Solutions
            """

    response = [
        co.chat(
            message=new_user,
            preamble=system,
            temperature=0.7,
            model="command-r-plus",
        )
    ]
    for chat_obj in response:
        return chat_obj.text
