# CloudGuard – Execution Steps

This document explains how a CloudGuard audit is executed, from access setup to final report delivery.

Duration: 3–5 working days  
Access level: Read-only  
Risk level: Zero (no changes performed automatically)

---

## 1. Engagement Overview
CloudGuard is a focused AWS audit to identify cost inefficiencies and stability risks without modifying resources.

## 2. Access & Safety Model
- Read-only IAM access only
- No delete or modify permissions
- No credentials retained after engagement

## 3. Pre-Audit Setup
- AWS credentials configured via standard SDK
- Regions defined in config/regions.yaml
- Scripts verified for read-only behavior

## 4. Audit Execution
- EC2 audit: stopped instances, underutilized instances, untagged resources
- EBS audit: unattached volumes, underutilized volumes, old snapshots
- ELB audit: active load balancers, unused load balancers
- RDS audit: stopped databases, underutilized databases, old snapshots
- S3 audit: public buckets, unused buckets, large objects
- IAM audit: unused users, excessive permissions, access key age
- Lambda audit: unused functions, high error rates

## 5. Report Generation
- Findings collected automatically
- Markdown report generated under reports/
- Human-readable and client-safe

## 6. Client Walkthrough
- Explain findings
- Discuss impact
- Recommend next steps

## 7. Optional Cleanup
- Manual only
- Written approval required

## 8. Closure
- Final report delivered
- Access revoked
- Engagement closed
