from langchain_core.tools import tool

from api.myemailer.sender import send_email
from api.myemailer.inbox_reader import read_inbox
from api.ai.services import generate_email_message


@tool
def research_email(query: str):
    """
    Perform research based on query
    
    Arguments:
     - query: str - Topic of research.
     
    """
    response = generate_email_message(query)
    msg = f"Subject {response.subject}:\nBody: {response.contents}"
    return msg


@tool
def send_email_tool(subject: str, content: str, recipient: str = None, sender: str = None) -> str:
    """Send an Emmail to a receipent.

    Args:
        subject (str): Email Subject.
        content (str): Email content.
        recipient (str, optional): Email of recipient, default none means send to myself, Default is None.
        sender (str, optional): Email of sender, default none means send by myself, Default is None.
        
    Returns:
    returns string message of successfully sending mail or failure while sending mail due to error.
    """
    try:
        send_email(subject, content)
    except Exception:
        return "Failed to send mail"
    
    return "Email sent successfully"



@tool
def get_unread_mails_tool(hours_ago: int = 12) -> str:
    """Get all the unread mails from Inbox within last `hours_ago` hours.

    Args:
        hours_ago (int, optional): number of hours ago to retrieve in the inbox. Defaults to 12.
    Returns:
    A string of emails seperated by a line "-----"
    """
    try:
        messages = read_inbox(hours_ago=hours_ago, verbose=False)
    except Exception:
        return "Error getting latest emails."
    
    cleaned_msg = []
    for email in messages:
        data = email.copy()
        if "html_body" in email:
            data.pop("html_body")
        msg = ""
        for k,v in data.items():
            msg += f"{k}:\t{v}"
        cleaned_msg.append(msg)    
    
    return "\n-----\n".join(cleaned_msg)
