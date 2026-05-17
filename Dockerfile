FROM gcr.io/distroless/python3-debian13@sha256:0e300647f5a9d51fb686e9167c97248e0419cd6e5186efc50b642748aab8d8be

COPY determine_docker_tags/__init__.py /determine-docker-tags.py

CMD [ "/determine-docker-tags.py" ]