#!/bin/bash
# get the body response after sending a DELETE request to the URL passed as the first argument
curl "$1" -X DELETE
