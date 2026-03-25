FROM python:3.10-slim

LABEL maintainer="you <your_email>" \
      version="0.1" \
      description="Python script to classify DNA and RNA sequences"

COPY seqClass.py /usr/local/bin/seqClass.py
RUN chmod +x /usr/local/bin/seqClass.py