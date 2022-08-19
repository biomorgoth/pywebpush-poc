# Web Push + Web Notifications PoC

This projects relies on a Python backend to implement Web Push notifications

## Requirements

- Docker
- Python (for development, this project can be built and ran without having Python installed on the local environment)

## Build

```sh
docker build -t pywebpush-poc .
```

## Setup

This app requires VAPID keys in order to work properly. Such keys can be generated using the py-vapid library which is already included in `requirements.txt`.

A setup script already exists to ease the configuration:

```sh
docker run --rm pywebpush-poc python app/setup.py > .env
```

will generate a `.env` file with a valid set of VAPID keys already formatted as env vars.

## Run as local server

```sh
docker run --rm --env-file .env -p 5000:5000 pywebpush-poc
```
