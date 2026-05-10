FROM gcr.io/distroless/python3-debian12@sha256:2fdb05402a2cf21cf78fdb3ba4c5db167241e9e498140f5bf689d7efb773731f

COPY determine_docker_tags/__init__.py /determine-docker-tags.py

CMD [ "/determine-docker-tags.py" ]