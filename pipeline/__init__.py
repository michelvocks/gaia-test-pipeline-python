from gaiasdk import sdk
import logging

def firstjob(self, args):
    logging.info("first job has been started")
    for arg in args:
        logging.info("Key:" + str(arg.key) + ";Value:" + str(arg.value))

def secondjob(self, args):
    logging.info("second job has been started")
    for arg in args:
        logging.info("Key:" + str(arg.key) + ";Value:" + str(arg.value))

def main():
    logging.basicConfig(level=logging.INFO)
    argVault = sdk.Argument("", sdk.InputType.VaultInp, "dbpassword")
    jobone = sdk.Job("first job", "First declared python job.", firstjob, None, [argVault])
    argParam = sdk.Argument("Type in your username.", sdk.InputType.TextFieldInp, "username")
    jobtwo = sdk.Job("second job", "Second declared python job with param", secondjob, None, [argParam])
    sdk.serve([jobone, jobtwo])

main()