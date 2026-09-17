# 财务合同审核 Finance Contract Review

![财务合同审核](assets/social-preview.png)

[![自动测试](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/test.yml/badge.svg)](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/test.yml)
[![GitHub Pages](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/pages.yml/badge.svg)](https://github.com/mc857m26md-maker/finance-contract-review/actions/workflows/pages.yml)
[![MIT License](https://img.shields.io/badge/License-MIT-0F172A.svg)](LICENSE)

**先有证据，再有结论。** 这是一个面向财务 BP、采购财务、FP&A、应付、共享中心和财务控制人员的开源合同审核 Skill 与 Plugin。

它把合同整理成可复核的交易事实、金额校验、风险事项、升级审批和签后义务台账，不替代法务、税务、资金、会计政策或有权审批人的专业判断。

[在线介绍](https://mc857m26md-maker.github.io/finance-contract-review/) · [完整示例](examples/acme-cloud-services.review.md) · [市场调研](docs/market-landscape.md) · [English](README.md)

## 先看它能发现什么

仓库内置了一份完全虚构的供应商合同，故意放入五个常见财务风险：

| 风险 | 合同证据 | 可能后果 |
|---|---|---|
| 总金额勾稽不一致 | 不含税 100,000，税 6,000，合同总额却写 105,000 | PO、暂估、发票或付款金额错误 |
| 付款比例合计 110% | 预付 30% + 验收后 80% | 超额付款 |
| 三天未反馈视为验收 | 合同没有客观验收标准 | 尚未取得可用成果即触发付款 |
| 邮件即可修改收款账户 | 没有独立回拨和双人复核 | 付款重定向欺诈 |
| 自动续期同时涨价 15% | 取消需提前 60 天 | 预算外支出和错过退出窗口 |

查看[虚构合同](examples/acme-cloud-services.synthetic.md)及其[带证据的审核报告](examples/acme-cloud-services.review.md)。示例不含任何真实合同数据。

## 安装

### 推荐：让 Codex 从 GitHub 安装

在 Codex 中输入：

```text
使用 $skill-installer 安装：
https://github.com/mc857m26md-maker/finance-contract-review/tree/main/skills/finance-contract-review
```

安装后新建会话，上传合同并输入：

```text
使用 $finance-contract-review，从买方和付款方立场审核这份供应商合同。
重点检查金额税额、付款与验收、自动续期、收款账户变更、责任敞口和签后义务，
每项重要结论都标明证据位置。
```

### 手工安装

```bash
git clone https://github.com/mc857m26md-maker/finance-contract-review.git
cp -R finance-contract-review/skills/finance-contract-review ~/.agents/skills/
```

仓库同时按照 [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) 打包为纯 Skill Plugin，便于后续目录和团队分发。

## 输出内容

1. `暂停签署`、`满足所列条件后可继续` 或 `未发现财务阻断项`；
2. 审核范围、假设、缺失材料和可靠性限制；
3. 带原文定位的交易事实和跨文件勾稽；
4. 金额、税额、付款比例、币种和日期重算；
5. 风险后果、建议控制、责任人与升级路径；
6. 带日期、公式和证据的签后义务台账。

“未发现财务阻断项”不代表法务批准、税务意见、签署授权或零风险。

## 确定性校验

```bash
python skills/finance-contract-review/scripts/validate_playbook.py \
  skills/finance-contract-review/assets/finance-playbook.example.json

python skills/finance-contract-review/scripts/verify_terms.py \
  skills/finance-contract-review/assets/deal-terms.example.json

python -m unittest discover -s tests -v
```

计算脚本只校验输入的结构化数据，不负责从合同抽取条款，也不作法律、税务或会计判断。

## 为什么值得使用

- **财务优先：** 覆盖付款、开票、税额、验收、返利、续期、授权和现金敞口；
- **证据可追溯：** 重要结论必须回到页码、条款或原文；
- **能计算就不猜：** 金额和比例交给确定性脚本重算；
- **按企业规则审核：** 区分首选、备选、禁止和升级条件；
- **覆盖签后执行：** 把关键条款转换成责任人和日期明确的义务；
- **保留人工责任：** 不替用户签署、付款、审批或作专业法律结论。

## 隐私与安全

本项目本身不运行服务器，也不收集遥测信息。使用者仍需确认承载产品和连接工具是否获准处理相关合同数据。不要把真实合同、个人信息、银行账号或内部 Playbook 上传到公开 Issue。详见[隐私说明](PRIVACY.md)、[安全说明](SECURITY.md)和[使用条款](TERMS.md)。

## 参与项目

最有价值的贡献包括：虚构测试合同、可复现的漏检场景、经过批准的财务控制规则以及可验证的输出示例。

- [反馈使用效果](https://github.com/mc857m26md-maker/finance-contract-review/issues/new?template=usage_feedback.yml)
- [报告问题](https://github.com/mc857m26md-maker/finance-contract-review/issues/new?template=bug_report.yml)
- [提出新功能](https://github.com/mc857m26md-maker/finance-contract-review/issues/new?template=feature_request.yml)
- 查看[贡献指南](CONTRIBUTING.md)和[路线图](ROADMAP.md)

如果它确实帮你节省了时间或避免了财务控制遗漏，欢迎 Star，并把示例分享给另一位财务审核人员。

## 许可证

[MIT](LICENSE)
