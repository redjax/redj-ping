# redj-ping

Ping a host/IP address, with options to retry if the ping fails. App is configured in the [`src/config/*.toml`](src/config/) directory, or with environment variables.

## Setup

First, make sure you've set the `ENV_FOR_DYNACONF` environment variable. The app uses this to determine which settings group to load. If the environment variable is not set, the app will load the `[default]` group in `settings.toml`. This group sets initial values for available environment variables, which are overridden per-environment (`dev`/`prod`).

Optionally, if you are using [`PDM`](pdm.fming.dev/), the [`pyproject.toml`](./pyproject.toml) has scripts that pre-set the environment variable and execute the app. Use `pdm run start` to run the app with `ENV_FOR_DYNACONF=prod`, or `pdm run start-dev` to run the app with `ENV_FOR_DYNACONF=dev`.

To set the `ENV_FOR_DYNACONF` environment variable:

    * Linux
      * `export ENV_FOR_DYNACONF=dev`
    * Windows
      * `$ENV_FOR_DYNACONF = "dev"`

Instead of setting an environment variable, you can also pre-set the variable before running, i.e. (from the [`src`](src/) directory):

`$ ENV_FOR_DYNACONF=dev python -m ping_utils`

## Container setup

If running this app in a container, prepend all environment variables with `DYNACONF_`. For example, to set the `host`, your container should have an environment variable called `DYNACONF_HOST`.
