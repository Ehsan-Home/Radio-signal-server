FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
EXPOSE 8000:8000

CMD cd interview && python printRadio.py && cd .. && python manage.py runserver  
