# ERYNDOX – DATABASE DESIGN

**Project:** ERYNDOX  
**Description:** Cyber Intelligence & Digital Forensics  
**Tagline:** Detect • Investigate • Preserve  
**Document Version:** 1.0  
**Reference:** ERYNDOX Software Requirements Specification v1.3

---

## 1. Introduction

This document describes the database design of ERYNDOX, an integrated cybersecurity monitoring and digital forensics platform.

The database design defines the main entities, relationships, constraints, and security mechanisms required to manage application data.

PostgreSQL will be used as the primary relational database management system.

The design focuses on:

- Data consistency and integrity.
- Personal and organizational workspace isolation.
- Secure storage of application records.
- Efficient data retrieval.
- Digital evidence metadata management.
- Auditability and future scalability.

## 2. Database Overview

ERYNDOX uses PostgreSQL to store application data, workspace information, security events, alerts, incidents, evidence metadata, and audit records.

The database will be accessed through SQLAlchemy, while Alembic will manage schema changes using version-controlled migrations.

### 2.1 Database Design Approach

The database follows a relational data model.

The design uses:

- Primary Keys (PK) to uniquely identify records.
- Foreign Keys (FK) to establish relationships.
- Unique Constraints to prevent duplicate records.
- Check Constraints to validate permitted values.
- Indexes to improve query performance.
- PostgreSQL Row-Level Security (RLS) to enforce workspace isolation.

UUIDs will be used as primary keys for externally referenced entities.

### 2.2 Database Naming Conventions

| Item | Convention |
|---|---|
| Table Names | snake_case, plural |
| Column Names | snake_case |
| Primary Keys | id |
| Foreign Keys | referenced_table_id |
| Workspace Reference | workspace_id |
| Timestamps | created_at, updated_at |
| Primary Key Type | UUID |
| Timestamp Type | TIMESTAMPTZ |

All timestamps will be stored in UTC.

## 3. Database Entities

The database is divided into functional domains.

### 3.1 Identity Management

| Entity | Description | Priority |
|---|---|---|
| Users | Stores user account information. | P1 |
| MfaFactors | Stores protected multi-factor authentication information. | P1 |
| RefreshTokens | Manages refresh token records and revocation. | P1 |

### 3.2 Workspace Management

| Entity | Description | Priority |
|---|---|---|
| Workspaces | Stores personal and organizational workspace information. | P1 |
| WorkspaceMembers | Manages user membership within workspaces. | P1 |
| Invitations | Stores workspace invitations and their status. | P1 |
| Roles | Defines available workspace roles. | P1 |
| Permissions | Defines individual access permissions. | P1 |
| RolePermissions | Connects roles with permissions. | P1 |
| MemberPermissionGrants | Stores additional member-specific permission grants. | P2 |

### 3.3 Security Event Ingestion

| Entity | Description | Priority |
|---|---|---|
| EventSources | Stores information about event sources. | P1 |
| LogUploads | Tracks uploaded log files and ingestion status. | P1 |
| SecurityEvents | Stores normalized security event records. | P1 |
| BackgroundJobs | Manages asynchronous processing jobs. | P1 |

### 3.4 Threat Detection and Alerts

| Entity | Description | Priority |
|---|---|---|
| DetectionRules | Stores versioned threat detection rules. | P1 |
| DetectionRuns | Records individual detection executions. | P1 |
| Alerts | Stores generated security alerts. | P1 |
| AlertEvents | Connects alerts with matching security events. | P1 |
| AlertExplanations | Stores detection explanations and supporting information. | P1 |
| AnalystFeedback | Records analyst feedback about detection results. | P1 |

### 3.5 Threat Intelligence

| Entity | Description | Priority |
|---|---|---|
| IntelSources | Stores approved threat intelligence source information. | P1 |
| ThreatIndicators | Stores indicators of compromise (IOCs). | P1 |
| IndicatorMatches | Records matches between indicators and security events. | P1 |
| AllowlistEntries | Stores approved indicators or exceptions. | P2 |

### 3.6 Employee Reporting

