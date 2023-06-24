FROM python:3.8.13

RUN pip install streamlit
RUN pip install scikit-learn
RUN pip install pandas


WORKDIR /app

COPY ./app.py /app/app.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]