ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /data


RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libharfbuzz-subset0 \
    libjpeg-dev \
    libopenjp2-7-dev \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /data/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /data/requirements.txt

COPY . /data/


CMD exec gunicorn --bind :50052 --workers 2 --timeout 180 --log-file=- --log-level=info --preload base.wsgi:application