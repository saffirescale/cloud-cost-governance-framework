# CloudGuard – AWS Cost & Stability Audit

CloudGuard is a **short, focused AWS audit** designed to help startups and small teams
understand where their cloud money is going and identify stability risks —
**without modifying or deleting any resources**.

This repository contains the **methodology and reference implementation**
used during CloudGuard engagements by **Saffire Scale**.

---

## What CloudGuard Is

✔ A read-only AWS cost & stability audit  
✔ Consultant-led (not a SaaS tool)  
✔ Safe to run on production accounts  
✔ Delivers clear, actionable recommendations in 3–5 days  

---

## What CloudGuard Is NOT

✖ Not an automated cleanup tool  
✖ Not a FinOps platform  
✖ Not long-term monitoring software  
✖ Not a replacement for architecture redesign  

---

## Problems CloudGuard Solves

As AWS usage grows, teams often face:

- Increasing bills without clear attribution
- Stopped or idle resources still incurring cost
- Lack of visibility into system health
- Reactive incident handling

CloudGuard provides **clarity first**, before scaling further.

---

## Audit Coverage (Typical)

CloudGuard reviews the following areas:

- EC2 instances (running / stopped)
- Unattached EBS volumes
- Load balancers (existence & exposure)
- RDS instances (active / stopped)
- Basic CloudWatch visibility
- High-level cost usage patterns
- Checks EKS, ECR, DB, S3.

> Coverage may vary slightly based on the AWS account and scope agreed.

---

## Safety & Access Model (IMPORTANT)

CloudGuard operates with **read-only IAM access**.

- No resources are modified automatically
- No deletions are performed without approval
- All findings are shared before any action

### Required IAM Permissions (Read-only)
```json
ec2:Describe*
elasticloadbalancing:Describe*
rds:Describe*
cloudwatch:Describe*
ce:GetCostAndUsage
```


