from audits.ec2 import audit_ec2
from audits.ebs import audit_ebs
from audits.elb import audit_elb
from audits.rds import audit_rds
from audits.dynamodb import audit_dynamodb
from audits.eks import audit_eks
from audits.s3 import audit_s3
from audits.ecr import audit_ecr
from datetime import datetime, timezone

findings = []

print("\n🔍 Running CloudGuard AWS Cost & Stability Audit\n")

findings.extend(audit_ec2())
findings.extend(audit_ebs())
findings.extend(audit_elb())
findings.extend(audit_rds())
findings.extend(audit_dynamodb())
findings.extend(audit_eks())
findings.extend(audit_s3())
findings.extend(audit_ecr())

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
report_file = f"reports/cloudguard_report_{datetime.now(timezone.utc).date()}.md"

with open(report_file, "w") as f:
    f.write("# CloudGuard – AWS Cost & Stability Report\n\n")
    f.write(f"**Generated:** {timestamp}\n\n")
    f.write("## Key Findings\n\n")

    if not findings:
        f.write("✅ No major cost or stability risks detected.\n")
    else:
        for item in findings:
            f.write(f"- {item}\n\n")

    f.write("\n## Notes\n")
    f.write("This audit was performed using read-only access.\n")
    f.write("No resources were modified during this process.\n")

print(f"\n📄 Report generated: {report_file}")
print("\n✅ CloudGuard audit completed.\n")
