#!/bin/bash
ARGS=$@
docker build . -t pokehelper>/dev/null && docker run -it pokehelper bash -c ". /venv/bin/activate && python /app/cli.py $ARGS"

