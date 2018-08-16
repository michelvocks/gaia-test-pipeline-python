from gaiasdk import sdk
import logging

def firstjob(arg):
    logging.info("DBPassword:" + str(arg.value))

def secondjob(arg):
    logging.info("Username:" + str(arg.value))

def main():
    logging.basicConfig(level=logging.INFO)
    jobs = []
    jobone = sdk.Job()
    jobone.title = "first job"
    jobone.handler = firstjob
    jobone.description = "This is the first python job"
    argVault = sdk.Argument()
    argVault.inputType = sdk.InputType.VaultInp
    argVault.key = "dbpassword"
    jobone.args.append(argVault)
    argParam = sdk.Argument()
    argParam.description = "Type in your username."
    argParam.inputType = sdk.InputType.TextFieldInp
    argParam.key = "username"
    jobtwo = sdk.Job()
    jobtwo.title = "second job"
    jobtwo.handler = secondjob
    jobtwo.description = "Second python job with param"
    jobtwo.args.append(argParam)
    jobs.append(jobone)
    jobs.append(jobtwo)
    sdk.serve(jobs)