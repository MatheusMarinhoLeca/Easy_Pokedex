# Copyright Matheus Marinho de Morais Leça, 2024
# Licensed under MIT license.
# See LICENSE for more information. 

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libnss3 libasound2 x11-apps libxrender1 libxtst6 \
    libxi6 libxrandr2 libxkbcommon-x11-0 libxcb-render0 \
    libxcb-shm0 libxcb1 libgl1-mesa-glx libgl1-mesa-dri \
    libglu1-mesa tk tcl libxft2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip setuptools wheel \
    && pip install .

ENV DISPLAY=:0 \
    QT_X11_NO_MITSHM=1
    
CMD ["easy-pokedex"]
