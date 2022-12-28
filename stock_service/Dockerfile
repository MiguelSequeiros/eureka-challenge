FROM python:3.10-slim

# Define ARGs 
ARG ENVIRONMENT=default

# Python logs to STDOUT
ENV PYTHONUNBUFFERED 1

# Sane defaults for pip
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY ./stock_service/requirements/ /tmp/requirements/
COPY ./stock_service .

RUN set -x \
    && buildDeps=" \
    libffi-dev \
    libpq-dev \
    gcc \
    python3-dev \
    binutils \
    openssh-client \
    apt-transport-https \
    ca-certificates \
    git \
    " \
    && runDeps="" \
    && apt-get update \
    && apt-get install -y --no-install-recommends $buildDeps \
    && apt-get install -y --no-install-recommends $runDeps \
    # Install Python dependencies
    && pip install -r /tmp/requirements/base.txt \
    && if [ $ENVIRONMENT = local ]; then \
    # Install python dev dependencies
    pip install -r /tmp/requirements/local.txt; \
    else \
    # other environment to local remove the build dependencies
    pip install -r /tmp/requirements/prd.txt; \
    apt-get remove -y $buildDeps; \
    fi \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Work dir and copy code.
WORKDIR /service
# COPY setup.cfg .
# COPY conftest.py .

EXPOSE 8000

CMD ["python", "stock_service/manage.py", "runserver", "0.0.0.0:8000"]