| Entity | Description | Priority |
|---|---|---|
| EmployeeReports | Stores employee-submitted security reports. | P1 |
| ReportAttachments | Stores protected attachment metadata and storage references. | P1 |
| ReportStatusHistory | Records changes to report status. | P1 |
| ReportMessages | Stores communication related to employee reports. | P2 |
| ReportLinks | Connects reports with related application records. | P2 |

### 3.7 Incident Management

| Entity | Description | Priority |
|---|---|---|
| Incidents | Stores cybersecurity incident information. | P1 |
| IncidentActivities | Records incident-related activities. | P1 |
| IncidentAlerts | Connects incidents with related alerts. | P1 |
| IncidentReports | Connects incidents with employee reports. | P1 |
| IncidentEvidence | Connects incidents with digital evidence records. | P1 |

### 3.8 Digital Evidence Management

| Entity | Description | Priority |
|---|---|---|
| EvidenceItems | Stores evidence metadata and protected storage references. | P1 |
| EvidenceManifests | Stores evidence manifests, hashes, and signature metadata. | P1 |
| SigningKeys | Stores public signing-key metadata only. | P1 |
| CustodyEvents | Records evidence chain-of-custody activities. | P1 |
| EvidenceVerifications | Stores evidence integrity verification results. | P1 |

### 3.9 Risk Management

| Entity | Description | Priority |
|---|---|---|
| Risks | Stores identified security risks. | P1 |
| RiskAssessments | Stores likelihood, impact, and risk score information. | P1 |
| Assets | Stores organizational asset information. | P2 |
| RiskTreatments | Tracks risk treatment activities. | P2 |
| RiskIncidents | Connects risks with related incidents. | P2 |

### 3.10 System Operations

| Entity | Description | Priority |
|---|---|---|
| Notifications | Stores application notification records. | P1 |
| DeviceTokens | Stores mobile push notification tokens. | P2 |
| AuditLogs | Records important security and administrative activities. | P1 |
| AiGenerations | Stores governed AI-assisted generation metadata. | P3 |

P1 entities support the initial MVP. P2 entities are planned for post-MVP development, while P3 entities are reserved for advanced functionality.

## 4. Main Entity Relationships

The following relationships define how the main database entities interact.

### 4.1 Identity and Workspace Relationships

- A user can have multiple workspaces.
- Each user account receives a personal workspace.
- An organization workspace can have multiple members.
- A workspace can contain multiple membership records.
- A workspace member is assigned a role.
- A role can contain multiple permissions.
- A permission can be associated with multiple roles.

### 4.2 Security Event and Detection Relationships

- A workspace can contain multiple event sources.
- An event source can produce multiple security events.
- A log upload can produce multiple security events.
- A detection rule can be used in multiple detection runs.
- A detection run can generate multiple alerts.
- An alert can be associated with multiple security events.
- An alert can contain one or more explanation records.
- An alert can belong to zero or one incident.

### 4.3 Employee Reporting Relationships

- A user can submit multiple employee reports.
- An employee report can contain multiple attachment records.
- An employee report can have multiple status history records.
- An employee report can be associated with an incident.

### 4.4 Incident Relationships

- A workspace can contain multiple incidents.
- An incident can contain multiple activities.
- An incident can be associated with multiple alerts.
- An incident can be associated with multiple employee reports.
- An incident can contain multiple evidence records.

### 4.5 Evidence Relationships

- An evidence item can have multiple manifest versions.
- An evidence item can have multiple custody events.
- An evidence item can have multiple verification records.
- An evidence item can be associated with multiple incidents through the incident-evidence relationship.

### 4.6 Risk and Operations Relationships

- A workspace can contain multiple risks.
- A risk can have multiple assessment records.
- A risk can be associated with multiple incidents.
- A user can receive multiple notifications.
- Audit logs record important activities performed by users or system processes.

## 5. Workspace Isolation and Multi-Tenancy

Workspace isolation is one of the most important database requirements of ERYNDOX.

The system supports personal workspaces and organizational workspaces.

### 5.1 Personal Workspace

Each registered user automatically receives a personal workspace.

A Solo Analyst can manage security events, alerts, incidents, evidence, and other permitted records within this workspace.

