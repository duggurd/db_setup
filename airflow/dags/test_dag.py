from airflow.operators.bash import BashOperator
from airflow import DAG
import datetime

from textwrap import dedent

with DAG(
    "test",
    "this is a test dag",
    schedule="0 * * * *",
    start_date=datetime.datetime.now(),
) as dag:
    
    repo_clone_cmd = dedent(
        """
        cd /tmp && \
        rm -rf db_setup && \
        git clone -b test -n --depth=1 --filter=tree:0 https://github.com/duggurd/db_setup && \
        cd db_setup && \
        git sparse-checkout set airflow && \
        git checkout && \
        cp -r airflow/dags /opt/airflow && \
        rm -rf /tmp/db_setup
        """
    )

    t1 = BashOperator(
        task_id="pull_repo_test",
        bash_command=repo_clone_cmd,
    )
    
    t1