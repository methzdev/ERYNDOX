# ERYNDOX – SYSTEM ARCHITECTURE

**Project:** ERYNDOX  
**Description:** Cyber Intelligence & Digital Forensics  
**Tagline:** Detect • Investigate • Preserve  
**Architecture Version:** 1.0

## 1. Introduction

ERYNDOX is a cybersecurity and digital forensics platform designed to help organizations and security analysts monitor security events, identify potential threats, manage incidents, and preserve digital evidence.

The platform consists of a web application, an Android mobile application, a backend API, a PostgreSQL database, background processing, and secure evidence storage.

Its architecture focuses on security, workspace isolation, modularity, and maintainability.

## 2. Architecture Overview

ERYNDOX follows a **Modular Monolithic Architecture**. The backend is developed as a single application divided into independent functional modules.

The main components are:

- **Web Application:** Provides the main interface for administrators, analysts, and employees.
- **Mobile Application:** Supports mobile-based employee reporting and status tracking.
- **Backend API:** Handles authentication, authorization, business logic, and data processing.
- **Database:** Stores users, workspaces, security events, alerts, incidents, and other application data.
- **Background Worker:** Processes ingestion, detection, notifications, and other asynchronous tasks.
- **Evidence Storage:** Stores encrypted digital evidence securely.

### High-Level Data Flow

1. Users interact with ERYNDOX through the web or mobile application.
2. Applications communicate with the backend through REST APIs over HTTPS.
3. The backend validates requests, performs authorization checks, and processes business logic.
4. Application data is stored in PostgreSQL, while digital evidence is stored separately in encrypted storage.
5. Background workers process time-consuming tasks such as event ingestion, threat detection, and notifications.

The backend API and background worker share the same codebase but run as separate processes.

This approach keeps the initial system manageable while allowing future expansion.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Web Frontend | Next.js, React, TypeScript |
| UI Styling | Tailwind CSS |
| Mobile Application | React Native, Expo, TypeScript |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Migrations | Alembic |
| Authentication | JWT, TOTP MFA |
| Password Hashing | Argon2id |
| Evidence Encryption | AES-256-GCM |
| Integrity Verification | SHA-256 |
| Digital Signatures | RSA |
| Containerization | Docker |
| Version Control | Git and GitHub |

## 4. Backend Architecture

The backend is developed using FastAPI and follows a modular structure.

Its main functional modules include:

- Authentication and user management.
- Workspace and permission management.
- Security event ingestion and normalization.
- Threat detection and alert management.
- Employee report processing.
- Incident investigation.
- Digital evidence management.
- Threat intelligence and risk management.
- Notifications and audit logging.

The backend separates API endpoints, business services, and data-access responsibilities to maintain a clear structure.

A background worker handles time-consuming tasks without blocking normal API requests. It runs separately from the API process while sharing the same backend codebase.

For the initial implementation, PostgreSQL can be used to manage background job records. Workers can claim available jobs using `SELECT ... FOR UPDATE SKIP LOCKED` to reduce the risk of multiple workers processing the same job.

All authentication, authorization, workspace validation, and sensitive business operations are enforced by the backend.

## 5. Database Architecture

PostgreSQL is used as the primary database.

The database manages the main entities of the platform, including:

- Users and Workspaces.
- Organizations and Memberships.
- Security Events and Threat Indicators.
- Alerts and Employee Reports.
- Incidents and Evidence Metadata.
- Risk Assessments.
- Notifications and Audit Logs.

### Workspace Isolation

Each account receives a personal workspace, while organizations use separate organizational workspaces.

Personal and organizational data are logically isolated. A user accesses one active workspace within a request, and access is restricted according to workspace membership and assigned permissions.

Workspace isolation is enforced through:

- Backend authorization and workspace validation.
- Workspace-aware database relationships.
- PostgreSQL Row-Level Security (RLS), where applicable.

The backend does not trust workspace identifiers or permissions supplied directly by the client. Access must be validated against the authenticated user and their authorized workspace.

SQLAlchemy handles database operations, while Alembic manages database schema migrations.

## 6. Security Architecture

Security is a core part of ERYNDOX. The platform uses multiple security mechanisms to protect accounts, application data, and digital evidence.

| Security Area | Approach |
|---|---|
| Password Protection | Argon2id |
| Authentication | JWT |
| Multi-Factor Authentication | TOTP |
| Evidence Encryption | AES-256-GCM |
| Data Integrity | SHA-256 |
| Digital Signatures | RSA |
| Network Security | HTTPS |
| Access Control | RBAC and Workspace Isolation |

### Evidence Protection

Digital evidence is encrypted using AES-256-GCM before being stored.

The architecture uses envelope encryption:

- Each evidence object or version can have its own Data Encryption Key (DEK).
- A Key Encryption Key (KEK) protects the DEK.
- Encryption keys are managed separately from the application database.
- Cryptographic keys and sensitive credentials must not be hardcoded into the application source code.

SHA-256 is used to calculate evidence hashes for integrity verification. Digital signatures and chain-of-custody records provide additional verification and accountability.

