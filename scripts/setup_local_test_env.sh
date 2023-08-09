#!/bin/bash

# Scripts args
RUN=${1}

ROOT_DIR="$HOME/dev"
TESTING_DIR="${ROOT_DIR}/e2e"
BANK_TOOLS_DIR="${ROOT_DIR}/bank-tools"
DB_USERNAME=postgres
DB_PASSWORD=pass
DB_PORT=5438

BASE_DB_URI="postgresql://$DB_USERNAME:$DB_PASSWORD@localhost:$DB_PORT"
BASE_DB_URI_PSYCOPG="postgresql+psycopg://$DB_USERNAME:$DB_PASSWORD@localhost:$DB_PORT"

setup_projects() {
  HERMES_ENV_FILE=$(
        cat <<EOF
HERMES_DATABASE_URL=postgres://postgres:pass@localhost:5438/hermes
HERMES_DATABASE_HOST=localhost
HERMES_DATABASE_PORT=5438
MIDAS_URL=http://0.0.0.0:8001
MASTER_LOG_LEVEL=INFO
UBIQUITY_LOG_LEVEL=INFO
METIS_URL=http://127.0.0.1:8095
VAULT_URL=https://uksouth-dev-2p5g.vault.azure.net/
SSO_OFF=True
LOCAL_SECRETS=False
PROMETHEUS_LOG_LEVEL=ERROR
HERMES_LOCAL=True
JSON_LOGGING=False

EOF
    )


ANGELIA_ENV_FILE=$(
        cat <<EOF

LOG_LEVEL=INFO
LOCAL_SECRETS=True
LOCAL_SECRETS_PATH=example_local_secrets.json
POSTGRES_READ_DSN=postgresql://postgres@127.0.0.1:5438/hermes
POSTGRES_WRITE_DSN=postgresql://postgres@127.0.0.1:5438/hermes
RABBIT_PASSWORD=guest
RABBIT_USER=guest
RABBIT_HOST=127.0.0.1
RABBIT_PORT=5672
HERMES_URL=http://127.0.0.1:8000
METRICS_SIDECAR_DOMAIN=localhost
METRICS_PORT=4000
PERFORMANCE_METRICS=0
VAULT_URL=https://uksouth-dev-2p5g.vault.azure.net/
QUERY_LOGGING=False
JSON_LOGGING=False

EOF
    )

# Set up services
echo "- Setting up services in directory: $TESTING_DIR"

# Hermes
cd $TESTING_DIR

if [[ ! -d "hermes" ]] ; then
  echo "- Cloning Hermes..." && git clone "git@github.com:binkhq/hermes.git"
  fi

cd hermes

echo "- (Hermes) Checking out and updating master branch..."
git checkout master
git pull --ff-only origin master

echo "- (Hermes) Synching .env and pipenv..."
echo "$HERMES_ENV_FILE" > .env && pipenv sync --dev


# Angelia
cd $directory

if [[ ! -d "Angelia" ]] ; then
  echo "- Cloning angelia..." && git clone "git@github.com:binkhq/angelia.git"
  fi

cd angelia

echo "- (Angelia) Checking out and updating master branch..."
git checkout master
git pull --ff-only origin master

echo "- (Angelia) Synching .env and pipenv..."
echo "$ANGELIA_ENV_FILE" > .env && pipenv sync --dev
}

run_services() {
  SCRIPT_PATH=$BANK_TOOLS_DIR/wallet-stack/run-wallet-stack.sh
  echo "Running services with $SCRIPT_PATH"
  exec $SCRIPT_PATH
}


if [[ $RUN = "services" ]]; then
    run_services
else
    setup_projects
    # run_services
fi