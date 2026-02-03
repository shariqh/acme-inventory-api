# GitHub Enterprise Demo Talk Track
## Acme Corp Contractor Onboarding Scenario

**Demo Duration:** ~15 minutes
**Audience:** Technical Director + CISO
**Scenario:** Acme Corp is onboarding 50 offshore contractors for a 12-month modernization project. They need fast developer productivity without device procurement headaches, while maintaining SOC 2 compliance and ensuring source code never lands on unmanaged devices.

---

## PART 1: OPENING (0-2 min)

**[Start on any neutral screen]**

> "Thanks for your time today. I understand Acme Corp is bringing on 50 offshore contractors for a 12-month modernization effort.
>
> Your Technical Director needs these developers writing code in days, not weeks. Your CISO needs to ensure source code never lands on unmanaged devices—and that you maintain SOC 2 compliance throughout.
>
> I'm going to show you how GitHub solves both problems with one platform. We'll cover two things:
> 1. How contractors get productive immediately without any device provisioning
> 2. How every line of code is automatically scanned for security issues before it reaches production
>
> Let's start with the productivity challenge."

---

## PART 2: CODESPACES (2-7 min)

**[Navigate to: https://github.com/shariqh/acme-inventory-api]**

> "This is a typical internal microservice—a Python Flask API for inventory management. Let me show you how a contractor would start working on day one."

**[Click green "Code" button → "Codespaces" tab → "Create codespace on main"]**

> "The contractor opens their browser, clicks one button, and..."

**[Wait for Codespace to load - ~30-60 seconds]**

> "While this spins up—notice what's NOT happening:
> - No git clone to a local machine
> - No Python installation
> - No 'works on my machine' debugging
> - And critically—no source code touching an unmanaged device
>
> The code stays here, in your controlled GitHub environment."

**[Once loaded, show VS Code in browser]**

> "Full VS Code—in a browser. Terminal, extensions, everything. Let me show you something."

**[Click on `.devcontainer/devcontainer.json` in the file tree]**

> "This file is the magic. It defines exactly what every developer gets:
> - Python 3.11
> - Specific linting rules
> - Pre-installed extensions
> - Even the port forwarding for testing
>
> Every single contractor gets this identical environment. No configuration drift. No 'I'm on Python 3.9 and it works for me.' Day one, they're productive."

**[Show that Codespaces are prebuilt]**

> "And notice how fast that started? We have prebuilds configured. GitHub automatically builds fresh development environments whenever the main branch changes. Your contractors don't wait for dependencies to install—they get a ready-to-code environment instantly.
>
> For a team of 50 contractors, that's 50 people who aren't waiting 5-10 minutes for pip install. Multiply that by every branch switch, every morning standup. Prebuilds pay for themselves in developer time."

**[Optional: Run `flask run` in terminal to show it works]**

> "For your CISO—source code never leaves GitHub's infrastructure. Contractors can work from a coffee shop, a personal laptop, anywhere. Your code stays right here."

**[Click on `.github/CODEOWNERS` in the file tree]**

> "Now here's the governance layer. This CODEOWNERS file defines who can approve changes to critical files.
>
> See these paths? The `.devcontainer` folder, the CI workflows, the dependency files—all locked to the platform team. If a contractor tries to modify the development environment—disable a linter, remove a security extension, change a dependency—the PR requires platform team approval.
>
> They can write application code all day long. But they cannot change the guardrails. GitHub enforces this automatically through branch protection rules."

**[Pause for questions, then transition]**

> "So that's velocity. Now let's talk about what happens when 50 contractors start committing code. More developers means more output—but also more surface area for security issues."

---

## PART 3: GITHUB ADVANCED SECURITY (7-13 min)

**[Navigate to: Security tab on the repo]**

> "GitHub Advanced Security gives you three layers of protection. Let me walk through each."

---

### 3A: DEPENDABOT (2 min)

**[Click "Dependabot" in the Security tab sidebar]**

> "First—your dependencies. This repo has 20 known vulnerabilities in its dependencies right now."

**[Show the list of alerts]**

> "These aren't theoretical. CVE-2018-18074 in the requests library, CVE-2020-1747 in PyYAML—real vulnerabilities with real exploits in the wild.
>
> But here's what's different from a quarterly security audit..."

**[Click "Pull requests" tab, show Dependabot PRs]**

> "Dependabot already created pull requests to fix them. Your developers review, run the tests, merge. This runs continuously—not quarterly, not monthly. Every day."

---

### 3B: CODE SCANNING / CODEQL (4 min)

**[Navigate to: Security tab → Code scanning]**

> "Second layer—the code itself. CodeQL is GitHub's semantic code analysis engine."

**[Show the alerts list - SQL injection, path traversal, etc.]**

> "It found four issues in this codebase. Let me show you the critical one."

**[Click into the SQL injection alert (py/sql-injection)]**

> "This is a SQL injection vulnerability. But CodeQL didn't just pattern-match the word 'SELECT.' Watch this."

**[Click "Show paths" or expand the data flow visualization]**

> "It traced the data flow. User input comes in through the route parameter here... flows through the code... and ends up concatenated directly into a SQL query here. That's exploitable.
>
> Your security team gets the CWE reference, the severity score, and the exact remediation path. Developers see this inline in their pull request."

**[Navigate to PR #11: https://github.com/shariqh/acme-inventory-api/pull/11]**

> "Let me show you what that looks like in practice. A developer on my team added a search feature yesterday."

**[Show the Checks tab on the PR]**

> "Tests passed. But look—CodeQL is blocking the merge. The developer introduced a SQL injection vulnerability in their new code.
>
> This PR cannot be merged until they fix it. The feedback happens here, in the pull request, not three months later in a penetration test report."

---

### 3C: SECRET SCANNING (2 min)

**[Navigate to: Settings → Code security and analysis (or just explain)]**

> "Third layer—secrets. Push protection is enabled on this repository.
>
> If a developer tries to commit an AWS key, a Stripe API key, a GitHub token—the push is rejected before it ever reaches the repository. They get immediate feedback: 'This commit contains a secret. Remove it and try again.'
>
> The secret never enters your git history. You don't have to rotate credentials because they were never exposed."

**[If they want proof, you can mention:]**

> "I tested this earlier—tried to push a Stripe key. GitHub blocked it at the command line with the exact secret type and line number."

---

## PART 4: WRAP-UP (13-15 min)

**[Return to repo main page or a neutral screen]**

> "Let me tie this back to your scenario.
>
> Your 50 contractors are productive in hours, not weeks. They open a browser, click a button, and start coding in a standardized environment. No device procurement, no configuration headaches.
>
> Your source code never touches an unmanaged device. It stays in GitHub's infrastructure, which is SOC 2 Type II certified, FedRAMP authorized, and used by 90% of the Fortune 100.
>
> And every commit—from every contractor—is automatically scanned:
> - Secrets are blocked before they're pushed
> - Vulnerabilities are flagged in the pull request
> - Dependencies are monitored continuously
>
> Your developers get feedback in their workflow. Your security team gets visibility across every repository. And your auditors get the paper trail they need.
>
> What questions do you have?"

---

## OBJECTION RESPONSES

| If they ask... | You say... |
|----------------|------------|
| "What about latency for offshore teams?" | "Codespaces runs on Azure with global regions. We'd want to test with your specific locations, but customers with teams in India and Eastern Europe report it's responsive for daily development." |
| "We already use SonarQube / Checkmarx" | "GitHub's advantage is shift-left. Developers see findings inline in their PR, not in a separate report after merge. Friction is lower, so adoption is higher. You're also consolidating tools—one platform for code, CI, and security." |
| "What about false positives?" | "CodeQL is tunable, and dismissed alerts stay dismissed. Industry benchmarks put CodeQL's false positive rate around 15%, which is leading for SAST tools." |
| "How does this integrate with Jira/ServiceNow?" | "Full API access and webhooks for all alerts. Many customers auto-create tickets via GitHub Actions. You can also use the native Security Overview for reporting." |
| "What's the cost?" | "Codespaces is usage-based—pay for compute hours, control machine types. GHAS is per active committer. For 50 contractors, I'd want to understand your repo count to scope it properly. Happy to connect you with our team for a detailed estimate." |
| "Can contractors bypass the security scanning?" | "No. Branch protection rules require all checks to pass before merge. And the devcontainer configuration is locked down via CODEOWNERS—only your platform team can approve changes to the development environment." |
| "What if contractors need to work offline?" | "Codespaces requires connectivity. For hybrid scenarios, you could allow cloning to managed VDI instances as a fallback. The key is you control the policy centrally." |

---

## KEY URLS FOR YOUR DEMO

| Resource | URL |
|----------|-----|
| **Repo** | https://github.com/shariqh/acme-inventory-api |
| **Security tab** | https://github.com/shariqh/acme-inventory-api/security |
| **PR #11 (blocked by CodeQL)** | https://github.com/shariqh/acme-inventory-api/pull/11 |
| **Dependabot PRs** | https://github.com/shariqh/acme-inventory-api/pulls?q=is%3Apr+author%3Aapp%2Fdependabot |
| **Code scanning alerts** | https://github.com/shariqh/acme-inventory-api/security/code-scanning |

---

## PRE-DEMO CHECKLIST

- [ ] Browser Tab 1: Repo main page (for Codespaces launch)
- [ ] Browser Tab 2: Security tab (pre-loaded)
- [ ] Browser Tab 3: PR #11 (pre-loaded)
- [ ] Browser Tab 4: GitHub docs for org-level policies (backup)
- [ ] Close any existing Codespaces to show fresh launch
- [ ] Test Codespace launch works (delete and recreate if needed)
- [ ] Verify Security tab shows alerts
- [ ] Verify prebuilds are configured (see setup below)
- [ ] Have backup screenshots ready in case of demo failures

---

## SETUP INSTRUCTIONS

### Configure Codespaces Prebuilds

Prebuilds must be configured in the GitHub UI:

1. Go to **Settings → Codespaces → Prebuilds**
2. Click **Set up prebuild**
3. Configure:
   - **Branch:** main
   - **Configuration:** .devcontainer/devcontainer.json
   - **Region:** Select regions closest to your contractors (e.g., US West, Europe West, Southeast Asia)
   - **Prebuild triggers:**
     - ✓ On push (rebuilds when main changes)
     - ✓ On configuration change (rebuilds when devcontainer.json changes)
   - **Template retention:** Keep 2 versions
4. Click **Create**

Prebuilds typically take 5-10 minutes to build initially. After that, new Codespaces launch in seconds.

### Enable CODEOWNERS Enforcement

For CODEOWNERS to actually block merges, you need branch protection:

1. Go to **Settings → Branches → Branch protection rules**
2. Click **Add rule** (or edit existing rule for `main`)
3. Configure:
   - **Branch name pattern:** `main`
   - ✓ **Require a pull request before merging**
   - ✓ **Require approvals** (set to 1 or more)
   - ✓ **Require review from Code Owners**
   - ✓ **Require status checks to pass before merging**
     - Add: `test`, `CodeQL`
   - ✓ **Require branches to be up to date before merging**
   - ✓ **Do not allow bypassing the above settings**
4. Click **Save changes**

Now any PR that touches files in CODEOWNERS (like `.devcontainer/`) will require approval from the designated owners.

### Verify Security Features

1. **Dependabot:** Settings → Code security and analysis → Dependabot alerts ✓
2. **Secret scanning:** Settings → Code security and analysis → Secret scanning ✓
3. **Push protection:** Settings → Code security and analysis → Push protection ✓
4. **Code scanning:** Should auto-run via `.github/workflows/ci.yml`

---

## ARCHITECTURE DIAGRAM (for whiteboarding)

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CONTRACTOR LAPTOP                           │
│                      (unmanaged device)                             │
│                              │                                      │
│                         Browser Only                                │
│                              │                                      │
└──────────────────────────────┼──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     GITHUB CLOUD                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    CODESPACES                                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │   │
│  │  │ Prebuilt    │  │ VS Code     │  │ Terminal    │         │   │
│  │  │ Environment │  │ (Browser)   │  │ Access      │         │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘         │   │
│  │                                                              │   │
│  │  Source code NEVER leaves this boundary                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                               │                                      │
│                               ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              GITHUB ADVANCED SECURITY                        │   │
│  │                                                              │   │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐        │   │
│  │  │   Secret     │ │   CodeQL     │ │  Dependabot  │        │   │
│  │  │  Scanning    │ │  Analysis    │ │   Alerts     │        │   │
│  │  │              │ │              │ │              │        │   │
│  │  │ Push         │ │ SQL Inject.  │ │ CVE          │        │   │
│  │  │ Protection   │ │ Path Trav.   │ │ Monitoring   │        │   │
│  │  └──────────────┘ └──────────────┘ └──────────────┘        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                               │                                      │
│                               ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    GOVERNANCE                                │   │
│  │                                                              │   │
│  │  • CODEOWNERS - Platform team approves env changes          │   │
│  │  • Branch Protection - Require passing checks               │   │
│  │  • Audit Logs - Every action tracked                        │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```
