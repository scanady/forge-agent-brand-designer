# Development Environment
- Windows + PowerShell
- Do not use the same terminal where the server was started for running other commands! Use a separate terminal to avoid conflicts and terminating the server.

## Development Workflows
### Running the Dev Server
**IMPORTANT**: Use the custom scripts to run/kill the dev server in the background during development, use server.log to check logs.
./server-start            # Background dev server (logs to server.log)
./server-kill-dev           # Kill background server

# Documentation Guidelines
Avoid using horizontal rules (---) in markdown files.

# Java Architecture & Package Organization Guidelines

You are an expert Java developer assisting with a project that strictly adheres to **Package by Feature**, with a dedicated isolation layer for **Common/Shared** code.

## 1. The "Common" Package Rule
**Strict Rule:** Any logic, utility, or configuration that is used by *more than one feature* must be moved to the dedicated `common` package. Never duplicate utility code across feature packages.

- **Location:** `[base.package].common`
- **Organization:** Do not dump files into the root of `common`. You must sub-categorize them.
    - `common.util` (String manipulation, Date formatting)
    - `common.exception` (Global custom exceptions)
    - `common.security` (JWT parsing, Auth filters)
    - `common.config` (Global bean configurations)

**Do not** place business logic or domain entities (e.g., `User`, `Order`) inside `common`. It is for infrastructure and helpers only.

## 2. Feature Package Structure
For all non-common code, use a **Package by Feature** strategy. All classes related to a feature must reside in the same package.

**Target Structure:**
```text
com.app
├── common          <-- SHARED CODE
│   ├── util
│   └── exception
├── order           <-- FEATURE
│   ├── OrderService.java
│   ├── OrderController.java
│   └── OrderRepository.java
└── customer        <-- FEATURE
```

## 3. Visibility & Encapsulation
- **Common Classes:** Must be `public` so features can access them.
- **Feature Classes:**
    - `Controller` and `Service` interfaces: `public`.
    - `Repository`, internal helpers, and implementation details: `package-private` (default) to prevent other features from accessing them directly.

## 4. Code Generation Examples

### BAD (Duplicating logic in a feature)
```java
package com.app.order;

// Copilot should NOT generate a private date formatter here
public class OrderService {
    private String formatDate(LocalDate date) { ... } 
}
```

### GOOD (Importing from Common)
```java
package com.app.order;

import com.app.common.util.DateUtils; // Importing shared logic

public class OrderService {
    public void process() {
        String date = DateUtils.format(LocalDate.now());
    }
}
```

## 5. Dependency Direction
- **Allowed:** `Feature Package` -> depends on -> `Common Package`
- **Forbidden:** `Common Package` -> depends on -> `Feature Package` (Circular dependency risk)
- **Forbidden:** `Feature A` -> depends on -> `Feature B` internal classes (Use public Services only)

## 6. Database Agnosticism
All database functionality must be database-agnostic. Prefer standard SQL, portable ORM features (e.g., JPA), or data-access abstractions (e.g., repository/DAO interfaces). Do not use vendor-specific SQL, functions, types, extensions, stored procedures, or features (for example PostgreSQL JSONB, MySQL-specific syntax) unless the user explicitly instructs. If a DB-specific optimization is required, isolate it behind a well-documented interface with a package-private implementation and require explicit approval. Ensure tests validate portability across supported engines when possible.