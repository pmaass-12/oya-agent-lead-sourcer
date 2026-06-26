---
name: hunter-enrich
display_name: "Hunter.io Enrichment"
description: "Enrich companies by domain and people by email using the Hunter.io API, returning firmographic and professional profile data"
category: sales
icon: database
skill_type: sandbox
catalog_type: addon
requirements: "httpx>=0.25"
resource_requirements:
  - env_var: HUNTER_API_KEY
    name: "Hunter.io API Key"
    description: "API key from Hunter.io (Dashboard > API & Integrations > API Keys)"
tool_schema:
  name: hunter-enrich
  description: "Enrich companies by domain and people by email using the Hunter.io API"
  parameters:
    type: object
    properties:
      action:
        type: "string"
        description: "Which enrichment to perform"
        enum: ["company_enrichment", "person_enrichment"]
      domain:
        type: "string"
        description: "Company domain for company_enrichment (e.g. 'stripe.com')"
        default: ""
      email:
        type: "string"
        description: "Email address for person_enrichment (e.g. 'john@stripe.com')"
        default: ""
    required: [action]
---
# Hunter.io Enrichment

Enrich companies by domain and people by email address using the Hunter.io API. Returns firmographic data (industry, revenue, employee count, location) and professional profile data (title, role, seniority, LinkedIn, bio).

## Actions

### company_enrichment
Enrich a company using its domain name.

**Example parameters:**