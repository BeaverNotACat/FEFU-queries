FROM python:3.12

WORKDIR code

RUN apt-get install make
COPY Makefile .
COPY pyproject.toml .
RUN make deps

COPY . .
CMD make run-dev