The original evidence hash is calculated before encryption. Verification checks can also use ciphertext hashes where required.

Chain-of-custody records are designed to preserve a traceable history of evidence-related actions. Audit logging records important security and administrative activities.

## 7. Web Application Architecture

The web application is developed using Next.js, React, and TypeScript.

It provides the main interface for users to access ERYNDOX features.

The main application areas include:

- Authentication and account management.
- Workspace and organization management.
- Security dashboard and monitoring.
- Alerts and incident investigation.
- Employee reporting.
- Evidence management.
- Threat intelligence and risk management.
- Administration and audit activities.

The frontend communicates with the backend through REST APIs over HTTPS.

The interface displays features according to the user's role and permissions. However, all actual authorization decisions are enforced by the backend.

## 8. Mobile Application Architecture

The mobile application is developed using React Native and Expo with TypeScript.

The initial Android application focuses on employee security reporting and report status tracking.

Main features include:

- Reporting suspicious activities.
- Submitting security-related information.
- Viewing submitted report status.
- Receiving relevant notifications.

The mobile application uses the same backend API as the web application. Authentication, validation, and authorization are handled by the backend.

Additional mobile features and user roles can be introduced in future development phases.

## 9. External Integrations and Communication

ERYNDOX uses REST APIs for communication between its web application, mobile application, and backend.

JSON is the primary data exchange format. CSV is supported for structured data import and export, while PDF is used for generated reports.

The platform is designed to support future external integrations, including approved threat intelligence feeds and antivirus services.

External integrations will use controlled API access, input validation, secure credential management, and appropriate error handling.

External providers will be selected during the relevant implementation phase.

## 10. Deployment Architecture

ERYNDOX will use separate environments for development, testing, demo, and future production deployment.

Docker will be used to package application components where appropriate.

The backend API, background worker, web application, and database will be configured according to their deployment requirements.

Evidence files will use private local storage during development and private object storage in a hosted environment.

### Demo Environment

The public Demo Mode will use synthetic data only.

Demo databases, evidence storage, and cryptographic keys will remain separate from real user environments. Real user information and evidence must not be exposed through the public demo.

### Production Considerations

Production deployment will require:

- Secure environment configuration and secret management.
- Database and evidence storage backups.
- HTTPS and restricted network access.
- Monitoring and error logging.
- Appropriate access controls and recovery procedures.

The final hosting provider and deployment configuration will be selected after evaluating cost, security, backup requirements, and infrastructure limitations.

## 11. Testing and Quality Assurance

Testing will ensure that ERYNDOX functions correctly, protects sensitive information, and maintains workspace isolation.

The main testing activities include:

- **Unit Testing:** Testing individual functions and backend modules.
- **Integration Testing:** Verifying communication between the frontend, backend, database, and background worker.
- **Security Testing:** Checking authentication, role-based access, workspace isolation, and evidence protection.
- **API Testing:** Validating API requests, responses, and error handling.
- **End-to-End Testing:** Testing important user workflows across the application.

Automated tests will be used to identify issues before new changes are released.

Special attention will be given to unauthorized workspace access, evidence integrity verification, and permission enforcement.

## 12. Risks and Future Considerations

The architecture is designed to support future improvements without unnecessary complexity in the initial development phase.

Important considerations include:

- **Data Isolation:** Maintaining strict separation between personal and organizational workspaces.
- **Evidence Security:** Protecting digital evidence through encryption, integrity verification, and controlled access.
- **System Scalability:** Increasing application and background processing capacity when required.
- **External Integrations:** Introducing approved threat intelligence and antivirus integrations in future phases.
- **AI Assistance:** Considering governed AI-assisted analysis in a future release, with human oversight and disabled by default.

Hosting provider selection, infrastructure costs, backup arrangements, and data residency requirements must be evaluated before production deployment.

The initial implementation will prioritize security, reliability, and core platform functionality before introducing advanced features.

## 13. System Limitations

The initial ERYNDOX release will focus on its core cybersecurity monitoring and digital forensics features.

The following limitations apply:

- Threat detection depends on the quality of imported data and configured detection rules.
- Detection alerts indicate potential threats and do not independently prove malicious activity.
- AI-based security decisions and autonomous response are outside the initial MVP scope.
- Antivirus integration and external threat intelligence feeds require future approval and implementation.
- Cryptographic verification helps identify changes to protected evidence but does not independently prove the accuracy or authenticity of the original information.
- Public Demo Mode uses synthetic data and does not represent real-world security performance.

These limitations will be considered during development, testing, and evaluation.

## 14. Conclusion

The ERYNDOX architecture provides a structured foundation for an integrated cybersecurity monitoring and digital forensics platform.

By combining a modular backend, web and mobile applications, workspace-based data isolation, threat detection, and secure evidence management, the system aims to provide a maintainable and extensible solution.

The initial development will prioritize core functionality, security, and reliability. Advanced features will be introduced in future phases based on system requirements and evaluation results.