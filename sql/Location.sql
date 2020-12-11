CREATE TABLE "Location" (
    Location_Key INT,
    City VARCHAR(50),
    Region VARCHAR(50),
    Country VARCHAR(50),
    Latitude REAL,
    Longitude REAL,
    Timezone_Offset INT
);

-- Adding some example locations
INSERT INTO "Location" VALUES
(1, 'Vancouver', 'BC', 'Canada', 49.28, -123.12, -28800),
(2, 'Toronto', 'ON', 'Canada', 43.69, -79.28, -18000)

