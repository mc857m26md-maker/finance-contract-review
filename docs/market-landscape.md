# Contract review tooling landscape

Research date: 2026-09-17. This is a capability map, not a ranking or procurement recommendation. Product claims come from vendor documentation unless stated otherwise and should be validated in a proof of concept using representative contracts, languages, jurisdictions, and security requirements. Features and packaging change frequently.

## Market map

| Product | Category | Publicly described strengths | Finance-review design lesson | Source |
|---|---|---|---|---|
| Spellbook | Word-based drafting/review copilot | Contract risk review, direct redlines, custom playbooks, clause drafting, and Word integration | Review must be usable where people edit; reusable positions and fallback language reduce reviewer drift | [Product](https://www.spellbook.legal/reviews-light-mode), [help center](https://help.spellbook.legal/en/articles/9079366-using-spellbook-as-a-transactional-lawyer) |
| Robin AI | Contract review and drafting assistant | Word-based clause search, summaries, redline summaries, drafting, proofreading, and missing-information checks | A finance review should expose missing data and summarize changes, not only classify clauses | [Word add-in](https://robinai.com/news-and-resources/robin-university/word-add-in-an-intelligent-ai-sidekick-for-contract-review) |
| Luminance | Legal AI for negotiation, review, and diligence | Automated contract review, information extraction, and Word-centered negotiation capabilities | Pre-signature review and portfolio/diligence analysis are different modes and should not be conflated | [Diligence brochure](https://www.luminance.com/files/brochures/Diligence-AI%20for%20Automated%20Contract%20Review-2024.pdf), [corporate brochure](https://www.luminance.com/files/brochures/Corporate%20Product%20Sheet%202025%20%28UK%29.pdf) |
| LegalOn | Contract review platform | Attorney-built and custom playbooks, risk ranking, sourced answers, Word/browser review, redlines, and contract vault | Evidence links, role-specific playbooks, preferred/fallback positions, and human control are foundational | [Playbooks](https://us-direct.legalontech.com/contract-playbooks), [overview](https://www.legalontech.com/what-is-legalon) |
| Ironclad | Enterprise CLM | AI playbooks, clause detection, preferred/fallback terms, clause approvers, permissions, redlining, and workflow | Non-standard finance terms should route to named approvers rather than remain as passive warnings | [Playbooks overview](https://support.ironcladapp.com/hc/en-us/articles/12275685560215-Ironclad-AI-Playbooks-Overview), [review](https://ironcladapp.com/product/review-contracts) |
| Juro | AI contract workflow / CLM | Word review against controlled playbooks, automated redlines, summaries, approval routing, version control, and priority levels | Review severity should reflect the organization's priorities, while execution rights remain role-restricted | [AI review](https://juro.com/ai-contract-review), [priority levels](https://juro.com/product-updates/january-2026) |
| LinkSquares | CLM and contract intelligence | Agreement and redline summaries, sourced document Q&A, AI-assisted drafting/redlining, OCR, metadata extraction, dashboards | A useful result combines document-level evidence with portfolio visibility and version-change analysis | [Word review](https://help.linksquares.com/hc/en-us/articles/22984722372759-LinkSquares-Finalize-for-Word-Add-In-AI-Powered-Contract-Review), [repository](https://linksquares.com/products/analyze/features/) |
| Icertis | Enterprise contract intelligence / CLM | Playbook review, risk assessment, contract search, summaries, insight extraction, and agentic workflows | Governance and company-standard compliance must remain explicit in enterprise automation | [Playbook Review](https://www.icertis.com/contentassets/4e8777886d1148beb251798ff0e9715d/playbook-review-for-icertis-copilot-datasheet.pdf), [Copilot](https://www.icertis.com/contentassets/38c6c60d138e466aa49e927341fa15ad/icertis-copilot-datasheet.pdf) |
| Workday CLM, powered by Evisort AI | CLM and portfolio intelligence | Automated redlining, clause library, templates, Ask AI across contracts, custom models, search, dashboards, and obligation visibility | Finance value extends beyond signing to renewal, rebate, savings, exposure, and audit tracking | [CLM product](https://www.workday.com/en-us/products/contract-management/contract-lifecycle-management.html), [finance/contract intelligence announcement](https://investor.workday.com/news-and-events/press-releases/news-details/2025/Evisort-AI-Powered-Contract-Intelligence-Now-Available-Through-Workday-03-27-2025/default.aspx) |
| MeCheck (幂律智能) | China-focused AI contract review | Configurable review rules, contract/party risk analysis, traceable reasoning, and business/legal/finance risk dimensions | Local products emphasize configurable rules and multi-function review; finance checks should be first-class, not an afterthought | [Official site](https://mecheck.net.cn/) |
| iTerms (法大大) | China-focused legal AI and contract lifecycle | Clause risk and revision suggestions, version comparison, drafting, extraction, collaboration, execution/archiving, and party checks | Version differences and counterparty identity should be reviewed alongside the contract text | [Official site](https://www.iterms.com/), [party review](https://www.fadada.com/article/Brand-000774) |
| 法天使 | China-focused legal AI platform | Contract parsing, built-in and enterprise rules, risk location, multi-department perspectives, drafting, and private deployment | Shared legal rules and company rules should be distinguishable, maintainable, and approved by their owners | [Platform](https://dev-leg.fatianshi.cn/) |
| 甄零科技 | China-focused CLM / business-finance-legal integration | Contract lifecycle and business-finance-legal data integration, AI review, structured extraction, and workflow | A finance skill should connect contract terms to operational data and approval evidence, even when it remains tool-neutral | [Official site](https://www.onecontract-cloud.com/), [AI review article](https://www.onecontract-cloud.com/news-337) |

## Open-source signals

Open-source projects are useful for architecture and reproducibility, but they vary widely in maturity and should not be treated as validated legal products.

| Project | Public approach | Useful signal | Source |
|---|---|---|---|
| terms-ai | LLM-based summaries, clause review, redlines, and recommendations | A clear report should separate executive summary, clause findings, redlines, and actions | [GitHub](https://github.com/nkasuku/terms-ai) |
| Counsel OS | Skill-oriented review against an organization's own positions, with citations and institutional knowledge | A review skill benefits from composable instructions and user-owned standards | [GitHub](https://github.com/eigenlegal/counsel-os) |
| Vaulytica | Deterministic, browser-based legal-document linting | Deterministic checks are valuable for reproducibility and auditability; use them where inputs can be structured | [GitHub](https://github.com/clay-good/vaulytica) |

## Cross-market capability pattern

Across the reviewed products, the most repeatable design pattern is:

1. classify the contract and the reviewer's position;
2. extract clauses, facts, obligations, and missing information;
3. compare them with a controlled playbook;
4. show source evidence and ranked deviations;
5. propose redlines or fallbacks;
6. route exceptions to the correct approver;
7. retain version history and convert signed terms into searchable obligations.

The finance-contract-review skill adopts that pattern and adds finance-specific controls that vendor pages often mention only indirectly: deterministic arithmetic, payment/acceptance/invoice alignment, tax uncertainty routing, bank-detail controls, discounts and rebates, accounting-policy flags, authorization boundaries, and a post-signature owner/date/evidence register.

## Procurement questions for any contract-review product

Use a representative proof of concept rather than a polished demo. Ask:

- Can it cite the exact clause/page for every conclusion and preserve the original document?
- Can different playbooks apply by contract type, jurisdiction, business unit, and payer/payee side?
- Can it separate preferred, fallback, prohibited, and approval-required positions?
- Does it recalculate amounts, tax, line items, and milestones, or only summarize text?
- Can it compare the contract with a PO, SOW, pricing sheet, amendment, or approval memo?
- How does it handle OCR, tables, scanned appendices, bilingual documents, and missing pages?
- Can reviewers accept/reject changes individually, and is there a complete audit trail?
- Can exceptions route to legal, finance, tax, treasury, procurement, security, and accounting-policy owners?
- What are the data retention, model training, data residency, encryption, access-control, and subprocessors terms?
- Is private or on-premises deployment available, and what features are lost in that mode?
- Can signed obligations generate reminders for renewals, rebates, price changes, guarantees, invoices, and notices?
- What are measured precision/recall and false-negative rates on your own contracts, and how are model changes governed?

## 中文结论

市面产品的成熟能力集中在 Playbook、原文定位、红线修改、版本比对、审批流和签后合同数据。面向财务的可复用 Skill 还必须补足四点：一是金额与税额的确定性复算；二是付款、开票、交付和验收的闭环；三是预算、授权、银行信息和专业职能的升级边界；四是把续期、返利、调价、担保和通知期限转成签后台账。本仓库据此设计，不宣称替代法务或专业意见。
