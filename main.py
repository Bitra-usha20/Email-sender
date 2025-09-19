import singleEmailsend
import BulkEmailSend
if __name__== "__main__":
    subject=input("Enter subject: ")
    body=input("Enter Body : ")
    choice=int(input("select your choice \n 1.single email send \n 2.Bulk email send \n"))
    if choice==1:
        email=input("please Enter Receiver Email :").strip()
        singleEmailsend.single_email_send(
        to_email=email,
        subject=subject, #this is keyword argument type pasing the values
        body=body
    )
    elif choice==2:
        emails=input("enter email separted by comma:").split(',')
        BulkEmailSend.bulk_email_send(
            emails=emails,
            subject=subject,
            body=body
        )




