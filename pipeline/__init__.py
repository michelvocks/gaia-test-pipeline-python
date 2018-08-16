from gaiasdk import sdk

def firstjob(arg):
    print "First job has been executed!"

def main():
    jobs = []
    jobone = sdk.Job()
    jobone.title = "first job"
    jobone.handler = firstjob
    jobone.description = "This is the first python job"
    jobs.append(jobone)
    sdk.serve(jobs)