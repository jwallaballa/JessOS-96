FROM ubuntu:latest
LABEL authors="jessi"

ENTRYPOINT ["top", "-b"]