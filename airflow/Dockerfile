FROM apache/airflow
USER root 
RUN apt update 
RUN apt install git -y
COPY ./airflow.cfg /opt/airflow/airflow.cfg
USER airflow