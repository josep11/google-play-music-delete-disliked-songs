from subprocess import call
import os


def prepareStringForCLI(string):
    return '"' + string + '"'


def tryToSendEmail(destEmail, title, content):
    sgDir = os.getenv('SENDGRID_DIR')
    if not sgDir:
        print("SENDGRID_DIR environment variable is not set. Aborting")
        return 1

    destEmail = prepareStringForCLI(destEmail)
    title = prepareStringForCLI(title)
    content = prepareStringForCLI(content)

    cmd = "node " + os.path.join(sgDir, "send_email.js") + ' ' + ' '.join([destEmail, title, content])
    # print(cmd)
    os.system(cmd)
    return 0
