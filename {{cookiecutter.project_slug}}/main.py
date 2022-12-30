# Use this as the lambda entry point, do not add logic here, use
# {{ cookiecutter.project_slug }} package for logic.

# if you need to create clients or connections to external resources
# do so here and pass then as parameters to the code in
# {{ cookiecutter.project_slug }}

from {{ cookiecutter.project_slug }} import do_something
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(json.dumps(os.environ)) ## DO NOT USE THIS ON PRODUCTION
    logger.info('## EVENT')
    logger.info(json.dumps(event))

    return do_something()
