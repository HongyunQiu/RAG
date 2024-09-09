# RAG 实验系统

这是一个用于实验检索增强生成(RAG)系统的项目。

## 安装

1. 克隆此仓库
2. 安装依赖: `pip install -r requirements.txt`
3. 创建.env文件并添加OpenAI API密钥: 
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
   请将`your_api_key_here`替换为您的实际OpenAI API密钥。

## 使用

1. 准备您的数据,并将其放在 `data/` 目录下
2. 修改 `src/main.py` 中的 `load_data()` 函数以适应您的数据格式
3. 运行主程序: `python src/main.py`

## 组件

- Indexer: 用于创建和管理文档的向量索引
- Retriever: 用于检索与查询相关的文档
- Generator: 用于生成最终的回答

## 注意

请确保您有足够的OpenAI API使用额度,因为生成步骤会消耗API调用。