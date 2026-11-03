-- Synthetic demo schema only. Not intended for production banking use.
CREATE SCHEMA IF NOT EXISTS banking_demo;

CREATE TABLE IF NOT EXISTS banking_demo.demo_accounts (
    account_id UUID PRIMARY KEY,
    customer_ref VARCHAR(40) NOT NULL,
    account_type VARCHAR(20) NOT NULL,
    currency CHAR(3) NOT NULL DEFAULT 'INR',
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_demo_account_status
        CHECK (status IN ('ACTIVE', 'FROZEN', 'CLOSED'))
);

CREATE TABLE IF NOT EXISTS banking_demo.demo_transfers (
    transfer_id UUID PRIMARY KEY,
    source_account_id UUID NOT NULL REFERENCES banking_demo.demo_accounts(account_id),
    destination_ref VARCHAR(40) NOT NULL,
    rail VARCHAR(10) NOT NULL,
    amount NUMERIC(14,2) NOT NULL CHECK (amount > 0),
    currency CHAR(3) NOT NULL DEFAULT 'INR',
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT chk_demo_transfer_rail
        CHECK (rail IN ('UPI', 'IMPS', 'NEFT', 'RTGS')),
    CONSTRAINT chk_demo_transfer_status
        CHECK (status IN ('INITIATED', 'PENDING', 'SUCCESS', 'FAILED'))
);
