# BINK API 2.0

This is a framework design in Python for the test automation of Bink's APIs.
The framework has been designed using the Pytest-BDD plugin to implement  the BDD approach.
Modules of the framework are designed in such a way that it can be reused by all merchants in any channels
This framework will provide a Regression testing suite for all available API endpoints, and also serve for Sanity,
Smoke testing & In- Sprint testing for all channels & merchants.


# Set Up
This project requires an up-to-date version of Python 3 (Currently using Python 3.9)
It also uses pipenv to manage packages.
To set up this project on your local machine:
1. Clone it from this GitLab repository [QA GitLab](git@git.bink.com:QA/bink-api-v2-automation-suite.git)
2. Run `pipenv install` from the project's root directory.
3. * Optional Step : For Django Web UI tests, install the appropriate browser and WebDriver executable
    * Current Django tests use Chrome and
     [chromedriver](https://chromedriver.chromium.org/downloads) 
4. Install Azure CLI and login to Azure for Key Vault access
    `brew install azure-cli`
    `az login`

# Running Tests

1. Test Execution:
    - Use `pytest` command 
    - Use markers '-m' to filter tests by BDD tags
    - Pass variables '--env' and '--channel' to set current environment and channel
    - The default environment is staging and default channel is bink
  
2. A few sample execution commands:
    - pytest -m "add" --env staging                    : Execute Add Journey for all merchants in staging-bink
    - pytest -m "add and iceland" --env staging        : Execute Add Journey for Iceland in staging-bink
    - pytest -m "add and enrol"                        : Execute Add & Enrol Journey for all merchants in dev-bink 

3. Commands used for nighly regression in bink in staging
    - pytest -m "bink_regression_api2.0" --env staging 
   
4. Run Database query into new server:
   Into Terminal:
   Port forward to database:   kubectl port-forward deploy/proxy-postgres 5432
   Then go to project and Run : pipenv install
                              : pipenv shell
                              : export HERMES_DATABASE_URI=$(echo $(kubectl get secret azure-pgfs -o json | jq -r .data.common_hermes | base64 --decode) | sed s/bink-uksouth-staging\.postgres\.database\.azure\.com/127\.0\.0\.1/)
                              : pytest -m "bink_regression_api2.0" --env staging 
                                
   

# Running inside Kubernetes
The project requires the following Environment Variables to function correctly:


NAME - The Human Readable Name which should be sent with reports

Example: Staging - Barclays




TEAMS_WEBHOOK - The Location to Alert to on Success/Failure

"Solutions Delivery/Alerts - Production" - https://hellobink.webhook.office.com/webhookb2/bf220ac8-d509-474f-a568-148982784d19@a6e2367a-92ea-4e5a-b565-723830bcc095/IncomingWebhook/7ae4116d366e4e5a92a65d9135a0664d/48aca6b1-4d56-4a15-bc92-8aa9d97300df

"Solutions Delivery/Alerts - QA" - https://hellobink.webhook.office.com/webhookb2/bf220ac8-d509-474f-a568-148982784d19@a6e2367a-92ea-4e5a-b565-723830bcc095/IncomingWebhook/0856493823a1484b9adfa37c942d2da4/48aca6b1-4d56-4a15-bc92-8aa9d97300df


SCHEDULE - Uses Cron Syntax, use crontab guru for help

Run at 22:30: 5 22 * * *

Run at 22:30 on Mondays: 0 22 * * 1


COMMAND - The command to run

Barclays dev run: pytest --html report.html --self-contained-html -s -m bink_regression_api2 --channel barclays

Bink dev run: pytest --html report.html --self-contained-html -s -m bink_regression_api2 --channel bink --env staging




ALERT_ON_SUCCESS - if run is successful, send report to Webhook

Default: True




ALERT_ON_FAILURE - if run fails, send report to Webhook

Default: True
