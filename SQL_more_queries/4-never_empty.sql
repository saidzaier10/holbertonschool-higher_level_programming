-- 4-never_empty.sql
-- Script to create the table id_not_null with NOT NULL constraint and default value for id

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
