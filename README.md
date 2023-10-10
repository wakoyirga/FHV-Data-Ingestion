# FHV Data Ingestion

This repository contains scripts and resources for ingesting data from the NYC "For Hire Vehicles (FHV) – Active" dataset. 

## Design Rationale

The following objectives and constraints guided the design and development of the data ingestion solution:

### Objectives and Constraints

- Cost Efficiency: Aimed to utilize AWS Free Tier resources to keep operational costs at a minimum.
- Simplicity: The solution is built using minimal external libraries and AWS-native tools to ensure ease of setup and maintenance.
- Incremental Data Ingestion: To minimize the transferred data volume and enhance efficiency, only new or updated records since the last ingestion are fetched.
- Scalability: The solution can accommodate growing datasets by utilizing scalable AWS services and pagination in data retrieval.
- SQL Accessibility: Persisted data is made available in a format and location (S3) compatible with AWS Big Data offerings like Athena, enabling SQL querying.

### Additional Measures for Robustness

To further enhance the solution, various measures were considered to ensure the robustness, security, and efficiency of the system:

- Data Quality Assurance: Implement data validation checks to ensure that ingested data is accurate, complete, and meets specified standards.
- Data Versioning: Enable tracking of data changes over time and the ability to revert to a previous state if necessary.
- Data Encryption: Enhanced data security and privacy with S3 server-side encryption.
- Notification System: The ability to notify stakeholders of any data ingestion errors, anomalies, or successes.
- Backup and Disaster Recovery: Safeguard against data loss or service disruptions with regular backups.
- Audit Trail: Track access and modifications to the data, ensuring traceability and accountability.
- Cost Optimization: Monitor and adjust AWS resources to ensure the solution remains cost-effective.
- API Management: Implement rate-limiting and retry strategies to handle API rate limits or transient errors.
- Data Transformation: Support more complex analytics or integration with other datasets by transforming and normalizing data.
- Documentation and Metadata Management: Centralized documentation and metadata to clarify data sources, structures, and transformations.

## Files in this Repository

- 'fhv_active_schema.ddl': Contains the DDL for creating the Athena external table.
- 'fhv_data_ingestion.py': Python script for ingesting data from the NYC “For Hire Vehicles (FHV) – Active” dataset.

## Setup & Usage

1. Ensure you have AWS CLI set up and configured with the necessary permissions.
2. Clone this repository.
3. Set up your environment variables or AWS Secrets Manager for sensitive data like API tokens.
4. Run 'fhv_data_ingestion.py' to start the data ingestion process.
5. Use Athena or similar AWS services to query the ingested data using the provided DDL.

---

Contributions, feedback, and issues are welcome! Please ensure that any issues raised do not contain sensitive information.
