# Postmortem: Database Outage on PawSitters Platform
## Issue Summary
**Duration:** August 12, 2024, 14:00 - 16:30 UTC
**Impact:** PawSitters platform was fully down, affecting 100% of users. Users were unable to log in, book services, or view profiles.
**Root Cause:** A misconfigured firewall rule blocked all incoming connections to the MySQL database server.

## Timeline
**14:00 UTC:** Issue detected through monitoring alerts indicating database connection failures.
**14:05 UTC:** We began investigating the database server's health and connectivity.
**14:15 UTC:** Initial assumption was a database server crash or overload.
**14:30 UTC:** Misleading investigation into database performance metrics showed no signs of overload or crash.
**15:00 UTC:** Decided to check firewall and network configurations.
**15:15 UTC:** Identified a recent firewall rule change that blocked incoming traffic to the database server.
**15:30 UTC:** Reverted firewall rule to allow traffic to the database server.
**15:45 UTC:** Database connections restored, and platform functionality gradually returned.
**16:30 UTC:** Full service restored; monitoring confirmed no further issues.

## Root Cause and Resolution
### Root Cause
The root cause of the outage was a misconfigured firewall rule implemented during a routine security update. The new rule inadvertently blocked all incoming traffic to the MySQL database server, causing a complete disruption of the database services required by the PawSitters platform.

### Resolution
The resolution involved reverting the firewall rule change that blocked the database server traffic. Once we identified the problematic rule, we promptly updated the firewall configuration to restore the proper traffic flow. The database server was then able to accept incoming connections, and the platform services resumed normal operation.

## Corrective and Preventative Measures
### Improvements and Fixes
**Firewall Rule Auditing:** Implement a stricter review and testing process for firewall rule changes to ensure they do not inadvertently block critical services.
**Monitoring Enhancements:** Improve monitoring to detect and alert on firewall configuration issues more effectively.
**Change Management:** Enhance change management protocols to include detailed impact analysis and rollback procedures for network configuration changes.


### Task List
**Patch Firewall Configurations:** Review and update all firewall configurations to prevent similar issues in the future.
**Add Monitoring on Firewall Rules:** Implement monitoring to track changes in firewall rules and alert on potential misconfigurations.
**Conduct Training:** Undergo additional training on the importance of careful firewall rule management.
**Update Change Management Process:** Revise the change management process to include comprehensive impact assessments and rollback plans for all network and security changes.
**Conduct Postmortem Review:** Hold a postmortem review meeting to discuss the incident, share lessons learned, and refine preventative measures.

By addressing these areas, we aim to prevent future incidents and ensure a more resilient and reliable PawSitters platform.

#### Side note
PawSitters is the portfolio project my peer and I are currently working on as part of our ALX SE foundations program. It is an online platform that connects pet owners with trusted and reliable sitters and walkers for their pets. The platform allows users to log in, book services, and manage profiles seamlessly.