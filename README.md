# Twitter ETL Automation Project

## Overview
This project automates the extraction, transformation, and loading (ETL) of tweet data using Apache Airflow. Given the removal of free access to the Twitter API, we leverage static data sourced from Kaggle. The project consists of the following key steps:

1. **Data Extraction**: The static tweet data is downloaded from Kaggle and uploaded to an Amazon S3 bucket.
2. **Data Transformation**: Basic transformations are applied, such as dropping unnecessary columns (latitude and longitude).
3. **Data Loading**: The transformed data is uploaded back to another S3 bucket.
4. **Automation**: The entire workflow is orchestrated using Apache Airflow, which is hosted on an EC2 instance (t2.medium).

The DAG is scheduled to run daily to ensure that the latest data is processed.

## Technologies Used
- **Apache Airflow**: For workflow orchestration.
- **Amazon S3**: For data storage and retrieval.
- **EC2**: For hosting the Airflow instance.
- **Python**: For scripting the ETL process.
- **Pandas**: For data manipulation and transformation.
- **IAM**: To manage permissions and access for the EC2 instance.

## Steps to Set Up the Project
1. **Set up an EC2 Instance**:
   - Launch an EC2 instance (t2.medium) and ensure you have access to the instance via SSH.
   - Assign an IAM role with permissions to access S3.

2. **Install Dependencies**:
   - Set up a virtual environment and install the required libraries:
     ```bash
     pip install apache-airflow pandas s3fs tweepy
     ```

3. **Upload Static Data**:
   - Download the static tweet data from Kaggle.
   - Upload the data to your S3 bucket using the AWS CLI or the AWS Management Console.

4. **Create Airflow DAG**:
   - Create a folder for your Airflow DAGs and place the `twitter_dag.py` and `twitter_etl.py` scripts inside.
   - Ensure that the DAG is set to read from your S3 bucket and write to your target S3 bucket.

5. **Run Airflow**:
   - Start the Airflow web server and scheduler:
     ```bash
     airflow webserver --port 8080
     airflow scheduler
     ```
   - Access the Airflow UI at `http://<your-ec2-public-ip>:8080`.

6. **Trigger the DAG**:
   - In the Airflow UI, trigger the `twitter_dag` to execute the ETL process.

7. **Monitor the Workflow**:
   - Check the logs in the Airflow UI to monitor the success or failure of the ETL process.

## Conclusion
This project provides a scalable solution for automating the ETL process for tweet data, using Apache Airflow and AWS services. The architecture allows for easy adjustments and scalability to accommodate larger datasets in the future.

## Architecture
<img src="Architecture">
