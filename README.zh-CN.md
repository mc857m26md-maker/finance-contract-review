# 财务合同审核 Skill

这是一个面向财务 BP、采购财务、财务共享、FP&A 与财务控制人员的开源 Codex Skill。它把商业合同整理为可复核的交易事实、算术校验、风险事项、升级审批和签后义务台账。

它不替代法务、税务、资金、会计政策或有权审批人的专业判断，也不会授权签署、付款、过账或审批。

## 安装

把仓库克隆到 Codex skills 目录：

```bash
git clone https://github.com/mc857m26md-maker/finance-contract-review.git ~/.codex/skills/finance-contract-review
```

可通过 `$finance-contract-review` 显式调用，也支持正常的自动发现。

## 使用示例

上传合同，并尽量同时提供订单/SOW、报价或价格表、补充协议、审批材料和公司审查规则。

```text
使用 $finance-contract-review，从买方/付款方立场审核这份供应商合同。
重点检查金额税额、付款与验收联动、自动续期、责任敞口和签后义务；
每条结论标明页码和条款号。
```

## 输出内容

- `暂停签署`、`满足所列条件后可继续` 或 `未发现财务阻断项`；
- 审核范围、假设、缺失材料和可靠性限制；
- 带原文定位的交易事实表；
- 金额、税额、明细、付款里程碑和跨文件一致性校验；
- 分级风险、财务影响、建议改法/备选方案、责任人与升级路径；
- 需要法务、税务、资金、会计政策、采购、安全或有权审批人判断的事项；
- 签后履约义务台账。

“未发现财务阻断项”只说明已完成的财务检查未发现阻断问题，不代表法务批准、税务意见、签署授权或零风险。

## 结构化规则与计算校验

复制并修改 `assets/finance-playbook.example.json`。投入正式使用前，应由相关制度所有人批准其中的规则。

```bash
python scripts/validate_playbook.py assets/finance-playbook.example.json
python scripts/verify_terms.py assets/deal-terms.example.json
```

第二个脚本只校验输入的结构化金额，不负责从合同抽取数据，也不作法律、税务或会计判断。
字段和退出码见 [references/structured-terms-schema.md](references/structured-terms-schema.md)：退出码 `1` 表示成功执行并发现不一致，`2` 才表示输入或运行错误。

## 安全提示

不要在公开 Issue 或 Pull Request 中上传真实合同、个人信息、账号密钥、受特权保护的材料或企业内部审查规则。详见 [SECURITY.md](SECURITY.md)。

市场调研与设计依据见 [docs/market-landscape.md](docs/market-landscape.md)。项目采用 [MIT 许可证](LICENSE)。
