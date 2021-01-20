DROP TABLE "Location";
CREATE TABLE "Location" (
    Location_Key SERIAL,
    City VARCHAR(50),
    Region VARCHAR(50),
    Country VARCHAR(50),
    Latitude REAL,
    Longitude REAL,
    Timezone_Offset INT
);

