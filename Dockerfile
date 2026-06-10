FROM gcr.io/distroless/python3-debian13@sha256:178dd00f2da3271f3819df5cd327472754946c7430d82197b247e95e839a3d55

COPY determine_docker_tags/__init__.py /determine-docker-tags.py

CMD [ "/determine-docker-tags.py" ]