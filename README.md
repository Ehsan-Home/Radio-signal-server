# Radio-signal-server ⚡️

## How to run? 📦

- Build the docker

```
docker build -t img .
```

- Run the image

```
docker run -it img
```

## Output 🖼️

It will print a randomized radio object as well as starting the Django project.

## Points

- Django contains a secret key that usually is hidden using `.env` variables. Each developer in the team should individually set up `.env` file and **MUST NOT** upload it to the GitHub. However, for this project and for the simplicity, this secret key is exposed to GitHub.
