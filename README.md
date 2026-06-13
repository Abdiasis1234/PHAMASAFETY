# PHAMASAFTEY

⭐ 1. “Pharma Safety Tri‑Agent System”
For pharmaceutical companies handling adverse drug reaction (ADR) reports.
Why this is niche
Pharma companies legally must process ADR reports quickly and accurately.
This is a £10B+ compliance market.

Agents
Personal Agent (PA)

Parses patient or doctor messages

Extracts symptoms, medication, dosage, timeline

Detects severity (e.g., “life‑threatening”, “mild”)

Writes structured ADR report into Redis

Customer Service Agent (CSA)

Determines if the case must be escalated

Checks if required fields are missing

Requests more info via PA

Sends research queries to RA

Research Agent (RA)

Looks up known side effects

Checks drug–drug interactions

Retrieves regulatory rules (MHRA, EMA, FDA)

Returns structured risk assessment
