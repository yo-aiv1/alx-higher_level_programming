#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI "$1" -X OPTIOND | grep "Allow:" | cut -d " " -f 2-
