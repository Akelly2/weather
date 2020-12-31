DROP TABLE Alert;

CREATE TABLE Alert (
    Sender VARCHAR(255),
    Event_Name VARCHAR(100),
    Start_Time TIMESTAMP,
    End_Time TIMESTAMP,
    Event_Description TEXT,
    Location_Key INT
);