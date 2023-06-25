# DMS 2022-2023 Backend Service

This service provides backend logic to the appliance.

## Installation

Run `./GIH-install.sh` for an automated installation.

To manually install the service:

```bash
pip3 install .
```

## Configuration

Configuration will be loaded from the root directory, subpath `/greeninhouse/cfg/config.yml`.

The configuration file is a YAML dictionary with the following configurable parameters:

- `db_connection_string` (mandatory): The string used by the ORM to connect to the database.
- `host` (mandatory): The service host.
- `port` (mandatory): The service port.
- `debug`: If set to true, the service will run in debug mode.

## Running the service

Just run `backend` as any other program.

## REST API specification

This service exposes a REST API in OpenAPI format that can be browsed at `greeninhouse/openapi/spec.yml` or in the HTTP path `/api/v1/ui/` of the service.

