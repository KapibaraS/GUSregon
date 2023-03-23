FROM python:3.10-alpine3.16
WORKDIR app
RUN python -m venv venv && source venv/bin/activate
COPY ./requirements.txt ./app/requirements.txt
RUN pip install --upgrade pip  && pip install -r ./app/requirements.txt
COPY . ./app
EXPOSE 8080

