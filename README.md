# Web Push + Web Notifications PoC

This projects relies on a Python backend to implement Web Push notifications

## Build

```sh
docker build -t pywebpush-poc .
```

## Run as local server

```sh
docker run --rm --env-file .env -p 5000:5000 pywebpush-poc
```