Personal workspace data must remain separate from organizational workspace data.

### 5.2 Organization Workspace

An organization workspace is created with an initial Organization Owner.

Users can become members through invitations and receive roles according to their responsibilities.

Workspace membership determines which organizational data a user is permitted to access.

### 5.3 Workspace Data Isolation

Every tenant-owned table, including child and relationship tables, must contain a `workspace_id` column.

Workspace isolation will be enforced through:

- Backend authorization.
- Workspace-aware database relationships.
- Composite foreign keys.
- PostgreSQL Row-Level Security (RLS).

Composite uniqueness and foreign key constraints will use `workspace_id` together with record identifiers to prevent cross-workspace relationships.

### 5.4 PostgreSQL Row-Level Security

RLS will be enabled and forced on tenant-owned tables.

At the beginning of each database transaction, the backend will establish the authenticated user's authorized active workspace using a transaction-local database setting.

RLS policies will use both `USING` and `WITH CHECK` conditions.

The application database role must not have superuser, table-owner, or `BYPASSRLS` privileges.

Background workers must establish workspace context using trusted and validated job records.

Pooled database connections must not retain workspace context between transactions.

Cross-workspace access attempts must fail securely and be covered by automated tests.

## 6. Database Constraints and Integrity

Database constraints will help maintain accurate and consistent records.

### 6.1 Primary Key Constraints

Every main entity will have a unique primary key.

UUID values will be used for externally referenced records.

### 6.2 Foreign Key Constraints

Foreign keys will establish valid relationships between database entities.

Tenant-owned relationships will use workspace-aware foreign keys to prevent records from different workspaces from being connected.

### 6.3 Unique Constraints

Unique constraints will be applied where duplicate records are not permitted.

Examples include:

- Unique user email addresses.
- Unique workspace membership combinations.
- Unique invitation consumption.
- Unique idempotency keys within their required scope.
- Unique evidence sequence numbers within a workspace.
- Unique audit sequence numbers within a workspace.

### 6.4 Check Constraints

Check constraints will validate important database values.

Examples include:

- Valid risk likelihood and impact ranges.
- Valid numeric scores.
- Required non-negative sequence numbers.
- Valid enumerated status values where appropriate.

State transitions will also be validated through backend service logic.

## 7. Database Indexing and Performance

Indexes will be introduced to improve frequently executed database queries.

Important indexing areas include:

- `workspace_id`
- User identifiers.
- Organization and membership identifiers.
- Security event timestamps.
- Alert status and severity.
- Incident identifiers.
- Evidence identifiers.
- Background job status and creation time.
- Audit sequence numbers.

Composite indexes will be selected according to common workspace filtering and sorting requirements.

Keyset pagination will be preferred for large datasets to maintain consistent query performance.

Indexes will be reviewed based on actual query patterns to avoid unnecessary storage and write-performance overhead.

## 8. Evidence Metadata and Cryptographic Storage

Digital evidence files will not be stored directly as ordinary database records.

The database will store evidence metadata and protected storage references. Actual evidence files will be stored separately in private encrypted storage.

### 8.1 Evidence Metadata

An evidence record may contain:

- Evidence identifier.
- Workspace identifier.
- Original filename.
- Media type.
- File size.
- Storage reference.
- Original plaintext SHA-256 hash.
- Ciphertext SHA-256 hash.
- Encryption algorithm.
- Encryption nonce information.
- Wrapped Data Encryption Key.
- Key identifier and version.
- Upload status.
- Creation timestamp.

Sensitive evidence contents and cryptographic private keys must not be stored in ordinary database tables.

### 8.2 Encryption Key Management

ERYNDOX will use envelope encryption.

- A unique Data Encryption Key (DEK) will be generated for each evidence object or version.
- AES-256-GCM will encrypt the evidence.
- A Key Encryption Key (KEK) will protect the DEK.
- KEKs will be managed outside the database.
- Key identifiers and versions will be stored for key rotation and verification.

Encryption operations must use fresh 96-bit nonces and authenticated metadata.

Large files will use a reviewed streaming or chunked authenticated-encryption design rather than loading entire files into memory.

