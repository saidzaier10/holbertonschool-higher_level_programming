-- 5-unique_id.sql
-- Script to create the table unique_id with a unique constraint on id

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
