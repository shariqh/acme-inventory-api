# GitHub Enterprise Demo - Visual Diagrams

## 1. High-Level Architecture

```mermaid
flowchart TB
    subgraph contractor["👤 Contractor (Unmanaged Device)"]
        browser["🌐 Browser Only"]
    end

    subgraph github["☁️ GitHub Cloud"]
        subgraph codespaces["Codespaces"]
            prebuild["⚡ Prebuilt Environment"]
            vscode["VS Code in Browser"]
            terminal["Terminal Access"]
            code["📁 Source Code"]
        end

        subgraph ghas["GitHub Advanced Security"]
            secrets["🔐 Secret Scanning"]
            codeql["🔍 CodeQL Analysis"]
            dependabot["📦 Dependabot"]
        end

        subgraph governance["🛡️ Governance"]
            codeowners["CODEOWNERS"]
            branchpro["Branch Protection"]
            audit["Audit Logs"]
        end
    end

    browser -->|"HTTPS Only"| vscode
    vscode --> code
    code -->|"Every Commit"| ghas
    ghas --> governance

    style contractor fill:#fee,stroke:#c00
    style github fill:#e8f5e9,stroke:#2e7d32
    style codespaces fill:#e3f2fd,stroke:#1565c0
    style ghas fill:#fff3e0,stroke:#ef6c00
    style governance fill:#f3e5f5,stroke:#7b1fa2
```

---

## 2. Contractor Onboarding Flow

```mermaid
flowchart LR
    subgraph day0["Day 0: Traditional"]
        d0a["Order Laptop"] --> d0b["Ship Device"]
        d0b --> d0c["IT Setup"]
        d0c --> d0d["Install Tools"]
        d0d --> d0e["Configure Access"]
        d0e --> d0f["Clone Repos"]
    end

    subgraph day1["Day 1: With Codespaces"]
        d1a["Grant GitHub Access"] --> d1b["Open Browser"]
        d1b --> d1c["Click 'Create Codespace'"]
        d1c --> d1d["✅ Start Coding"]
    end

    day0 ~~~|"2-3 Weeks"| placeholder1[" "]
    day1 ~~~|"< 1 Hour"| placeholder2[" "]

    style day0 fill:#ffebee,stroke:#c62828
    style day1 fill:#e8f5e9,stroke:#2e7d32
```

---

## 3. Codespaces Prebuild Flow

```mermaid
flowchart TD
    subgraph trigger["Triggers"]
        push["Push to Main"]
        schedule["Weekly Schedule"]
        manual["Manual Trigger"]
    end

    subgraph prebuild["Prebuild Process"]
        start["Start Prebuild"] --> pull["Pull Base Image<br/>Python 3.11"]
        pull --> deps["Install Dependencies<br/>requirements.txt"]
        deps --> ext["Install VS Code Extensions"]
        ext --> snapshot["Create Snapshot"]
    end

    subgraph launch["Developer Experience"]
        click["Developer Clicks<br/>'Create Codespace'"]
        restore["Restore from Snapshot"]
        ready["✅ Ready to Code"]
    end

    trigger --> start
    snapshot --> click
    click --> restore
    restore -->|"~10 seconds"| ready

    style trigger fill:#e3f2fd,stroke:#1565c0
    style prebuild fill:#fff3e0,stroke:#ef6c00
    style launch fill:#e8f5e9,stroke:#2e7d32
```

---

## 4. Security Scanning Pipeline

```mermaid
flowchart TD
    subgraph dev["Developer Actions"]
        write["Write Code"]
        commit["Git Commit"]
        push["Git Push"]
        pr["Open Pull Request"]
    end

    subgraph scanning["GitHub Advanced Security"]
        subgraph secrets["Secret Scanning"]
            pushpro["🚫 Push Protection"]
            secretalert["Secret Alerts"]
        end

        subgraph codeql["CodeQL"]
            analyze["Semantic Analysis"]
            sqli["SQL Injection"]
            path["Path Traversal"]
            xss["XSS Detection"]
        end

        subgraph deps["Dependabot"]
            scan["Dependency Scan"]
            cve["CVE Database"]
            autopr["Auto-Fix PRs"]
        end
    end

    subgraph result["Outcomes"]
        block["❌ Merge Blocked"]
        alert["⚠️ Alert Created"]
        fix["✅ Fix & Merge"]
    end

    write --> commit
    commit --> push
    push -->|"Contains Secret?"| pushpro
    pushpro -->|"Yes"| block
    pushpro -->|"No"| pr
    pr --> codeql
    pr --> deps
    codeql -->|"Vulnerability Found"| block
    deps -->|"CVE Found"| alert
    alert --> autopr
    autopr --> fix

    style dev fill:#e3f2fd,stroke:#1565c0
    style scanning fill:#fff3e0,stroke:#ef6c00
    style result fill:#f3e5f5,stroke:#7b1fa2
```

---

## 5. CODEOWNERS Enforcement Flow

```mermaid
flowchart TD
    subgraph contractor["Contractor"]
        change["Modify .devcontainer/"]
        createpr["Create Pull Request"]
    end

    subgraph github["GitHub Automation"]
        codeowners["CODEOWNERS Check"]
        assign["Auto-Assign Reviewers"]
        require["Require Platform Team Approval"]
    end

    subgraph platform["Platform Team"]
        review["Review Changes"]
        decision{{"Approve?"}}
        approve["✅ Approve"]
        reject["❌ Request Changes"]
    end

    subgraph outcome["Result"]
        merge["Merge Allowed"]
        blocked["Merge Blocked"]
    end

    change --> createpr
    createpr --> codeowners
    codeowners --> assign
    assign --> require
    require --> review
    review --> decision
    decision -->|"Yes"| approve
    decision -->|"No"| reject
    approve --> merge
    reject --> blocked

    style contractor fill:#fee,stroke:#c00
    style github fill:#e3f2fd,stroke:#1565c0
    style platform fill:#e8f5e9,stroke:#2e7d32
```

