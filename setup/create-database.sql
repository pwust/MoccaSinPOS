--
-- File generated with SQLiteStudio v3.1.1 on Di Feb 7 11:51:55 2017
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: product_old_DEF
DROP TABLE IF EXISTS product_old_DEF;

CREATE TABLE product_old_DEF (
    id        INTEGER  NOT NULL,
    text      TEXT     NOT NULL,
    valid     BOOLEAN  NOT NULL
                       DEFAULT true,
    validfrom DATETIME NOT NULL
                       DEFAULT (now() ),
    validto   DATETIME
);


-- Table: product_old_LABEL
DROP TABLE IF EXISTS product_old_LABEL;

CREATE TABLE product_old_LABEL (
    id        INTEGER  UNIQUE
                       NOT NULL,
    color     TEXT     NOT NULL,
    labellist TEXT,
    valid     BOOLEAN  NOT NULL,
    validfrom DATETIME NOT NULL
                       DEFAULT (now() ),
    validto   DATETIME
);


-- Table: product_old_PREIS
DROP TABLE IF EXISTS product_old_PREIS;

CREATE TABLE product_old_PREIS (
    id           INTEGER (12) NOT NULL,
    valuewithvat REAL (5, 2)  NOT NULL,
    valid        BOOLEAN      NOT NULL
                              DEFAULT true,
    validfrom    DATETIME     NOT NULL
                              DEFAULT (now() ),
    validto      DATETIME,
    [temporary]  BOOLEAN      NOT NULL
                              DEFAULT false
);


-- Table: users
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id         INTEGER   NOT NULL
                         PRIMARY KEY
                         UNIQUE,
    logonname  TEXT (16) NOT NULL
                         UNIQUE,
    first      TEXT,
    last       TEXT,
    PIN        TEXT (8)  CHECK (PIN BETWEEN 0 AND 99999999),
    password   TEXT,
    lastlogon  DATETIME,
    lastlogoff DATETIME,
    islocked   BOOLEAN   DEFAULT false
                         NOT NULL,
    isadmin    BOOLEAN   DEFAULT false
                         NOT NULL
);


-- Table: vat
DROP TABLE IF EXISTS vat;

CREATE TABLE vat (
    country             TEXT  DEFAULT 'DE'
                              NOT NULL,
    vat_type            TEXT  DEFAULT 'full'
                              NOT NULL,
    valid_from_yyyymmdd TEXT  NOT NULL,
    vat_rate            FLOAT NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
