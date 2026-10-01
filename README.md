# Zotero Literature Tools

这套小工具把 Zotero 作为原始文献库，把 GitHub 作为可审计的元数据和脚本仓库。R 是主语言，Python 只负责轻量文本处理和跨平台辅助。

## 推荐工作流

1. Zotero 中用 DOI/PMID 添加条目，修正标题、作者、年份、期刊和物种/模型标签。
2. 用 Better BibTeX 导出一个不包含本地附件路径的 `.bib` 文件。
3. 用 `python/doi_normalize.py` 清理 DOI，用 `Rscript R/audit_bibtex.R references.bib` 检查重复 key/DOI。
4. 用 `Rscript R/bib_to_papers_csv.R references.bib data/papers.csv` 生成文献主索引，再补充实验设计和项目关联。
5. 按 `templates/zotero-note.md` 创建阅读笔记，并把可核查结论同步到 evidence 仓库。

## 工具

~~~text
R/audit_bibtex.R             BibTeX key、DOI 和必填字段审计
R/bib_to_papers_csv.R        用 bib2df 转换为 papers.csv
python/doi_normalize.py      DOI 规范化与去重
python/bib_to_csv.py         无第三方依赖的轻量 BibTeX 转 CSV
templates/zotero-note.md     每篇论文的结构化笔记
config/zotero.yml            导出字段和隐私规则
~~~

## Zotero 约定

- Better BibTeX citation key 使用 `author_year_firstword` 风格，尽量稳定。
- collection 名称表示主题，标签表示机制、物种、组织、方法和项目。
- PDF、网页快照和 Zotero 数据库保留在本地；仓库只放公开 metadata 和脚本。
- 论文的可验证结论放入 [bioinformatics-literature-workbench](https://github.com/Threezs/bioinformatics-literature-workbench) 的 `claims.csv`。
- 需要按机制汇总时使用 [research-evidence-notebook](https://github.com/Threezs/research-evidence-notebook)。

## 参考项目

- [retorquere/zotero-better-bibtex](https://github.com/retorquere/zotero-better-bibtex)
- [fchicout/zotero-cli](https://github.com/fchicout/zotero-cli)
- [bio5paper/zotero-better-notes](https://github.com/wshuyi/zotero-better-notes)
- [r-lib/bibtex](https://github.com/r-lib/bibtex)

