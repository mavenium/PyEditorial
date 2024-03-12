FROM python:3.9

WORKDIR /app
COPY . .

# install requirements
RUN pip install -r requirements.txt

COPY /entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN ./entrypoint.sh

