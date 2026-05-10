FROM gcr.io/distroless/python3-debian13

COPY determine_docker_tags/__init__.py /determine-docker-tags.py

CMD [ "/determine-docker-tags.py" ]