Incomplete uploads must not be treated as valid evidence.

### 8.3 Evidence Manifests and Verification

Evidence manifests will contain relevant evidence metadata, cryptographic hashes, and verification information.

Manifest signatures will use RSA-PSS with SHA-256.

Signing private keys will remain outside the database, while public-key metadata will be stored in the `SigningKeys` entity.

Evidence verification records will store verification outcomes, timestamps, and relevant details.

## 9. Audit Logs and Chain of Custody

Audit logs and custody events are essential for accountability and digital evidence tracking.

### 9.1 Audit Logs

Audit logs will record important application activities, including:

- Authentication events.
- Workspace membership changes.
- Permission changes.
- Security event ingestion.
- Alert status changes.
- Incident updates.
- Evidence operations.
- Evidence verification.
- Administrative activities.

Audit records should include the actor, action, target entity, workspace, timestamp, and relevant metadata.

Sensitive information such as passwords, tokens, encryption keys, and plaintext evidence must never be recorded in audit logs.

### 9.2 Audit Hash Chain

Audit records will use a SHA-256 canonical hash chain.

Each record will reference the previous record's hash.

The audit sequence number and chain-head update must be managed transactionally to prevent concurrent updates from producing inconsistent chains.

Audit and custody records will be append-only for normal application roles.

The hash chain is designed to be tamper-evident, not tamper-proof.

## 10. Database Transactions and Background Jobs

Database transactions will be used when multiple related operations must succeed or fail as one logical unit.

Important transactional operations include:

- Workspace creation and initial membership assignment.
- Workspace invitation acceptance.
- Security event ingestion.
- Alert generation.
- Incident updates.
- Evidence metadata creation.
- Audit sequence and hash-chain updates.

### 10.1 Background Jobs

The `BackgroundJobs` entity will manage asynchronous tasks such as:

- Log ingestion.
- Event normalization.
- Duplicate detection.
- Threat detection.
- Notification processing.
- Scheduled tasks.

Jobs will support appropriate status tracking, bounded retries, and idempotent processing.

PostgreSQL job claiming will use `SELECT ... FOR UPDATE SKIP LOCKED` to reduce duplicate processing by concurrent workers.

## 11. Data Retention and Privacy

Data retention and privacy controls will be considered throughout database development.

The initial implementation will prioritize secure data handling and workspace isolation.

Future retention functionality may include:

- Configurable retention policies.
- Controlled workspace export.
- Controlled data deletion.
- Legal hold support.
- Cryptographic erasure where appropriate.

Employee reporting information will follow privacy requirements.

Employees can view their own reports and permitted status messages. Organization Owners and Administrators receive aggregate reporting by default. Access to identifiable report content will be limited to authorized triage roles and audited.

Real personal or regulated data must not be used without the required privacy and legal review.

## 12. Demo Database Isolation

The public Demo Mode will use synthetic data only.

The demo environment must maintain separate:

- Database or database schema.
- Evidence storage.
- Cryptographic keys.
- Demo accounts and records.

Real user information and real evidence must never be exposed through the public demo environment.

Demo data will support controlled resets and appropriate abuse-prevention measures.

## 13. Database Security and Backup

Database security will be implemented through multiple protective measures.

These include:

- Restricted database permissions.
- Secure database credentials.
- Encrypted database connections where supported.
- Backend-enforced authorization.
- PostgreSQL RLS policies.
- Parameterized database queries.
- Secure secret management.
- Encrypted backups.
- Regular backup verification and restore testing.

Database credentials and cryptographic secrets must not be committed to source control.

Production database access will follow the principle of least privilege.

## 14. Conclusion

The ERYNDOX database design provides a structured foundation for managing cybersecurity events, threat intelligence, incidents, digital evidence, and organizational information.

The relational model, workspace isolation, database constraints, and security controls are designed to maintain data integrity and protect sensitive information.

PostgreSQL, SQLAlchemy, and Alembic will support reliable database operations and schema management.

The database will initially prioritize P1 functionality while allowing future expansion through P2 and P3 features.

This design will serve as the reference for database implementation, API development, and database testing.