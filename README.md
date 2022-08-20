# Web Push + Web Notifications PoC

This projects relies on a Python backend to implement Web Push notifications.

Please take in consideration that this is a simple project that aims to prove the effectivity of the pywebpush + Web Push API among other technologies. **This is not a production-ready implementation.**

## Requirements

- Docker
- Python (for development, this project can be built and ran without having Python installed on the local environment)

## Build

```sh
docker build -t pywebpush-poc .
```

## Setup

This app requires VAPID keys in order to work properly. Such keys can be generated using the [py_vapid](https://github.com/web-push-libs/vapid/tree/main/python) library which is already included in `requirements.txt`.

A setup script already exists to ease the configuration:

```sh
docker run --rm pywebpush-poc python app/setup.py > .env
```

will generate a `.env` file with a valid set of VAPID keys already formatted as env vars.

## Run as local server

```sh
docker run --rm --env-file .env -e WEBPUSH_MAILTO=YourNameHere@example.org -p 5000:5000 pywebpush-poc
```

Now open this site on your browser: http://localhost:5000

## Useful resources

You **REALLY** should take a look at these documentations in order to understand what is happening here and how did i got all this working.

- [pywebpush](https://github.com/web-push-libs/pywebpush): An implementation of Web Push server-side in Python, so you can easily send Push messages to a push server.
- [py_vapid](https://github.com/web-push-libs/vapid/tree/main/python): Utility library to generate VAPID keys in an easy way.
- [flask](https://flask.palletsprojects.com/en/2.1.x/quickstart/): A Pyhton web framework oriented in being light and simple.
- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API): Service Workers are an important part since they are inherently needed by the Web Push API in order to receive Push events, work offline, etc.
- [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API): The main star here, its the one who enables websites to receive events from servers at any time, even when they are not opened in a tab.
- [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API): Note that i have not said anything about showing a notification on screen? That is because Web Push only deals with enabling receiving events from a server. The Notifications API is the one that deals with requesting permission to the user and being the graphical part of the notifications itself.

## Some words of wisdom

- Web Push and Notifications API are enforced to work in HTTPS-only environments. There are few exceptions where this does not happen and one is specifically on the `localhost` and `127.0.0.1` addresses, mainly for test purposes.
- Changing the Web Push private key will likely invalidate any subscriptions already registered. In a test environment this should be no problem, but you may need to reset the site configuration on your browser so that a new subscription is generated.
- Updating a Service Worker implementation may be kind of annoying when doing quick changes and trying to see them reflected quickly. Remember you can always force update the Service Worker from the Developer tools panel, or directly unregister it so a new instance get installed.
- Remember to disable any notification silencer/blocker in your OS (Do not Disturb, Focus Assist, and such). Otherwise everything could seem to be working perfectly but no notifications showing on screen (:
