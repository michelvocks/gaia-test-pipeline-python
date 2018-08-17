from gaiasdk import sdk
import logging

def firstjob(args):
    for arg in args:
        logging.info("Key:" + str(arg.key) + ";Value:" + str(arg.value))

def secondjob(args):
    for arg in args:
        logging.info("Key:" + str(arg.key) + ";Value:" + str(arg.value))

def main():
    logging.basicConfig(level=logging.INFO)
    jobs = []
    jobone = sdk.Job("first job", "First declared python job.", firstjob)
    argVault = sdk.Argument("", sdk.InputType.VaultInp, "dbpassword")
    jobone.args.append(argVault)
    jobtwo = sdk.Job("second job", "Second declared python job with param", secondjob)
    argParam = sdk.Argument("Type in your username.", sdk.InputType.TextFieldInp, "username")
    jobtwo.args.append(argParam)
    jobs.append(jobone)
    jobs.append(jobtwo)
    sdk.serve(jobs)