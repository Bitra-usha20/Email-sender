import singleEmailsend
#bulk email sender 
def bulk_email_send(emails:list,subject:str,body:str):
    for email in emails:
        try:
            singleEmailsend.single_email_send(
                to_email=email,
                subject=subject,
                body=body
                )
        except:
            print("email send failed")