# BINK API 2.0

This is a framework design in Python for the test automation of Bink's APIs.
The framework has been designed using the Pytest-BDD plugin to implement  the BDD approach.
Modules of the framework are designed in such a way that it can be reused by all merchants in any channels
This framework will provide a Regression testing suite for all available API endpoints, and also serve for Sanity,
Smoke testing & In- Sprint testing for all channels & merchants.


# Set Up
This project requires an up-to-date version of Python 3
It uses poetry to manage packages.
To set up this project on your local machine:
1. Clone the repo from GitHub (git@github.com:binkhq/bink-api-v2-automation-suite.git)
2. Execute `poetry shell` ,  from the project's root directory to create the  virtual environment
3. Execute `poetry install` to install depedndecies from pyproject.toml
4. Install Azure CLI and login to Azure for Key Vault access
    `brew install azure-cli`
    `az login`

# Executing Tests from Local

1. Test Execution:
    - Use `pytest` command
    - Use markers '-m' to filter tests by BDD tags
    - Pass variables '--env' to set current environment (defaulted to staging)
    - The default environment is staging and default channel is bink

2. A few sample execution commands:
    - pytest -m "add" --env staging                    : Execute Add Journey for all merchants in staging
    - pytest -m "add and viator" --env staging         : Execute Add Journey for Viator in staging
    - pytest -m "add and enrol"                        : Execute Add & Enrol Journey for all merchants in staging

3. Commands used for nighly regression in bink in staging
    - pytest -m "bink_regression_api2.0" --env staging

4. Run Database query from the test scripts:
   - Connect to Tailscale
   - Set the env variable for DB in the terminal
     `set HERMES_DATABASE_URI $(kubectl get secret azure-postgres -o json | jq -r .data.url_hermes | base64 --decode)`
     (Env variables: HERMES_DATABASE_URI, HARMONIA_DATABASE_URI, SNOWSTORM_DATABASE_URI)
   - Execute the tests as usual from local



# Executing tests from Kubernetes pods

1. Create a new corn job  : `kubectl create job --from=cronjob/pyqa-apiv2 <jobname>`
2. Execute the whole suite:
 - To run a Check the pod status - A new pod will create and it will be in '_Running_' status
 -  Once all the tests are completed the HTML result will be published in [Alerts-QA]([url](https://teams.microsoft.com/l/channel/19%3A80a305fc779e4ec5a01a1796c21b3674%40thread.skype/Alerts%20-%20QA?groupId=bf220ac8-d509-474f-a568-148982784d19&tenantId=a6e2367a-92ea-4e5a-b565-723830bcc095)) teams channel

3. Execute a subset of tests fron the newly created pod:
  - Get the pod name : `kubectl get pods`
  - Get into the pod:  `kubectl exec -it <pyqa pod name>   -- bash`
  - Idetify the subset of tests need to execute by using the tags in th.feature files
  - Execute tests from terminal using `pytest -m "<unique tag name>" --env staging`


# Scheduled Regression execution

1.  The whole suite will run based on the cron job 0 20 * * 1-5 ( Monday to Friday at 8pm)
    If any change needed in the schedule, update the same in gitops (https://github.com/binkhq/gitops/blob/master/overlays/uksouth-staging/olympus/pyqa-apiv2/cronjob.yaml)
2.  And the results will be published on  [Alerts-QA]([url](https://teams.microsoft.com/l/channel/19%3A80a305fc779e4ec5a01a1796c21b3674%40thread.skype/Alerts%20-%20QA?groupId=bf220ac8-d509-474f-a568-148982784d19&tenantId=a6e2367a-92ea-4e5a-b565-723830bcc095)) teams channel
3. The generic tag used for regression execution :_ '@bink_regression_api2'_

# Execution using Starbug

https://hellobink.atlassian.net/wiki/spaces/BD/pages/3802562640/Executing+API+v2.0+Automation+Framework+pyqa-apiv2+using+Starbug+tbc
