# Changelog

All notable changes to the Space Pioneers API project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed - 2026-01-21

#### Complete Project Rebrand: Human Spaceflight API → Space Pioneers API

**Major Breaking Change**: The project has been completely rebranded from "Human Spaceflight API" to "Space Pioneers API".

##### HTML Templates (31 files)
- Updated all 27 page titles from `| Human Spaceflight API` to `| Space Pioneers API`
- Modified homepage main heading from "Human spaceflight data" to "Space pioneers data"
- Updated branding across all template files:
  - Error pages (403, 404, 500)
  - Account pages (login, logout, signup, password reset, etc.)
  - Agency pages
  - Astronaut pages
  - EVA pages
  - Mission pages
  - Social authentication pages

##### Base Template Branding (`templates/base.html`)
- **Line 74**: Updated logo alt text: `humanspaceflightapi_logo` → `spacepioneersapi_logo`
- **Line 74**: Updated logo src to reference `spacepioneersapi-navbarlogotext.svg`
- **Line 170**: Changed footer domain: `humanspaceflightapi.com` → `spacepioneersapi.com`
- **Line 227**: Updated contact email: `info@humanspaceflightapi.com` → `info@spacepioneersapi.com`
- **Line 241**: Updated copyright notice to "Copyright © 2026 Space Pioneers API. All rights reserved."

##### Logo Assets
- **Renamed**: `static/base/images/humanspaceflightapi-navbarlogotext.svg` → `spacepioneersapi-navbarlogotext.svg`
- **Renamed**: `static/base/images/humanspaceflight-navbarlogotext.svg` → `spacepioneers-navbarlogotext.svg`
- Updated SVG text content from "human spaceflight API" to "Space Pioneers API"
- Updated SVG metadata (sodipodi:docname attributes)

##### Documentation
- **Added**: Comprehensive README.md (328 lines) with:
  - Complete project description and features overview
  - Technology stack documentation
  - Architecture overview with project structure
  - Development environment setup (Docker + local options)
  - Common problems and troubleshooting solutions
  - Management commands reference
  - Contributing guidelines

##### Configuration Files
- **Updated** `config/wsgi.py`: Changed docstring from "config project" to "Space Pioneers API project"
- **Updated** `config/asgi.py`: Changed docstring from "config project" to "Space Pioneers API project"
- **Updated** `config/settings/settings.py`: Changed docstring from "config project" to "Space Pioneers API project"

##### Statistics
- **Files Changed**: 31
- **Additions**: 362 lines
- **Deletions**: 43 lines
- **Files Renamed**: 2 (SVG logo files)

##### Migration Notes
- All template references have been updated
- Logo file references in templates have been updated to new filenames
- Domain and email references updated throughout
- No database schema changes required
- No breaking changes to URLs or API endpoints

---

## Previous Versions

### [0.1.0] - Historical Baseline

Initial version of the project as "Human Spaceflight API" before rebrand.

#### Features
- Django 5.1.6 application for managing space mission data
- PostgreSQL database with astronauts, missions, agencies, and EVAs
- Bootstrap 4 frontend with Material Design
- Django admin panel with import/export functionality
- Social authentication (GitHub, Bitbucket)
- Docker/Docker Compose deployment support
- Coverage period: April 1961 - December 1972 (early space era)