---

## 6. Complete Security Layer Stack

```mermaid
flowchart TB
    subgraph layers["Defense in Depth"]
        direction TB

        subgraph l1["Layer 1: Push Protection"]
            push1["Secrets blocked BEFORE reaching repo"]
        end

        subgraph l2["Layer 2: PR Security Checks"]
            push2["CodeQL scans every pull request"]
            push3["Vulnerabilities block merge"]
        end

        subgraph l3["Layer 3: Dependency Monitoring"]
            push4["Dependabot monitors CVE databases"]
            push5["Auto-creates fix PRs"]
        end

        subgraph l4["Layer 4: Governance"]
            push6["CODEOWNERS protects critical files"]
            push7["Branch protection enforces reviews"]
        end

        subgraph l5["Layer 5: Audit & Compliance"]
            push8["Every action logged"]
            push9["SOC 2 / FedRAMP compliant"]
        end
    end

    l1 --> l2 --> l3 --> l4 --> l5

    style l1 fill:#ffcdd2,stroke:#c62828
    style l2 fill:#ffe0b2,stroke:#ef6c00
    style l3 fill:#fff9c4,stroke:#f9a825
    style l4 fill:#c8e6c9,stroke:#2e7d32
    style l5 fill:#bbdefb,stroke:#1565c0
```

---

## 7. Demo Flow / Timeline

```mermaid
gantt
    title Demo Timeline (15 minutes)
    dateFormat mm:ss
    axisFormat %M:%S

    section Opening
    Set the stage / Scenario     :a1, 00:00, 2m

    section Codespaces
    Navigate to repo             :a2, after a1, 30s
    Launch Codespace             :a3, after a2, 1m
    Show devcontainer.json       :a4, after a3, 1m
    Explain prebuilds            :a5, after a4, 30s
    Show CODEOWNERS              :a6, after a5, 1m

    section GHAS - Dependabot
    Navigate to Security tab     :b1, after a6, 30s
    Show vulnerability alerts    :b2, after b1, 1m
    Show auto-fix PRs            :b3, after b2, 30s

    section GHAS - CodeQL
    Show code scanning alerts    :c1, after b3, 1m
    Deep dive SQL injection      :c2, after c1, 1m
    Show PR #11 blocked          :c3, after c2, 1m

    section GHAS - Secrets
    Explain push protection      :d1, after c3, 1m

    section Wrap-up
    Tie back to scenario         :e1, after d1, 1m
    Q&A                          :e2, after e1, 1m
```

---

## 8. Value Proposition Summary

```mermaid
mindmap
  root((GitHub Enterprise))
    Velocity
      Codespaces
        Instant dev environments
        Prebuilt containers
        No device provisioning
      Standardization
        Identical environments
        No "works on my machine"
        Day 1 productivity
    Security
      Secret Scanning
        Push protection
        Never reaches repo
      CodeQL
        Semantic analysis
        PR blocking
        Data flow tracing
      Dependabot
        CVE monitoring
        Auto-fix PRs
        Continuous updates
    Governance
      CODEOWNERS
        Platform team control
        Protected configurations
      Branch Protection
        Required reviews
        Required checks
      Audit Trail
        Every action logged
        Compliance ready
```

---

## 9. Before/After Comparison

```mermaid
flowchart LR
    subgraph before["❌ Before GitHub Enterprise"]
        direction TB
        b1["2-3 weeks to onboard"]
        b2["Source code on laptops"]
        b3["Quarterly security audits"]
        b4["Manual dependency tracking"]
        b5["Secrets in git history"]
    end

    subgraph after["✅ After GitHub Enterprise"]
        direction TB
        a1["< 1 hour to onboard"]
        a2["Code stays in cloud"]
        a3["Continuous scanning"]
        a4["Automated CVE alerts"]
        a5["Push protection blocks secrets"]
    end

    before -.->|"Transform"| after

    style before fill:#ffebee,stroke:#c62828
    style after fill:#e8f5e9,stroke:#2e7d32
```

---

## 10. Cost-Benefit Overview

```mermaid
quadrantChart
    title GitHub Enterprise ROI
    x-axis Low Cost --> High Cost
    y-axis Low Value --> High Value
    quadrant-1 Strategic Investment
    quadrant-2 Quick Wins
    quadrant-3 Avoid
    quadrant-4 Optimize

    Codespaces Prebuilds: [0.3, 0.85]
    Secret Push Protection: [0.2, 0.95]
    CodeQL Scanning: [0.4, 0.9]
    Dependabot: [0.1, 0.8]
    CODEOWNERS: [0.1, 0.7]
    Branch Protection: [0.1, 0.75]
```

---

## Screenshot Guide

For your presentation, capture these diagrams:

1. **Slide: "The Challenge"** → Use Diagram #2 (Contractor Onboarding Flow)
2. **Slide: "Our Solution"** → Use Diagram #1 (High-Level Architecture)
3. **Slide: "Instant Productivity"** → Use Diagram #3 (Codespaces Prebuild Flow)
4. **Slide: "Security at Every Step"** → Use Diagram #4 (Security Scanning Pipeline)
5. **Slide: "Governance & Control"** → Use Diagram #5 (CODEOWNERS Enforcement)
6. **Slide: "Defense in Depth"** → Use Diagram #6 (Security Layer Stack)
7. **Slide: "The Transformation"** → Use Diagram #9 (Before/After)
8. **Slide: "Summary"** → Use Diagram #8 (Value Proposition Mindmap)
