CREATE EXTERNAL TABLE fhv_active (
    Active STRING,
    VehicleLicenseNumber STRING,
    Name STRING,
    LicenseType STRING,
    ExpirationDate TIMESTAMP,
    PermitLicenseNumber STRING,
    DMVLicensePlateNumber STRING,
    VehicleVINNumber STRING,
    WheelchairAccessible STRING,
    CertificationDate TIMESTAMP,
    HackUpDate TIMESTAMP,
    VehicleYear INT,
    BaseNumber STRING,
    BaseName STRING,
    BaseType STRING,
    VEH STRING,
    BaseTelephoneNumber STRING,
    Website STRING,
    BaseAddress STRING,
    Reason STRING,
    OrderDate TIMESTAMP,
    LastDateUpdated TIMESTAMP,
    LastTimeUpdated STRING
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH LOCATION 's3://fhv-active-dataset/data/'
TBLPROPERTIES ('has_encrypted_data'='false');
