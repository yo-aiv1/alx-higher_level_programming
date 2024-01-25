#!/bin/bash
# displays all HTTP methods the server will accept
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
