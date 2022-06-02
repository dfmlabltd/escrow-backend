FROM python:3.8.3

ENV PROGRAM_DIRECTORY=/app/

RUN mkdir -p ${PROGRAM_DIRECTORY}

WORKDIR ${PROGRAM_DIRECTORY}

COPY . .

RUN pip install -r requirements.txt

RUN  python manage.py collectstatic --no-input 