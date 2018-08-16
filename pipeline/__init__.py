from gaiasdk import sdk
import logging

def firstjob(arg):
    logging.info("First job has been executed!")

def main():
    logging.basicConfig(level=logging.INFO)
    jobs = []
    jobone = sdk.Job()
    jobone.title = "first job"
    jobone.handler = firstjob
    jobone.description = "This is the first python job"
    jobs.append(jobone)
    sdk.serve(jobs)